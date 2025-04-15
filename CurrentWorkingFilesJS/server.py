#Joseph Saponaro Apr 14th 2025
#Advanced version of the server code. Uses fastapi to serve the html file to the server.
#To start the server type: python -m uvicorn server:app --host 0.0.0.0 --port 8765
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from collections import defaultdict

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def get():
    return HTMLResponse(open("static/simple_client.html", encoding="utf-8").read())

# username -> websocket
connected_clients = {}
user_scores = defaultdict(int)
user_votes = defaultdict(str)

questions = {
    "Science": {"question": "What planet is known as the Red Planet?", "answer": "Mars"},
    "History": {"question": "Who discovered America?", "answer": "Christopher Columbus"},
    "Geography": {"question": "What is the largest ocean on Earth?", "answer": "Pacific Ocean"}
}

current_question = {"topic": None, "text": "", "answer": ""}

async def broadcast(message: str):
    for ws in connected_clients.values():
        await ws.send_text(message)

async def update_user_list():
    user_list = ",".join(connected_clients.keys())
    await broadcast(f"Users:{user_list}")

async def update_leaderboard():
    leaderboard = "Leaderboard:\n"
    for name, score in sorted(user_scores.items(), key=lambda x: -x[1]):
        leaderboard += f"{name}: {score} points\n"
    await broadcast(leaderboard)

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    # temp name until join
    username = f"client_{id(websocket)}" 
    connected_clients[username] = websocket

    try:
        while True:
            data = await websocket.receive_text()
            print(f"Received: {data}")

            if data.startswith("Join:"):
                username = data.split(":", 1)[1].strip()
                connected_clients[username] = websocket
                await broadcast(f"{username} joined the game.")
                await update_user_list()
                if current_question["text"]:
                    await websocket.send_text(f"Question: {current_question['text']}")

            elif data.startswith("Chat:"):
                _, name, text = data.split(":", 2)
                await broadcast(f"{name}: {text}")

            elif data.startswith("Vote:"):
                _, name, topic = data.split(":", 2)
                user_votes[name] = topic
                await broadcast(f"{name} voted for {topic}")
                #added to avoid the clients being counted as users toward votes
                real_users = [u for u in connected_clients if not u.startswith("client_")]
                if len(user_votes) == len(real_users):
                    winning_topic = max(set(user_votes.values()), key=list(user_votes.values()).count)
                    q = questions[winning_topic]
                    current_question["topic"] = winning_topic
                    current_question["text"] = q["question"]
                    current_question["answer"] = q["answer"]
                    await broadcast(f"Question: {q['question']}")
                    user_votes.clear()

            elif data.startswith("Answer:"):
                _, name, answer = data.split(":", 2)
                correct = answer.strip().lower() == current_question["answer"].lower()
                await broadcast(f"{name} answered {'correctly' if correct else 'incorrectly'}.")
                if correct:
                    user_scores[name] += 1
                await update_leaderboard()

            elif data.startswith("HostCommand:"):
                command = data.split(":", 1)[1].strip().upper()
                if command == "NEXT":
                    await broadcast("Host is starting the next round. Vote now!")
                elif command == "RESET":
                    user_scores.clear()
                    await broadcast("Scores have been reset!")
                    await update_leaderboard()

    except WebSocketDisconnect:
        if username in connected_clients:
            del connected_clients[username]
            await broadcast(f"{username} left the game.")
            await update_user_list()
