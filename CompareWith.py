def ChooseOthers(main_name):
    # Let the user pick which other books the selected book is compared with.
   
    candidates = []
    for name in TextFiles():
        if os.path.abspath(name) != os.path.abspath(main_name):
            candidates.append(name)

    if not candidates:
        print("No other .txt files found in this folder.")
        return []

    print(f"\n Books available to compare with \"{main_name}\" (press Enter to cancel):")
    for i, name in enumerate(candidates, 1):
        print(f" {i}. {name}")
    answer = input("Enter numbers/filenames separated by commas, or 'all': ").strip()

    if not answer:
        return []
    if answer.lower() == "all":
        return candidates

    chosen = []
    for token in answer.split(","):
        token = token.strip()
        if not token:
            continue
        if token.isdigit() and 1 <= int(token) <= len(candidates):
            name = candidates[int(token) - 1]
        elif token in candidates:
            name = token
        else:
            print(f"Skipping \"{token}\" (not in the list).")
            continue
        if name not in chosen:
            chosen.append(name)
    if not chosen:
        print("No valid books chosen. Your previous choice is unchanged.")
    return chosen
