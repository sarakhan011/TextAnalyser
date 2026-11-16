def PrintSection(title, lines):
    print(f"\n--- {title} ---")
    for line in lines:
        print(line)


def PrintBasicComparison(books):
    PrintSection(f"Basic Statistics: \"{books[0][0]}\" vs other books", BasicCompareLines(books))


def PrintWordComparison(books):
    PrintSection(f"Word Analysis: \"{books[0][0]}\" vs other books", WordCompareLines(books))


def PrintSentenceComparison(books):
    PrintSection(f"Sentence Analysis: \"{books[0][0]}\" vs other books", SentenceCompareLines(books))


def PrintCharacterComparison(books):
    PrintSection(f"Character Analysis: \"{books[0][0]}\" vs other books", CharacterCompareLines(books))


def PrintReadabilityComparison(books):
    PrintSection(f"Readability: \"{books[0][0]}\" vs other books", ReadabilityCompareLines(books))


def PrintNgramComparison(books):
    PrintSection(f"Common Phrases: \"{books[0][0]}\" vs other books", NgramCompareLines(books))


