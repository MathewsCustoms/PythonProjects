import random
import string
import json
import tkinter as tk
from tkinter import filedialog

# Generate a random substitution cipher key
def generate_key():
    letters = list(string.ascii_lowercase)
    shuffled = letters[:]
    random.shuffle(shuffled)
    return dict(zip(letters, shuffled))

# Save key to a file
def save_key(key, filename="key.json"):
    with open(filename, "w") as f:
        json.dump(key, f)

# Load key from a file
def load_key(filename="key.json"):
    with open(filename, "r") as f:
        return json.load(f)

# Encrypt text using the key
def encrypt_text(text, key):
    return "".join(key.get(c, c) for c in text.lower())  # Preserve non-alphabet characters

# Decrypt text using the key
def decrypt_text(text, key):
    reverse_key = {v: k for k, v in key.items()}
    return "".join(reverse_key.get(c, c) for c in text.lower())

# Open file selection dialog
def select_file():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(title="Select a text file", filetypes=[("Text files", "*.txt")])
    return file_path

# Encrypt a file
def encrypt_file():
    input_filename = select_file()
    if not input_filename:
        print("No file selected.")
        return
    
    key = generate_key()
    save_key(key, "key.json")
    
    with open(input_filename, "r") as f:
        text = f.read()

    encrypted_text = encrypt_text(text, key)
    
    output_filename = input_filename.replace(".txt", "_encrypted.txt")
    with open(output_filename, "w") as f:
        f.write(encrypted_text)
    
    print(f"File encrypted: {output_filename}")

# Decrypt a file
def decrypt_file():
    input_filename = select_file()
    if not input_filename:
        print("No file selected.")
        return
    
    key = load_key("key.json")
    
    with open(input_filename, "r") as f:
        text = f.read()

    decrypted_text = decrypt_text(text, key)
    
    output_filename = input_filename.replace("_encrypted.txt", "_decrypted.txt")
    with open(output_filename, "w") as f:
        f.write(decrypted_text)
    
    print(f"File decrypted: {output_filename}")

# Main menu
if __name__ == "__main__":
    while True:
        choice = input("Enter 'e' to encrypt, 'd' to decrypt, or 'q' to quit: ").strip().lower()
        if choice == "e":
            encrypt_file()
        elif choice == "d":
            decrypt_file()
        elif choice == "q":
            break
        else:
            print("Invalid choice. Try again.")
