def BuildReport(books):
    line = "=" * 60
    report = [line, "BOOK COMPARISON RESULTS", line,
              f"Selected book: {books[0][0]}",
              "Compared with: " + ", ".join(name for name, stats in books[1:]),
              f"Analysis date: {datetime.now():%Y-%m-%d %H:%M:%S}", ""]
    sections = [
        ("BASIC STATISTICS COMPARISON", BasicCompareLines(books)),
        ("WORD ANALYSIS COMPARISON", WordCompareLines(books)),
        ("SENTENCE ANALYSIS COMPARISON", SentenceCompareLines(books)),
        ("CHARACTER ANALYSIS COMPARISON", CharacterCompareLines(books)),
        ("READABILITY COMPARISON", ReadabilityCompareLines(books)),
        ("COMMON PHRASES (N-GRAM) COMPARISON", NgramCompareLines(books)),
    ]
    for title, lines in sections:
        report.append(title)
        report.append("-" * 30)
        report.extend(lines)
        report.append("")
    report.extend([line, "End of Comparison Report", line])
    return report
