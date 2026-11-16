def NgramCompareLines(books):
    lines = TopListLines(books, "Top 5 two-word phrases in each book (count):", PhraseText("bigramCounts"))
    lines.append("")
    lines.extend(PhraseTableLines(books, "bigramCounts", "Selected book's two-word phrases in every book:"))
    lines.append("")
    lines.extend(TopListLines(books, "Top 5 three-word phrases in each book (count):", PhraseText("trigramCounts")))
    lines.append("")
    lines.extend(PhraseTableLines(books, "trigramCounts", "Selected book's three-word phrases in every book:"))
    lines.append("")
    lines.append("(Phrases starting or ending with a common word such as 'the' or 'of' are skipped;")
    lines.append(" a phrase must appear at least twice.)")
    return lines
