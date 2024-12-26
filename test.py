import os
import subprocess

# Configura la repo
FILENAME = "file.txt"    # File da modificare
TOTAL_COMMITS = 10000       # Numero di commit da fare

# Assicurati che il file esista
if not os.path.exists(FILENAME):
    with open(FILENAME, "w") as f:
        f.write("Contenuto iniziale\n")

# Modifica il file per il numero di commit richiesti
for i in range(1, TOTAL_COMMITS + 1):
    with open(FILENAME, "a") as f:
        f.write(f"Modifica numero {i}\n")

# Aggiungi e committa tutte le modifiche in un solo comando
subprocess.run(["git", "add", FILENAME])
subprocess.run(["git", "commit", "-m", f"{TOTAL_COMMITS} modifiche aggregate"])

# Push dei commit su GitHub
subprocess.run(["git", "push", "origin", "main"])
