import tkinter as tk
from tkinter import messagebox
import random

INITIAL_TIME_LIMIT = 30
TIME_LIMIT = INITIAL_TIME_LIMIT
TIMER_RUNNING = False

texts = [
    "In the heart of the dense forest, where ancient trees stood tall and proud, there lived a tribe of skilled hunters and gatherers. Their days were filled with reverence for the natural world around them, and their nights were illuminated by the flickering light of the campfire. The elders of the tribe passed down stories of bravery and wisdom, teaching the younger generations the ways of survival and harmony with nature.",
    "Deep within the labyrinthine corridors of the old castle, whispers of ghosts and forgotten secrets echoed through the stone walls. Each room held a story untold, each passageway a mystery waiting to be unraveled. Many brave adventurers had ventured into the castle, seeking fame and fortune, only to be ensnared by the castle's dark enchantments. But legends spoke of a hidden treasure, guarded by a curse that only the purest of hearts could break.",
    "On the distant shores of an undiscovered island, where the emerald waters kissed the white sandy beaches, a solitary figure stood gazing at the horizon. The island was untouched by human hands, its beauty preserved by the mystical creatures that called it home. As the sun dipped below the horizon, casting hues of pink and orange across the sky, the figure felt a sense of belonging, a connection to the untamed wilderness that surrounded them.",
    "Amidst the bustling streets of the futuristic city, where neon lights illuminated the night sky and hovercrafts glided silently above, a group of rebels plotted their next move against the tyrannical regime. They operated from hidden underground tunnels, using advanced technology to evade detection and spread messages of hope among the oppressed citizens. Their leader, a charismatic figure with a past shrouded in mystery, inspired courage and defiance in the hearts of those who dared to dream of freedom.",
    "In the sprawling metropolis where dreams were born and shattered in equal measure, a young artist painted murals that captured the soul of the city. Each stroke of the brush conveyed a story of resilience and passion, reflecting the struggles and triumphs of everyday life. Tourists from around the world flocked to see the murals, drawn by the artist's unique perspective and bold use of color. The city skyline became a canvas, showcasing the artist's vision of hope and unity in a world filled with chaos and uncertainty."
]

def start_test():
    global TIMER_RUNNING, TIME_LIMIT
    TIMER_RUNNING = True
    TIME_LIMIT = INITIAL_TIME_LIMIT
    entry.config(state=tk.NORMAL)
    entry.delete("1.0", tk.END)
    start_button.config(state=tk.DISABLED)
    reset_button.config(state=tk.NORMAL)
    countdown()

def countdown():
    global TIME_LIMIT
    if TIME_LIMIT > 0 and TIMER_RUNNING:
        timer_label.config(text=f"Remaining time: {TIME_LIMIT}")
        TIME_LIMIT -= 1
        window.after(1000, countdown)
    else:
        timer_label.config(text="Remaining time: 0")
        end_test()

def end_test():
    global TIMER_RUNNING
    TIMER_RUNNING = False
    entry.config(state=tk.DISABLED)
    calculate_cpm()

def reset_test():
    global TIME_LIMIT, TIMER_RUNNING
    TIMER_RUNNING = False
    TIME_LIMIT = INITIAL_TIME_LIMIT
    entry.config(state=tk.DISABLED)
    entry.delete("1.0", tk.END)
    timer_label.config(text=f"Remaining time: {TIME_LIMIT}")
    start_button.config(state=tk.NORMAL)
    reset_button.config(state=tk.DISABLED)
    goal_text.config(text=random.choice(texts))

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f"{width}x{height}+{x}+{y}")

def check_input(event):
    current_text = entry.get("1.0", tk.END).strip()
    correct_text = goal_text.cget("text")[:len(current_text)]
    if current_text != correct_text:
        entry.delete("end-2c")
        entry.config(bg="red")
        window.after(500, lambda: entry.config(bg="white"))

def calculate_cpm():
    typed_text = entry.get("1.0", tk.END).strip()
    characters_typed = len(typed_text)
    time_taken_seconds = INITIAL_TIME_LIMIT - TIME_LIMIT
    time_taken_minutes = time_taken_seconds / 60
    cpm = (characters_typed / time_taken_minutes) if time_taken_minutes > 0 else 0
    messagebox.showinfo("Typing Report", f"Characters per minute: {int(cpm)}")
    entry.delete("1.0", tk.END)

window = tk.Tk()
window.title("Typing Speed Test")
window_width = 1200
window_height = 800
center_window(window, window_width, window_height)

instruction_label = tk.Label(window, text="Goal text:", font=("Helvetica", 20))
instruction_label.grid(row=0, column=0, padx=200, pady=(40,20))

goal_text = tk.Label(window, text=random.choice(texts), wraplength=800, font=("Helvetica", 16))
goal_text.grid(row=1, column=0, padx=200)

entry = tk.Text(window, height=12, width=100)
entry.grid(row=2, column=0, pady=(50,20))
entry.config(state=tk.DISABLED)
entry.bind("<KeyRelease>", check_input)

start_button = tk.Button(window, text="Start", width=20, height=2, command=start_test, font=("Helvetica", 16))
start_button.grid(row=3, column=0)

reset_button = tk.Button(window, text="Reset", width=20, height=2, command=reset_test, font=("Helvetica", 16), state=tk.DISABLED)
reset_button.grid(row=4, column=0, pady=(20, 0))

timer_label = tk.Label(window, text=f"Remaining time: {TIME_LIMIT}", pady=50, font=("Helvetica", 16))
timer_label.grid(row=5, column=0)

window.mainloop()
