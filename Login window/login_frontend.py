import login_backend
import tkinter as tk
from tkinter import ttk, messagebox

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Login panel")
        self.geometry("350x300")

        container = tk.Frame(self)
        container.pack(fill="both", expand=True)
        self.frames = {}

        for F in (MainWindow, Login_window, Sign_in_window):
            page_name = F.__name__
            frame = F(container, self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("MainWindow")
    
    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

class MainWindow(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller

        self.label = tk.Label(self, text="Log in or Sign up")
        self.label.pack(pady=20)

        self.button = ttk.Button(self, text="Log in", command=lambda: controller.show_frame("Login_window"))
        self.button.pack(pady=10)

        self.button = ttk.Button(self, text="Sign in", command=lambda: controller.show_frame("Sign_in_window"))
        self.button.pack(pady=10)  

class Login_window(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller

        self.label = tk.Label(self, text="Log in")
        self.label.pack(pady=10)

        self.login_entry = tk.Entry(self, width=50)
        self.login_entry.pack(pady=5, padx=5)

        self.password_entry = tk.Entry(self, width=50)
        self.password_entry.pack(pady=5, padx=5)

        self.button = ttk.Button(self, text="Back", command=lambda: controller.show_frame("MainWindow"))
        self.button.pack(pady=10)

class Sign_in_window(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller

        self.label = tk.Label(self, text="Sign in")
        self.label.pack(pady=10)

        self.name_entry = tk.Entry(self, width=50)
        self.name_entry.pack(pady=5, padx=5)

        self.last_name_entry = tk.Entry(self, width=50)
        self.last_name_entry.pack(pady=5, padx=5)

        self.login_entry = tk.Entry(self, width=50)
        self.login_entry.pack(pady=5, padx=5)

        self.password_entry = tk.Entry(self, width=50)
        self.password_entry.pack(pady=5, padx=5)

        self.button = ttk.Button(self, text="Back", command=lambda: controller.show_frame("MainWindow"))
        self.button.pack(pady=10)


if __name__ == "__main__":
    window = Window()
    window.mainloop()