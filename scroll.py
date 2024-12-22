import tkinter as tk
import pyautogui
import time
import threading

scrolling = False
scrollDelay = 0.01

def toggleScroll():
    global scrolling
    scrolling = not scrolling
    if scrolling:
        scrollButton.config(text="Stop Scrolling")
        threading.Thread(target=scrollLoop, daemon=True).start()
    else:
        scrollButton.config(text="Start Scrolling")

def scrollLoop():
    global scrolling
    while scrolling:
        if root.focus_get() is None:
            speed = speedSlider.get()
            direction = 1 if directionVar.get() == "Up" else -1
            
            scrollAmount = int(speed / 10)
            pyautogui.scroll(direction * scrollAmount)
            
            time.sleep(scrollDelay)
        else:
            time.sleep(0.1)

root = tk.Tk()
root.title("Mouse Scroll Control")

root.attributes('-topmost', True)
root.geometry("300x175")

speedSlider = tk.Scale(root, from_=1, to=200, orient=tk.HORIZONTAL, label="Scroll Speed")
speedSlider.set(100)
speedSlider.pack()

directionVar = tk.StringVar(value="Up")
directionRadioUp = tk.Radiobutton(root, text="Scroll Up", variable=directionVar, value="Up")
directionRadioDown = tk.Radiobutton(root, text="Scroll Down", variable=directionVar, value="Down")
directionRadioUp.pack()
directionRadioDown.pack()

scrollButton = tk.Button(root, text="Start Scrolling", command=toggleScroll)
scrollButton.pack()

root.mainloop()
