import tkinter as tk
import os
import webbrowser
import pyperclip

from tkinter import messagebox, ttk, scrolledtext
from PIL import Image, ImageTk
from src.core import process_command
from src.helpers import listen, speak

# GUI for J.A.R.V.I.S. (Just A Rather Very Intelligent System)
class JarvisGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("J.A.R.V.I.S. - Your AI Assistant")
        self.root.geometry("850x550")
        self.root.resizable(False, False)
        self.root.configure(bg="#121212")

        # Load and Display Logo
        self.logo_image = Image.open("assets/jarvis_logo.png")
        self.logo_image = self.logo_image.resize((120, 120)) 
        self.logo = ImageTk.PhotoImage(self.logo_image)
        self.logo_label = tk.Label(root, image=self.logo, bg="#121212")
        self.logo_label.pack(pady=5)

        # Header Label (J.A.R.V.I.S. Branding)
        self.label = tk.Label(root, text="Hello, I am J.A.R.V.I.S.", font=("Helvetica", 20, "bold"), fg="#00E5FF", bg="#121212")
        self.label.pack(pady=10)

        # Input Frame
        self.input_frame = tk.Frame(root, bg="#121212")
        self.input_frame.pack(pady=5)

        # Dropdown for Quick Selection
        self.command_options = [
            "weather New York", "news", "reminder add submit Project Video",
            "reminder view", "search file document.txt"
        ]
        self.command_var = tk.StringVar(value="Enter, Select or Speak a Command")
        self.command_dropdown = ttk.Combobox(
            self.input_frame, textvariable=self.command_var,
            values=self.command_options, width=40, font=("Helvetica", 12)
        )
        self.command_dropdown.grid(row=0, column=1, padx=10, pady=5)

        def button_style(btn):
            btn.configure(
                font=("Helvetica", 12, "bold"), bg="#007BFF", fg="white",
                relief="flat", padx=12, pady=6, bd=2, activebackground="#0056b3",
                borderwidth=0, highlightthickness=0
            )
            btn.config(width=10, height=1)
            btn.bind("<Enter>", lambda e: btn.config(bg="#0056b3")) 
            btn.bind("<Leave>", lambda e: btn.config(bg="#007BFF"))

        # Run Button
        self.run_button = tk.Button(self.input_frame, text="Ask", command=self.process_input)
        button_style(self.run_button)
        self.run_button.grid(row=0, column=2, padx=5, pady=5)

        # Clear Button
        self.clear_button = tk.Button(self.input_frame, text="Clear", command=self.clear_input)
        button_style(self.clear_button)
        self.clear_button.grid(row=0, column=3, padx=5, pady=5)

        # Speak Button
        self.speak_button = tk.Button(
            self.input_frame,
            text="🎤 Speak",
            command=self.speak_input,
            font=("Helvetica", 12, "bold"),
            bg="#00E5FF",
            fg="#0D1B2A",
            relief="flat",
            padx=10,
            pady=5
        )
        self.speak_button.grid(row=0, column=4, padx=15, pady=5)
    

        # Output Box
        self.output_label = tk.Label(root, text="Response:", font=("Helvetica", 14, "bold"), fg="#00E5FF", bg="#121212")
        self.output_label.pack(pady=5)

        self.output_text = scrolledtext.ScrolledText(
            root, height=10, width=80, wrap=tk.WORD,
            font=("Helvetica", 12), bg="#1C1F26", fg="#FFFFFF", insertbackground="white", bd=2, relief="flat"
        )
        self.output_text.pack(pady=5)

    def process_input(self):
        user_input = self.command_var.get().strip().lower()
        if user_input == "Enter your request or select a command":
            messagebox.showerror("Error", "Please enter or select a command!")
            return
        response = process_command(user_input)
        self.display_output(response)

    def display_output(self, text):
        self.output_text.config(state="normal")
        self.output_text.delete("1.0", tk.END)

        if text.startswith("Found:"):
            paths = text.splitlines()[1:]
            for path in paths:
                self.output_text.insert(tk.END, path + "\n")

            # Open Folder button
            open_btn = tk.Button(
                self.output_text,
                text="Open Folder",
                command=lambda p=path: self.open_folder(p),
                font=("Helvetica", 9), bg="#00E5FF", fg="#0B162A", relief="flat", padx=5
            )
            self.output_text.window_create(tk.END, window=open_btn)

            # Copy Path button
            copy_btn = tk.Button(
                self.output_text,
                text="Copy Path",
                command=lambda p=path: self.copy_to_clipboard(p),
                font=("Helvetica", 9), bg="#007BFF", fg="white", relief="flat", padx=5
            )
            self.output_text.window_create(tk.END, window=copy_btn)

            self.output_text.insert(tk.END, "\n\n")
        else:
            self.output_text.insert(tk.END, text)

        self.output_text.config(state="disabled")



    def speak_input(self):
        voice_input = listen()
        self.command_var.set(voice_input)
        response = process_command(voice_input)
        self.display_output(response)
        speak(response)

    
    def clear_input(self):
        self.command_var.set("Enter your request or select a command")
        self.output_text.delete("1.0", tk.END)

    def open_folder(self, file_path):
        import os 
        import webbrowser
        if os.path.exists(file_path):
            folder = os.path.dirname(file_path)
            webbrowser.open(f'file:///{folder}')
        else:
            print("Path not found or inaccessible.")

    def copy_to_clipboard(self, text):
        import pyperclip
        pyperclip.copy(text)

if __name__ == "__main__":
        root = tk.Tk()
        app = JarvisGUI(root)
        root.mainloop()

