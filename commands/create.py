import json
def create(notes):
    try:
        note = input(' ')
        notes.append(note)
        with open('D:/Projects/Notes Manager/storage/notes.json' , 'w') as f:
            json.dump(notes, f)
    except ValueError:
        print("Please enter a vaild note")
    except Exception:
        print("something went wrong")

