import PySimpleGUI as sg

left_Col = [
    [sg.Text("Card Name:"), sg.InputText(key='-CARDNAME-'),sg.Button("Search",key='-SEARCH-')],
    [sg.Image(key='-CARDFACE-')],
]

right_Col = [
    []
]

page_One = [
    [
        sg.Column(left_Col),
        sg.VSeperator(),
        sg.Column(right_Col),
    ]
]

def INIGUI(winName,margin):
    return sg.Window(title=winName,layout=page_One,margins=margin)
