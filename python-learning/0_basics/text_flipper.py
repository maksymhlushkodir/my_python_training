import tkinter as tk

screen = tk.Tk()
screen.title("Text Flipper Pro")
screen.geometry("800x600")

text_input = tk.Entry(screen, width=20, font=("Arial", 20))
text_input.pack(pady=10)

label = tk.Label(screen, text="Тут буде твій текст...", font=("Arial", 20))
label.pack(pady=10)

def text_flipper():
    user_text = text_input.get()  # Отримуємо поточний текст
    reversed_text = user_text[::-1]  # Інвертуємо рядок
    label.config(text=f"Інвертований текст: {reversed_text}")

def text_clear():
    text_input.delete(0, tk.END)  # Очищаємо поле вводу
    label.config(text="Тут буде твій текст...")  # Скидаємо напис

button_flip = tk.Button(
    screen,
    text="Перевернути текст",
    command=text_flipper,
    bg="#009933",
    fg="white"
)
button_flip.pack(pady=10)

button_clear = tk.Button(
    screen,
    text="Очистити",
    command=text_clear,
    bg="#ff0000",  # Червоний для наочності
    fg="white"
)
button_clear.pack(pady=10)

screen.mainloop()
