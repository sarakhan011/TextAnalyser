def BasicCompareLines(books):
    return TableLines(books, BASIC_METRICS)


def WordCompareLines(books):
    lines = TableLines(books, WORD_METRICS)
    lines.append("")
    lines.extend(TopListLines(books, "Top 5 most common words in each book:", TopWordText))
    lines.append("")
    lines.extend(OverlapLines(books))
    lines.append("")
    lines.extend(DistinctiveLines(books))
    return lines


def SentenceCompareLines(books):
    lines = TableLines(books, SENTENCE_METRICS)
    lines.append("")
    lines.append("Longest sentence in each book:")
    for i, (name, stats) in enumerate(books):
        longest = stats["longestSentence"]
        text = f"{longest[0]} words - {longest[1]}" if longest else "No sentences found."
        lines.append(f"  {BookLabel(i, name, 30)}: {text}")
    return lines


def CharacterCompareLines(books):
    lines = TableLines(books, CHARACTER_METRICS)
    lines.append("")
    lines.extend(TopListLines(books, "Top 5 letters in each book:", TopLetterText))
    lines.append("")
    lines.extend(TopListLines(books, "Top 5 punctuation marks in each book:", TopPunctuationText))
    return lines


def ReadabilityCompareLines(books):
    lines = TableLines(books, READABILITY_METRICS)
    lines.append("")
    lines.append("Flesch: 90+ very easy, 60-70 standard, 30-50 difficult, <30 very difficult.")
    lines.append("LIX: <30 very easy, 40-50 medium, 50-60 difficult, 60+ very difficult.")
    lines.append("(Syllable counting is an English-language estimate.)")
    return lines

