import tkinter as tk

screen = tk.Tk()
screen.title("Text flipper")
screen.geometry("800x600")

text_input = tk.Entry(screen, width=20, font=("Arial", 20))
text_input.pack(pady=10)

label = tk.Label(screen, text="Тут буде твій текст...", font=("Arial", 20))
label.pack(pady=10)

def text_flipper():
    user_text = text_input.get()  # Отримуємо текст з Entry
    reversed_text = user_text[::-1]  # Перевертаємо текст
    label.config(text=f"Ваш інвертований текст: {reversed_text}")  # Виводимо

button = tk.Button(screen, text="перевернути текст", command=text_flipper, bg="#009933", fg="white")
button.pack(pady=10)

screen.mainloop()