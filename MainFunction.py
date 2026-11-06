import os
import sys
import importlib

MODULE_NAME = "TextAnalyserCode"          

sys.path.insert(0, os.getcwd())           
module = importlib.import_module(MODULE_NAME)
importlib.reload(module)                 
globals().update({name: value for name, value in vars(module).items()
                  if not name.startswith("_")})   

def main():
    print("Welcome to the Text Analyser - Book Comparison!")
    cache = {}              
    main_name = None       
    other_names = []       

    def select_others():
        
        chosen = ChooseOthers(main_name)
        if not chosen:
            return other_names                 
        try:
            for name in chosen:
                LoadCached(name, cache)
        except OSError as error:
            print(f"Could not read a file: {error}")
            return other_names
        print(f"Comparing \"{main_name}\" with {len(chosen)} other book(s).")
        return chosen

    while True:
        menu(main_name, other_names)
        choice = input("Enter your choice (1-10): ").strip()

        if choice == "1":
            name = ChooseFile()
            if name:
                try:
                    LoadCached(name, cache)
                except OSError as error:
                    print(f"Could not read \"{name}\": {error}")
                    continue
                main_name = name
                # the selected book must never be compared with itself
                other_names = [n for n in other_names
                               if os.path.abspath(n) != os.path.abspath(main_name)]
                print(f"Loaded \"{main_name}\" ({cache[main_name]['lines']:,} lines).")
                if not other_names:
                    other_names = select_others()

        elif choice == "2":
            if not main_name:
                print("Please load the selected book first (option 1).")
            else:
                other_names = select_others()

        elif choice in {"3", "4", "5", "6", "7", "8", "9"}:
            if not main_name:
                print("Please load the selected book first (option 1).")
            elif not other_names:
                print("Please choose other books to compare with first (option 2).")
            else:
                RunComparison(choice, BuildBookList(main_name, other_names, cache))

        elif choice == "10":
            print("Thank you for using Text Analyser!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 10.")
main()
