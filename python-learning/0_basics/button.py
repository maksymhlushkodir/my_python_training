import tkinter as tk
from tkinter import messagebox

def on_button_click():
    messagebox.showinfo("Hello!", "You clicked the button!")

# Створення головного вікна
screen = tk.Tk()
screen.title("My first GUI")
screen.geometry("300x200") # Розмір вікна (ширина x висота)

# Додаємо напис
label = tk.Label(screen, text="This is my first interface!", font=("Arial", 16))
label.pack(pady=20) # pady — відступ зверху і знизу

# Додаємо кнопку
button = tk.Button(screen, text="Click me", command=on_button_click, bg="#4CAF50", fg="white")
button.pack(pady=20)

# Запускаємо головний цикл
screen.mainloop()