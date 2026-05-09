import json
def list_notes():
    try:
        with open('D:/Projects/Notes Manager/storage/notes.json', 'r') as file:
            notes = json.load(file)
        for num , note in enumerate(notes):
            num = num + 1
            print(num ,'.', note)
    except FileNotFoundError:
        print("File not found.")
    except Exception:
        print("Something went wrong.")