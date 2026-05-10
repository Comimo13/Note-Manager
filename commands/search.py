import json
def search():
    try:
        with open('D:/Projects/Notes Manager/storage/notes.json' , 'r') as f:
            notes = json.load(f)
        note = input('PS C:\\WINDOWS\\System32> ')
        if note in notes:
            print(note)
        if note not in notes:
            print('This note does not exist')
    except Exception:
        print('Something went wrong')