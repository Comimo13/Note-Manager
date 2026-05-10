import json

from commands import create as c
from commands import delete as d
from commands import list_notes as l
from commands import search as s

from utils import helpers as h

def main():
    notes = []
    try:
        with open('D:/Projects/Notes Manager/storage/notes.json' , 'r') as json_file:
            notes = json.load(json_file)
    except FileNotFoundError:
        notes = []
    except json.decoder.JSONDecodeError:
        notes = []

    while True:
        action = input('PS C:\\WINDOWS\\System32> ')
        if action == "nm create":
            c.create(notes)
        elif action == "nm delete":
            d.delete(notes)
        elif action == "nm list-notes":
            l.list_notes()
        elif action == "nm search":
            s.search()
        elif action == "nm --help":
            h.helper()
        elif action == "nm exit":
            break
        else:
            print('CommandNotFoundException: This term is not recognized as a name of a cmdlet, function, script file, or operable program.')