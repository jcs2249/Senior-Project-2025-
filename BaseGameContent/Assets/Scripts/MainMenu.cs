using System.Collections;
using System.Collections.Generic;
using Unity.VisualScripting;
using UnityEngine;
using UnityEngine.SceneManagement;


public class MainMenu : MonoBehaviour
{

    public void HostLobby()
    {
        //Generate room code
    }

    public void Quit()
    {
        Application.Quit();
        Debug.Log("The Host has left the game");
    }

    /* Things to add:
     *      - Settings Menu: Volume
     *      - Detect first player to join + make them host
     *      - Once host presses the "start" button on their screen, send *all* players to the next scene
     */

}
