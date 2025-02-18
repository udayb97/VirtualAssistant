import tkinter as tk
from tkinter import messagebox
from src.core import process_command  # Importing function from core.py

class AssistantGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Virtual Assistant")
        self.root.geometry("500x400")  # Set window size
        # Title Label
        self.label = tk.Label(root, text="Personal Assistant", font=("Arial", 16, "bold"))
        self.label.pack(pady=10)
        # Input Field
        self.input_text = tk.StringVar()
        self.input_entry = tk.Entry(root, textvariable=self.input_text, width=50)
        self.input_entry.pack(pady=10)
        # Buttons
        self.run_button = tk.Button(root, text="Run", command=self.process_input)
        self.run_button.pack(pady=5)
        self.clear_button = tk.Button(root, text="Clear", command=self.clear_input)
        self.clear_button.pack(pady=5)
        # Output Display
        self.output_label = tk.Label(root, text="Output:", font=("Arial", 12, "bold"))
        self.output_label.pack(pady=10)
        self.output_text = tk.Text(root, height=10, width=50)
        self.output_text.pack(pady=5)
    def process_input(self):
        user_input = self.input_text.get().strip().lower()
        response = self.get_response(user_input)
        self.display_output(response)

    def get_response(self, command):
        return process_command(command)  # Call the actual function from core.py

    def display_output(self, text):
        self.output_text.delete("1.0", tk.END)  # Clear previous output
        self.output_text.insert(tk.END, text)   # Insert new output
    def clear_input(self):
        self.input_text.set("")  # Clear input field
        self.output_text.delete("1.0", tk.END)  # Clear output area
if __name__ == "__main__":
    root = tk.Tk()
    app = AssistantGUI(root)
    root.mainloop()