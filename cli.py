from alliance_data_editor import AllianceDataEditor

import os


data_path = "data/test.json"
alliance_data_editor = AllianceDataEditor(data_path)
alliance_data_editor.load_data()

def main():
    while True:
        print("\nAlliance Chat Visualizer")
        print("1. Add Alliance Chat")
        print("2. Remove Alliance Chat")
        print("3. List Alliance Chats")
        print("4. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_alliance()
        elif choice == "2":
            remove_alliance()
        elif choice == "3":
            list_alliances()
        elif choice == "4":
            break
            

def clear_console():
    os.system("cls" if os.name == "nt" else "clear")
    
def add_alliance():
    name = input("Alliance Chat Name: ").strip()
    round = input("Round Created: ").strip()
    players = input("Players (seperated by ,): ").split(",")
    if (name == None or round == None or players == None):
        print("Fields can't be null")
        return
    alliance_data_editor.create_alliance_chat(name, round, players)

def remove_alliance():
    name = input("Alliance Chat Name: ").strip()
    if name == None:
        print("Fields can't be null")
        return
    if input("Are you sure you want to delete? (y/n)").lower().strip() == "y":
        alliance_data_editor.remove_alliance_chat(name)
        
def list_alliances():
    print()
    alliance_data_editor.list_alliance_chats()
    
if __name__ == "__main__":
    main()
