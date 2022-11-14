import requests
import json
import os

apiurl = "https://api.scryfall.com/"

def Main():
    testCard = GetCard(input("input card name: "))
    print("Found Card - " + testCard["name"])
    input()

# Gets card json
def GetCard(x):
    request = "cards/named?fuzzy="
    return requests.get(apiurl + request + x).json()

if __name__ == "__main__":
    Main()
