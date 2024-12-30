import tkinter as tk
from tkinter import scrolledtext

class ChatApp:
    def __init__(self, root, mobile_number):
        self.root = root
        self.root.title(f"Chat - {mobile_number}")
        self.root.geometry("500x500")
        self.root.configure(bg="#f0f0f0")

        # Chat display area
        self.chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=20, state='disabled')
        self.chat_area.pack(pady=10)

        # Message entry area
        self.message_entry = tk.Entry(root, width=50)
        self.message_entry.pack(pady=5, side=tk.LEFT, padx=5)

        # Send button
        self.send_button = tk.Button(root, text="Send", command=self.send_message, bg="#4CAF50", fg="white")
        self.send_button.pack(side=tk.LEFT)

    def send_message(self):
        message = self.message_entry.get()
        if message.strip():
            self.display_message(f"You: {message}")
            # Simulate receiving a reply
            self.display_message("Bot: Thanks for your message!")
        self.message_entry.delete(0, tk.END)

    def display_message(self, message):
        self.chat_area.config(state='normal')
        self.chat_area.insert(tk.END, f"{message}\n")
        self.chat_area.config(state='disabled')
        self.chat_area.yview(tk.END)
