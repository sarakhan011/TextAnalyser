def ChooseFile():
    files = TextFiles()
    if not files:
        print("\nNo .txt files found in this folder.")
        return None
    print("\n File Selection (press Enter to cancel)")
    for i, name in enumerate(files, 1):
        print(f" {i}. {name}")
    choice = input("Enter filename or number: ").strip()
    if not choice:
        return None
    if choice.isdigit() and 1 <= int(choice) <= len(files):
        return files[int(choice) - 1]
    if os.path.isfile(choice):
        return choice
    print("File not found.")
    return None
