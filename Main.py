import requests as req
import json
import os
import time
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
            card = ''.join(values["-CARDNAME-"]).replace(' ',"_")
            print("looking for " + card)
            cardData = GetCard(card)
            if cardData != None:
                print("FOUND CARD")
            # change image on screen to card
            print("URL = " + cardData['image_uris']['large'])
            cardImg = Download(cardData['image_uris']['large'])
            with open("temp/" + card + ".jpg",'wb') as handler:
                handler.write(cardImg)
            time.sleep(3)
            values["-CARDFACE-"].update(filename="temp/" + card + ".jpg")


# Gets card json
def GetCard(x):
    request = "cards/named?fuzzy="
    return req.get(apiurl + request + x).json()

def Download(url):
    return req.get(url).content

if __name__ == "__main__":
    Main()
