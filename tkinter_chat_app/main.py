import tkinter as tk
from tkinter import messagebox
from auth import register_user, verify_user
from chat import ChatApp
from database import create_database

# Initialize database
create_database()

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Chat Application - Login")
        self.root.geometry("400x400")
        self.root.configure(bg="#f0f0f0")

        # Mobile number entry
        tk.Label(root, text="Enter Mobile Number:", bg="#f0f0f0").pack(pady=10)
        self.mobile_entry = tk.Entry(root, width=30)
        self.mobile_entry.pack(pady=5)

        # OTP entry
        tk.Label(root, text="Enter OTP:", bg="#f0f0f0").pack(pady=10)
        self.otp_entry = tk.Entry(root, width=30, show="*")
        self.otp_entry.pack(pady=5)

        # Buttons
        tk.Button(root, text="Register & Send OTP", command=self.register, bg="#4CAF50", fg="white").pack(pady=10)
        tk.Button(root, text="Verify & Login", command=self.verify, bg="#2196F3", fg="white").pack(pady=10)

    def register(self):
        mobile_number = self.mobile_entry.get()
        if mobile_number:
            otp = register_user(mobile_number)
            messagebox.showinfo("OTP Sent", f"OTP sent to {mobile_number}. (For testing: {otp})")
        else:
            messagebox.showerror("Error", "Please enter a valid mobile number.")

    def verify(self):
        mobile_number = self.mobile_entry.get()
        otp = self.otp_entry.get()
        if verify_user(mobile_number, otp):
            messagebox.showinfo("Success", "Login successful!")
            self.root.destroy()
            self.open_chat_app(mobile_number)
        else:
            messagebox.showerror("Error", "Invalid OTP or mobile number.")

    def open_chat_app(self, mobile_number):
        chat_root = tk.Tk()
        ChatApp(chat_root, mobile_number)
        chat_root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    LoginApp(root)
    root.mainloop()
