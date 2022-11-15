import requests
import json
import os
import GUI

apiurl = "https://api.scryfall.com/"

def Main():
    #create GUI
    window = GUI.INIGUI('ScryPY',(500,500))

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break
        elif event == "-SEARCH-":
            print("OK")

# Gets card json
def GetCard(x):
    request = "cards/named?fuzzy="
    return requests.get(apiurl + request + x).json()

if __name__ == "__main__":
    Main()
