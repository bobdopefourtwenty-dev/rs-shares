import tkinter as tk
import subprocess
import os
import sys
import atexit

# Define the name for the temporary script that will be created.
TEMP_SCRIPT_NAME = "temp_console_writer.py"

def create_and_run_console_script():
    """
    Creates a temporary Python script to produce the console effect and runs it
    in a new console window.
    """
    
    # --- Python code for the new console window ---
    # This code is written as a multi-line string. It will be saved as a .py file.
    console_script_code = """
import os
import sys
import time

# Set the console title and color (0=black background, 2=green text).
os.system('title ChuckBot Console')
os.system('color 02')
os.system('cls') # Clear the console screen.

text_to_type = "chuckbotallwayswins"
typing_delay = 0.1  # Seconds to wait between each character.

# Loop through each character in the string and print it one by one.
for char in text_to_type:
    sys.stdout.write(char)  # Write one character without a newline.
    sys.stdout.flush()      # Immediately display the character.
    time.sleep(typing_delay) # Wait before typing the next character.

# After typing, wait for the user to press Enter to close the window.
input()
"""

    # --- Writing and Executing the Script ---
    try:
        # Write the string content to the temporary .py file.
        with open(TEMP_SCRIPT_NAME, "w") as f:
            f.write(console_script_code)
        
        # Use subprocess.Popen to run the script in a new console window.
        # The 'creationflags' argument is specific to Windows to ensure a new
        # window is created, separate from the main application.
        # For macOS/Linux, you might need a different command, e.g., involving 'xterm' or 'gnome-terminal'.
        if sys.platform == "win32":
            subprocess.Popen(
                [sys.executable, TEMP_SCRIPT_NAME],
                creationflags=subprocess.CREATE_NEW_CONSOLE
            )
        else:
            # A basic fallback for macOS/Linux (may require specific terminals to be installed).
            # This is a simplified example.
            print("This script is best run on Windows for the intended console effect.")
            print("Attempting to run in a new terminal...")
            try:
                # Try to open in a new terminal, though behavior can vary.
                subprocess.Popen(['xterm', '-e', f'python3 {TEMP_SCRIPT_NAME}'])
            except FileNotFoundError:
                print("xterm not found. Please run the temp script manually.")


    except Exception as e:
        print(f"An error occurred: {e}")

def cleanup():
    """
    Deletes the temporary script file when the application exits.
    """
    if os.path.exists(TEMP_SCRIPT_NAME):
        os.remove(TEMP_SCRIPT_NAME)
        print(f"Cleaned up {TEMP_SCRIPT_NAME}.")

# Register the cleanup function to run when the program exits.
atexit.register(cleanup)

# --- Main Tkinter Application Setup ---
# Create the main window.
root = tk.Tk()
root.title("Console Launcher")
root.geometry("300x150") # Set window size.
root.configure(bg='#2e2e2e') # Set a dark background color.

# Create a frame to hold the widgets and center them.
main_frame = tk.Frame(root, bg=root.cget('bg'))
main_frame.pack(expand=True)

# Create a button widget.
# When clicked, it will call the 'create_and_run_console_script' function.
launch_button = tk.Button(
    main_frame,
    text="Open Console",
    font=("Helvetica", 12),
    bg="#4a4a4a",
    fg="white",
    activebackground="#5a5a5a",
    activeforeground="white",
    padx=20,
    pady=10,
    relief="flat",
    command=create_and_run_console_script
)
launch_button.pack(pady=20)

# Start the Tkinter event loop. This keeps the window open and responsive.
root.mainloop()

