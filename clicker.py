import keyboard
import mouse
import time
from rich import print

print("[bold yellow]Auto_clicker[/bold yellow]\nДля запуска нажмите [yellow]Alt + C[/yellow]\nРазработчик: [yellow]blaze_edge[/yellow]")

work = False

def switchMode():
    global work
    if work:
        work = False
        print("[red]Кликер отключен[/red]")
    else:
        work = True
        print("[green]Кликер включен[/green]")

keyboard.add_hotkey('alt+c', switchMode)

while True:
    if work:
        mouse.click(button="left")
        time.sleep(0.01)