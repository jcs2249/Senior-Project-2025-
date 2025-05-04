Senior project 2025. Joseph Saponaro, Robert Bossert, Ava McFadden, Andrew Barrera

Inteller, a spy‑themed, real‑time trivia experience where players join via a web client, vote on topics, submit answers, and the game host (built in Unity) orchestrates rounds, timers, and leaderboards.

---

Features

- **Agent Lobby & Voting**  
  Players join with a codename, chat in real‑time, and vote on one of the topic categories each round.

- **Dynamic Questions**  
  Topic‑based question pools are stored in Python; the server picks a random question once voting completes.

- **Round Timer & Scoring**  
  A 30‑second countdown locks out answers when time’s up. Correct answers earn points; the Unity host is notified when scoring closes.

- **Spy Theme UI**  
  Black‑and‑white “Spy vs Spy” aesthetic across HTML and Unity, with typewriter effects, transmission banners, and sound cues.

- **Host Controls in Unity**  
  Next Round, Reset Scores, Close Game, and volume controls. The Unity window is resizable and displays chat, the current question, the leaderboard, and online users.

---

Tech Stack

| Layer              | Technology                              |
|--------------------|-----------------------------------------|
| Frontend (Client)  | HTML5, CSS, Vanilla JavaScript, WebSockets |
| Backend (Server)   | Python3 + FastAPI + `uvicorn` + WebSocket |
| Tunneling          | ngrok (for public HTTPS testing)        |
| Game Host (Admin)  | Unity2021+ (C#) + TextMeshPro + NativeWebSocket |
| Data               | In‑memory Python dict (from Excel/JSON) |
