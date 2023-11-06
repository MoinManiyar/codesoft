import tkinter as tk
import random
import string

# Function to generate a random password
def generate_password():
    password_length = int(length_entry.get())
    if password_length < 4:
        password_label.config(text="Password length must be at least 4")
        return

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_characters = "!@#$%^&*()_+-=[]{}|;:'\"<>,.?/~"
    
    characters = lowercase + uppercase + digits + special_characters
    password = ''.join(random.choice(characters) for _ in range(password_length))
    
    password_label.config(text="Generated Password: " + password)

# Create the main application window
app = tk.Tk()
app.title("Password Generator")

# Label and entry for password length
length_label = tk.Label(app, text="Password Length:")
length_label.pack()
length_entry = tk.Entry(app)
length_entry.pack()

# Button to generate password
generate_button = tk.Button(app, text="Generate Password", command=generate_password)
generate_button.pack()

# Label to display the generated password
password_label = tk.Label(app, text="")
password_label.pack()

# Start the application main loop
app.mainloop()
