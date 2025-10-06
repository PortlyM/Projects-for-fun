import login_backend
import tkinter as tk
from tkinter import ttk, messagebox

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Login window")
        self.geometry("500x500")

        self.label = tk.Label(self, text="Log in or Sign up")
        self.label.pack(pady=20)

        self.button = ttk.Button(self, text="Log in", command=lambda: print(self.on_button_click()))
        self.button.pack(pady=10)

        self.button = ttk.Button(self, text="Sign in", command=lambda: print(self.on_button_click()))
        self.button.pack(pady=10)
    
    def on_button_click(self):
        messagebox.showinfo("Information", "Button has been clicked")


if __name__ == "__main__":
    window = Window()
    window.mainloop()