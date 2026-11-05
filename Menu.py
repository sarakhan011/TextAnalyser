def menu(main_name, other_names):
    line = "=" * 56
    print(f"\n{line}")
    print("          TEXT ANALYSER - BOOK COMPARISON")
    print(line)
    if main_name:
        print(f" Selected book : {main_name}")
    else:
        print(" Selected book : (none - choose option 1)")
    if other_names:
        shown = ", ".join(other_names[:3])
        if len(other_names) > 3:
            shown += f" (+{len(other_names) - 3} more)"
        print(f" Compared with : {shown}")
    elif main_name:
        print(" Compared with : (none - choose option 2)")
    print("-" * 56)
    print(" 1. Load selected book")
    print(" 2. Choose other books to compare with")
    print(" 3. Compare basic statistics")
    print(" 4. Compare word frequency analysis")
    print(" 5. Compare sentence analysis")
    print(" 6. Compare character analysis")
    print(" 7. Compare readability scores (Flesch, LIX)")
    print(" 8. Compare common phrases (2 and 3 word n-grams)")
    print(" 9. Export comparison results")
    print("10. Exit")
    print(line)
