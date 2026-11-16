def RunComparison(choice, books):
    
    if choice == "3":
        PrintBasicComparison(books)
        PlotBasicComparison(books)
    elif choice == "4":
        PrintWordComparison(books)
        PlotWordComparison(books)
    elif choice == "5":
        PrintSentenceComparison(books)
        PlotSentenceComparison(books)
    elif choice == "6":
        PrintCharacterComparison(books)
        PlotCharacterComparison(books)
    elif choice == "7":
        PrintReadabilityComparison(books)
        PlotReadabilityComparison(books)
    elif choice == "8":
        PrintNgramComparison(books)
        PlotNgramComparison(books)
    elif choice == "9":
        path = ExportResults(books)
        print(f"Comparison exported to \"{path}\"")
