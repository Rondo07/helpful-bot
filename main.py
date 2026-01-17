from datetime import datetime


'''
App saving notes

This is my notes, that I'm taking on my laptop
-Created on 13.01.2026 00:50 ❤️

[("This is my notes, that I'm taking on my laptop", "3.01.2026 00:50")]

1) Create vocab of notes
2) Write function that will print note
3) Write function that will print all notes
4) Write cycle which gets info from User

'''

note_list = []
note_file = "notes.txt"

welcome_banner = '''
▖▖  ▜         ▌   ▗ 
▙▌█▌▐ ▛▌█▌▛▘  ▛▌▛▌▜▘
▌▌▙▖▐▖▙▌▙▖▌   ▙▌▙▌▐▖
      ▌             
'''

commands = '''
1) exit - to exit the application
2) add_note - to add new note
3) print_note [i] - to print note number i
4) print_all - to print all notes
'''

def add_new_note(note_text) -> bool:
    note_creation_date = datetime.today()
    note_list.append({"text": note_text, "creation_date": note_creation_date})
    return True
def print_note(index: int):
    note = note_list[index]
    formatted_creation_date = note["creation_date"].strftime("%d.%m.%Y %H:%M")
    print(f'{note["text"]}\n- Created on {formatted_creation_date}\n')
    
def print_all_notes():
    for note_index in range(len(note_list)):
        print_note(note_index)
    text = input('Please enter note text: ')
    
def save_notes():
    with open(note_file, 'w') as file:
        for note in note_list:
            file.write(f'{note["text"]};{note["creation_date"]}\n')

def read_notes() -> list[dict]:
    with open(note_file) as file:
        for line in file:
            text, date = line.strip().split(';')
            creation_date = datetime.strptime(date, "%Y-%m-%d %H:%M:%S.%f")
            note_list.append({"text": text, "creation_date": creation_date})
    return note_list

def init():
    global note_list
    note_list = read_notes()
    print(welcome_banner)
    print("\nHello and welcome to our app\n")
    print(commands)
    
def main():
    while True:
        command, *args = input("Please enter command (enter exit to stop): ").strip().split(' ')
        if command == 'exit':
            print("GoodBye!")
            save_notes()
            break
        elif command == "add_note":
            text = input("Please enter note text: ")
            if add_new_note(text):
                print("\nNote added\n")
            else:
                print("\nError\n")
        elif command == "help":
            print(commands)        
        elif command == "print_note":
            index = int(args[0]) - 1
            if index < 0 or index > len(note_list):
                print("Please enter a valid note number: ")
                continue
            print(index)
            
init()
main()

    
# add_new_note(text)
# add_new_note(text)
# add_new_note(text)

# print_all_notes()
