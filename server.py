#Joseph Saponaro Apr 14th 2025
#Advanced version of the server code. Uses fastapi to serve the html file to the server.
#To start the server type: python -m uvicorn server:app --host 0.0.0.0 --port 8765
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from collections import defaultdict
import random

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def get():
    return HTMLResponse(open("static/simple_client.html", encoding="utf-8").read())

connected_clients = {}
user_scores = defaultdict(int)
user_votes = defaultdict(str)
current_question = {"topic": None, "text": "", "answer": ""}
accepting_answers = True  # 🔐 Flag for timer-based answer cutoff

questions = {
    "Science": [
        {"question": "What planet is known as the Red Planet?", "answer": "Mars"},
        {"question": "What gas do plants absorb from the atmosphere?", "answer": "Carbon Dioxide"},
        {"question": "What is the chemical symbol for water?", "answer": "H2O"},
    ],
    "History": [
        {"question": "Who discovered America?", "answer": "Christopher Columbus"},
        {"question": "What year did World War II end?", "answer": "1945"},
        {"question": "Who was the first President of the United States?", "answer": "George Washington"},
    ],
    "Geography": [
        {"question": "What is the largest ocean on Earth?", "answer": "Pacific Ocean"},
        {"question": "Which continent is the Sahara Desert located in?", "answer": "Africa"},
        {"question": "What is the capital of France?", "answer": "Paris"},
    ],
    "Literature": [
        {"question": "Who wrote '1984'?", "answer": "George Orwell"},
        {"question": "What is the name of Sherlock Holmes’ assistant?", "answer": "Dr. Watson"},
    ],
    "Movies": [
        {"question": "Who directed Jurassic Park?", "answer": "Steven Spielberg"},
        {"question": "Which film features the quote 'I am your father'?", "answer": "The Empire Strikes Back"},
    ]
}

async def broadcast(message: str):
    for ws in connected_clients.values():
        await ws.send_text(message)

async def update_user_list():
    real_users = [u for u in connected_clients if not u.startswith("client_")]
    user_list = ",".join(real_users)
    await broadcast(f"Users:{user_list}")

async def update_leaderboard():
    leaderboard = "Leaderboard:\n"
    for name, score in sorted(user_scores.items(), key=lambda x: -x[1]):
        leaderboard += f"{name}: {score} points\n"
    await broadcast(leaderboard)

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    temp_name = f"client_{id(websocket)}"
    connected_clients[temp_name] = websocket

    try:
        while True:
            data = await websocket.receive_text()

            if data.startswith("Join:"):
                username = data.split(":", 1)[1].strip()
                if temp_name in connected_clients:
                    del connected_clients[temp_name]
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
                real_users = [u for u in connected_clients if not u.startswith("client_")]
                if len(user_votes) == len(real_users):
                    winning_topic = max(set(user_votes.values()), key=list(user_votes.values()).count)
                    if winning_topic in questions:
                        q = random.choice(questions[winning_topic])
                        current_question["topic"] = winning_topic
                        current_question["text"] = q["question"]
                        current_question["answer"] = q["answer"]
                        global accepting_answers
                        accepting_answers = True
                        await broadcast(f"Question: {q['question']}")
                        user_votes.clear()

            elif data.startswith("Answer:"):
                _, name, answer = data.split(":", 2)
                correct = answer.strip().lower() == current_question["answer"].lower()
                if correct and accepting_answers:
                    user_scores[name] += 1
                    await broadcast(f"{name} answered correctly.")
                else:
                    await broadcast(f"{name} answered {'correctly' if correct else 'incorrectly'}, but scoring is {'open' if accepting_answers else 'closed'}.")
                await update_leaderboard()

            elif data.startswith("HostCommand:"):
                command = data.split(":", 1)[1].strip().upper()
                if command == "NEXT":
                    accepting_answers = True
                    await broadcast("Host is starting the next round. Vote now!")
                elif command == "RESET":
                    user_scores.clear()
                    await broadcast("Scores have been reset!")
                    await update_leaderboard()
                elif command == "ROUNDOVER":
                    accepting_answers = False
                    await broadcast("Time's up! No more scoring until next round.")

    except WebSocketDisconnect:
        for name, ws_ref in list(connected_clients.items()):
            if ws_ref == websocket:
                del connected_clients[name]
                await broadcast(f"{name} left the game.")
                await update_user_list()
                break
