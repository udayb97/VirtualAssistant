import tkinter as tk
from tkinter import messagebox, ttk, scrolledtext
from PIL import Image, ImageTk  # Import for handling images
from src.core import process_command  # Importing function from core.py

class JarvisGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("J.A.R.V.I.S. - Your AI Assistant")
        self.root.geometry("700x550")  # Adjusted window size
        self.root.resizable(False, False)
        self.root.configure(bg="#0D1B2A")  # J.A.R.V.I.S. theme dark blue

        # Load and Display Logo
        self.logo_image = Image.open("assets/jarvis_logo.png")  # Load the logo
        self.logo_image = self.logo_image.resize((120, 120))  # Resize
        self.logo = ImageTk.PhotoImage(self.logo_image)
        self.logo_label = tk.Label(root, image=self.logo, bg="#0D1B2A")
        self.logo_label.pack(pady=5)

        # Header Label (J.A.R.V.I.S. Branding)
        self.label = tk.Label(root, text="Hello, I am J.A.R.V.I.S.", font=("Helvetica", 18, "bold"), fg="#00E5FF", bg="#0D1B2A")
        self.label.pack(pady=10)

        # Input Frame
        self.input_frame = tk.Frame(root, bg="#0D1B2A")
        self.input_frame.pack(pady=5)

        # Dropdown for Quick Selection
        self.command_options = [
            "weather New York", "news", "reminder add Buy groceries",
            "reminder view", "search file document.txt"
        ]
        self.command_var = tk.StringVar(value="Type or Select Command")
        self.command_dropdown = ttk.Combobox(
            self.input_frame, textvariable=self.command_var,
            values=self.command_options, width=40, font=("Helvetica", 12)
        )
        self.command_dropdown.grid(row=0, column=1, padx=5, pady=5)

        # Run Button
        self.run_button = tk.Button(self.input_frame, text="Ask", command=self.process_input,
                                    font=("Helvetica", 12, "bold"), bg="#00E5FF", fg="#0D1B2A",
                                    relief="flat", padx=10, pady=5, activebackground="#0088CC")
        self.run_button.grid(row=0, column=2, padx=5, pady=5)

        # Clear Button
        self.clear_button = tk.Button(self.input_frame, text="Clear", command=self.clear_input,
                                      font=("Helvetica", 12, "bold"), bg="#00E5FF", fg="#0D1B2A",
                                      relief="flat", padx=10, pady=5, activebackground="#0088CC")
        self.clear_button.grid(row=0, column=3, padx=5, pady=5)

        # Output Box
        self.output_label = tk.Label(root, text="Response:", font=("Helvetica", 12, "bold"), fg="#00E5FF", bg="#0D1B2A")
        self.output_label.pack(pady=5)

        self.output_text = scrolledtext.ScrolledText(
            root, height=10, width=65, wrap=tk.WORD,
            font=("Helvetica", 12), bg="#1B263B", fg="#FFFFFF", insertbackground="white"
        )
        self.output_text.pack(pady=5)

    def process_input(self):
        user_input = self.command_var.get().strip().lower()
        if user_input == "Type or Select Command":
            messagebox.showerror("Error", "Please enter or select a command!")
            return
        response = process_command(user_input)
        self.display_output(response)

    def display_output(self, text):
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, text)

    def clear_input(self):
        self.command_var.set("Type or Select Command")
        self.output_text.delete("1.0", tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = JarvisGUI(root)
    root.mainloop()
