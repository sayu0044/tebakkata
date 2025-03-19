import tkinter as tk
from tkinter import messagebox
import random

# Gunakan daftar kata yang lebih luas (bisa diperluas dengan file)
word_list = ["apple", "grape", "mango", "peach", "berry", "lemon", "melon", "chili", "plums", "guava", 
             "merah", "putih", "hitam", "biru", "hijau", "kuning", "cokel", "ungu", "abuab", "orany"]
secret_word = random.choice(word_list)  # Pilih kata acak
max_attempts = 6
attempts = 0

def check_word():
    global attempts
    guess = entry_word.get().strip().lower()
    
    if len(guess) != 5:
        messagebox.showerror("Error", "Kata harus terdiri dari 5 huruf!")
        return
    
    # Hapus pengecekan kata dari word_list agar pengguna bisa menebak kata bebas
    attempts += 1
    for i in range(5):
        letter = guess[i]
        if letter == secret_word[i]:
            labels[attempts - 1][i].config(text=letter, bg="green", fg="white")
        elif letter in secret_word:
            labels[attempts - 1][i].config(text=letter, bg="yellow", fg="black")
        else:
            labels[attempts - 1][i].config(text=letter, bg="gray", fg="white")
    
    if guess == secret_word:
        messagebox.showinfo("Selamat!", "Anda menebak kata dengan benar!")
        root.quit()
    elif attempts >= max_attempts:
        messagebox.showinfo("Game Over", f"Kata yang benar: {secret_word}")
        root.quit()

def reset_game():
    global secret_word, attempts
    secret_word = random.choice(word_list)
    attempts = 0
    for row in labels:
        for label in row:
            label.config(text="", bg="white")
    entry_word.delete(0, tk.END)

# GUI Setup
root = tk.Tk()
root.title("Tebak Kata - Wordly")
root.geometry("400x500")

tk.Label(root, text="Tebak kata 5 huruf:").pack()
entry_word = tk.Entry(root, font=("Arial", 14))
entry_word.pack()
tk.Button(root, text="Cek Kata", command=check_word).pack()

tk.Label(root, text="\nPercobaan:").pack()
labels = []
for i in range(max_attempts):
    row = []
    frame = tk.Frame(root)
    frame.pack()
    for j in range(5):
        lbl = tk.Label(frame, text="", width=4, height=2, font=("Arial", 16), relief="solid", bg="white")
        lbl.pack(side=tk.LEFT, padx=2, pady=2)
        row.append(lbl)
    labels.append(row)

tk.Button(root, text="Reset", command=reset_game).pack()
root.mainloop()
