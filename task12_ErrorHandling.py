# --- task_12_error_handling.py ---
# EXAMPLE: Catching a zero division error
try:
    print(10 / 0)
except ZeroDivisionError:
    print("You cannot divide by zero!")

# CHALLENGE: Ask the user for their 'Age' using input().
# Wrap it in a try/except block. If the user types a word 
# instead of a number, print "Please enter a valid age."
# Hint: Use int(input()) to trigger a ValueError.
# ---------------------------------------------------------
