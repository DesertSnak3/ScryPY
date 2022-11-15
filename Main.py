import requests as req
import json
import os
import PySimpleGUI as sg
#########################
# File imports
#########################
import GUI

apiurl = "https://api.scryfall.com/"

def Main():
    #create GUI
    window = GUI.INIGUI('ScryPY',(500,500))

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'EXIT':
            break
        elif event == "-SEARCH-":
            # get user card input
            card = ''.join(values["-CARDNAME-"])
            cardData = GetCard(card)
            # change image on screen to card
            #req.get(apiurl + "cards/named?exact=" + cardData["name"] + "?face=front").image()


# Gets card json
def GetCard(x):
    request = "cards/named?fuzzy="
    return req.get(apiurl + request + x).json()

if __name__ == "__main__":
    Main()
