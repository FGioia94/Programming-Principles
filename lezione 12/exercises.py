"""
Scrivi un programma che chiede all'utente 
il nome di un social network che utilizza abitualmente 
e la relativa password di accesso

Il programma a questo punto, apre un file
e scrive al suo interno una riga contenete social e password,
magari separati da un = o un altro carattere a piacere

Attenzione: ogni volta che il programma viene riavviato,
ed i nuovi social e password vengono inseriti, 
la nuova riga che li conterrà deve essere aggiunta al file"""
import os
class NotASocialError(ValueError):
    def __init__(self):
        super().__init__("The text that you input is not a social network")
def ask_social():
    try:
        socials = ["Facebook", "Instagram", "TikTok", "Discord", "Threads", "X"]
        social = input("Write your favorite social network\n").title()
        if not social in socials:
            raise NotASocialError
    
        
    except NotASocialError:
        ask_social()
    else:
        return social
def ask_password():
    try:
        pwd = input("Type your password\n")
        if not pwd:
            raise(ValueError("Password can't be empty, try again"))
    except ValueError:
        ask_password()
    else:
        return pwd
    
def write(path, data):
    with open(path, "w", encoding="utf-8") as file:
        file.write(data)

def read(path):
    with open(path, "r", encoding="utf-8") as file:
        data = file.read()
    return data

def serialize(path, social, pwd):
    new_line = f"{social} = {pwd}\n"
    if os.path.exists(path):
        data = read(path)
        data += new_line
    else:
        data = new_line
    write(path, data)

def main():
    social = ask_social()
    pwd = ask_password()
    serialize("data.txt", social, pwd)
main()