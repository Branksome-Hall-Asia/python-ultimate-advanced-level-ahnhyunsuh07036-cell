# --- task_03_file_read.py ---
# EXAMPLE: Reading a whole file
# (Note: Make sure 'secrets.txt' exists in your folder!)
try:
    with open("secrets.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("Create a file called secrets.txt first!")

# CHALLENGE: Create a file called 'poem.txt' with 3 lines of text.
# Write code to open 'poem.txt' and print only the first 10 characters.
# Hint: f.read(10)
# ---------------------------------------------------------
