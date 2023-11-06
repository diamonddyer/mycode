#!/usr/bin/env python3

import subprocess

# Ask for the user's comment
user_comment = input("Enter your comment: ")

# Run the Git commands
try:
    subprocess.run(['git', 'add', '*'], check=True)
    subprocess.run(['git', 'commit', '-m', user_comment], check=True)
    subprocess.run(['git', 'push', 'origin'], check=True)
    print("Git commands executed successfully.")
except subprocess.CalledProcessError as e:
    print(f"An error occurred while running Git commands: {e}")



