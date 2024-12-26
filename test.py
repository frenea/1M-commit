import os
import subprocess

# Configuration
FILENAME = "file.txt"    # File to modify
TOTAL_COMMITS = 10       # Number of commits to make

# Ensure the file exists
if not os.path.exists(FILENAME):
    with open(FILENAME, "w") as f:
        f.write("Initial content\n")

# Initialize the Git repository in the current directory
if not os.path.exists(".git"):
    subprocess.run(["git", "init"])

# Create or modify the file and commit it
for i in range(1, TOTAL_COMMITS + 1):
    # Append content to the file
    with open(FILENAME, "a") as f:
        f.write(f"Change number {i}\n")

    # Stage the file
    subprocess.run(["git", "add", FILENAME])

    # Commit the change
    subprocess.run(
        ["git", "commit", "-m", f"Commit number {i}"]
    )

print(f"{TOTAL_COMMITS} commits made in the current directory.")
