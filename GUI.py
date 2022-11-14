import PySimpleGUI as sg

ly = [[sg.Text("Hello from PySimpleGUI")], [sg.Button("OK")]]

window = sg.Window(title="ScryPY",layout=ly,margins=(400,200))

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == "OK":
        print("OK")
        break

window.close()
