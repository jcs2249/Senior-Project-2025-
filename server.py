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
accepting_answers = True  #Flag for timer-based answer cutoff

#Question dictionary for the trivia
questions = {

  "Lizards": [
    {"question": "- (Options: -, -, -, -)", "answer": "-"},
    {"question": "Which of the following Gecko types do *not* have sticky toe-pads? (Options: Crested Geckos, Giant Cave Geckos, Leopard Geckos, Tokay Geckos)", "answer": "Leopard Geckos"},
    {"question": "How do crested geckos get rid of their sheds? (Options: They Burn It, They Eat It, They Give it to a Friend, They Throw it Away)", "answer": "They Eat It"},
    {"question": "What lizard has two clusters of fingers? (Options: Anole, Bearded Dragon, Chameleon, Gila Monster)", "answer": "Chameleon"},
    {"question": "What do Plated Lizards eat? (Options: All of the Above, Fruit, Insects, Other Lizards)", "answer": "All of the Above"},
    {"question": "Tegus are bigger than Komodo Dragons (Options: -, -, -, False)", "answer": "False"},
    {"question": "Salamanders are a type of lizard (Options: -, -, -, False)", "answer": "False"},
  ],
    "Spy": [
    {"question": "Which is NOT one of the steps in the CIA's Intelligence Cycle? (Options: Collection, Dissemination, Production, Protection)", "answer": "Protection"},
    {"question": "Which of the following is NOT a real spy tool used in the past? (Options: Cigarette Packet Detonator, Dog Doo Transmitter, Insectothopter, The Lipstick Pistol)", "answer": "Cigarette Packet Detonator"},
    {"question": "Which cryptid is associated with the state of Pennsylvania? (Options: The Bigfoot, The Momo, The Squonk, The Wendigo)", "answer": "The Squonk"},
    {"question": "- (Options: -, -, -, -)", "answer": "-"},
    {"question": "The first Spy vs Spy comic strip was released in January 1961 (Options: -, -, -, True)", "answer": "True"},
    {"question": "George Washington was a Spymaster (Options: -, -, -, True)", "answer": "True"},
    {"question": "In cyber security, CIA stands for Confidentiality, Integrity, and Access (Options: -, -, -, False)", "answer": "False"},
    {"question": "Skin-Walkers are the cryptid often associated with Wyoming (Options: -, -, -, False)", "answer": "False"},
    {"question": "On which continent can lizards *not* be found? (Options: -, -, -, Antarctica)", "answer": "Antarctica"},
    {"question": "Which continent are Bearded Dragons native to? (Options: -, -, -, Australia)", "answer": "Australia"},
    {"question": "This phrase is often used to describe animals whose body temperature fluctuates with their surroundings (2 words) (Options: -, -, -, Cold Blooded)", "answer": "Cold Blooded"},
    {"question": "Which U.S. State has the Gila Monster as its state reptile? (Options: -, -, -, Utah)", "answer": "Utah"},
    {"question": "What is the name of the secret code that utilizes dots and dashes? (Options: -, -, -, Morse Code)", "answer": "Morse Code"},
    {"question": "This substance used for secret writing could be revealed using heat, ultraviolet light, or a specific chemical (Options: -, -, -, Invisible Ink)", "answer": "Invisible Ink"},
    {"question": "This species of bird was often outfitted with cameras for espionage or tasked with carrying messages during World War I (Options: -, -, -, Pigeon)", "answer": "Pigeon"},
    {"question": "Originating in 1953, this fictional Secret Service Agent nicknamed 007 featured in at least 12 novels and 2 story collections written by their creator (Options: -, -, -, James Bond)", "answer": "James Bond"},
    {"question": "Originally intended for use in radar-based detection, this form of electromagnetic radiation is now used to heat food (plural answer) (Options: -, -, -, Microwaves)", "answer": "Microwaves"},
    {"question": "Previously issued as an undergarment by the US Navy, this short-sleeved article of clothing became widely accepted as a form of outerwear by the 1950s  (Options: -, -, -, T-Shirt)", "answer": "T-Shirt"},
    {"question": "In 1928, Walter E. Diemer created a new formula of bubble gum that improved on its 1906 predecessor. What did Diemer name it? (Options: -, -, -, Double Bubble)", "answer": "Double Bubble"},
    {"question": "In 1930, what we now know as the Chocolate Chip Cookie was invented at an inn by accident. What was it called originally? (Options: -, -, -, Toll House Cookie)", "answer": "Toll House Cookie"},
    {"question": "What is the name of the most notorious entity rumored to reside within one of Scotland's many bodies of water? (Options: -, -, -, Loch Ness Monster)", "answer": "Loch Ness Monster"},
    {"question": "What is the name of the military installation that is often associated with extraterrestrial activity? (Options: -, -, -, Area 51)", "answer": "Area 51"},
    {"question": "Originating from a movie released in the early 1980's, this fictional alien befriends a 10-year-old boy while trying to find a way back to his people (Options: -, -, -, ET)", "answer": "ET"},
    {"question": "Existing as a form of pseudoscience, this term describes the study of and search for undiscovered (and often legendary) animals (Options: -, -, -, Cryptozoology)", "answer": "Cryptozoology"},
    {"question": "Written as ...---... in Morse Code, this acronym is used as a distress signal in emergency situations (Options: -, -, -, SOS)", "answer": "SOS"},
    {"question": "Complete the sentence: According to NASA, the four basic needs for survival include Food, Water, Air, and ______ (Options: -, -, -, Shelter)", "answer": "Shelter"},
    {"question": "What type of natural disaster is typically denoted by a drastic change in sea level after an earthquake? (Options: -, -, -, Tsunami)", "answer": "Tsunami"},
    {"question": "On average, around how many days can someone survive without water (numerical value)? (Options: -, -, -, 3)", "answer": "3"},
  ],

  "Supernatural": [
    {"question": "Which U.S. state has the most reported UFO sightings? (Options: California, Florida, Nevada, Washington)", "answer": "California"},
    {"question": "Which of the following is NOT a New Jersey urban legend? (Options: Captain Kidd, Salem Church Road, The Leeds Devil, The White Stag)", "answer": "Salem Church Road"},
    {"question": "Which of the following is a tool used for ghost hunting? (Options: All of the Above, EMF Reader, Spirit Box, Thermal Imaging Camera)", "answer": "All of the Above"},
    {"question": "- (Options: -, -, -, -)", "answer": "-"},
    {"question": "It is believed that salt can be used to repel ghosts and demons (Options: -, -, -, True)", "answer": "True"},
    {"question": "Washington has the most reported Bigfoot sightings out of all of the U.S. states (Options: -, -, -, True)", "answer": "True"},
  ],

  "Survival": [
    {"question": "Which is NOT one of the steps in the 3-part method to extinguish a fire on your person? (Options: Drop, Jump, Roll, Stop)", "answer": "Jump"},
    {"question": "When performing CPR on a baby, which of the following should be used for chest compressions? (Options: None of the Above, One Hand, Two Fingers, Two Hands)", "answer": "Two Fingers"},
    {"question": "- (Options: -, -, -, -)", "answer": "-"},
    {"question": "Basilisks can run on water (Options: -, -, -, True)", "answer": "True"},
    {"question": "It is a smart idea to boil unfiltered water before drinking it (Options: -, -, -, True)", "answer": "True"},
    {"question": "Water should never be used to extinguish a grease fire (Options: -, -, -, True)", "answer": "True"},
    {"question": "Wild snakes in the U.S. are safe to handle so long as they are not a pit viper (which are notoriously venomous) (Options: -, -, -, False)", "answer": "False"},
  ],
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
