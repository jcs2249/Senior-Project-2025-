using System;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using NativeWebSocket;
using TMPro;

public class WebSocketReceiver : MonoBehaviour
{
    private WebSocket websocket;

    public TMP_Text logText;
    public TMP_Text questionText;
    public TMP_Text leaderboardText;
    public TMP_Text usersText;
    public Button connectButton;
    public Button nextRoundButton;
    public Button resetScoresButton;

    private List<string> messageHistory = new List<string>();
    private const int maxMessages = 10;

    void Start()
    {
        connectButton.onClick.AddListener(ConnectToServer);
        nextRoundButton.onClick.AddListener(() => SendHostCommand("NEXT"));
        resetScoresButton.onClick.AddListener(() => SendHostCommand("RESET"));
    }

    async void ConnectToServer()
    {
        websocket = new WebSocket("wss://aarj.ngrok.io/ws");

        websocket.OnOpen += () => AddLog("Connected to server.");
        websocket.OnMessage += (bytes) =>
        {
            string message = System.Text.Encoding.UTF8.GetString(bytes);
            Debug.Log("📩 " + message);

            if (message.StartsWith("Question:"))
            {
                string q = message.Substring("Question:".Length).Trim();
                questionText.text = q;
                AddLog("❓ " + q);
            }
            else if (message.StartsWith("Leaderboard:"))
            {
                leaderboardText.text = message;
            }
            else if (message.StartsWith("Users:"))
            {
                string[] users = message.Substring(6).Split(',');
                usersText.text = "Users:\n" + string.Join("\n", users);
            }
            else
            {
                AddLog(message);
            }
        };

        websocket.OnClose += (e) => AddLog("Disconnected.");
        websocket.OnError += (e) => AddLog("Error: " + e);

        await websocket.Connect();
    }

    void Update()
    {
#if !UNITY_WEBGL || UNITY_EDITOR
        websocket?.DispatchMessageQueue();
#endif
    }

    async void OnApplicationQuit()
    {
        if (websocket != null && websocket.State == WebSocketState.Open)
            await websocket.Close();
    }

    void AddLog(string message)
    {
        messageHistory.Add(message);
        if (messageHistory.Count > maxMessages)
            messageHistory.RemoveAt(0);
        logText.text = string.Join("\n", messageHistory);
    }

    async void SendHostCommand(string command)
    {
        if (websocket != null && websocket.State == WebSocketState.Open)
            await websocket.SendText($"HostCommand:{command}");
    }
}
