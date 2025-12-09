import subprocess

print("FFUF - Fuzzing file con estensioni .php .html .js .bak\n")

url = input("URL (inserisci l'url)\n> ").strip()
wordlist = input("\ninserisci la Wordlist\n> ").strip()
threads = "100"

print("\nFuzzando...")
comando = [
    "ffuf",
    "-u", url,
    "-w", wordlist,
    "-t", threads,
    "-e", ".php,.html,.js,.bak",
    "-ac",
    "-c",
    "-v"
]

subprocess.run(comando)
