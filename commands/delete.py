import json
def delete(notes):
    try:
        note = input('PS C:\\WINDOWS\\System32> ')
        notes.remove(note)
        with open('D:/Projects/Notes Manager/storage/notes.json', 'w') as file:
            json.dump(notes, file)
    except ValueError:
        print("Please enter a valid note.")
    except Exception:
        print("something went wrong.")
