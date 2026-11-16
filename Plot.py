def PlotBasicComparison(books):
    figure, axes = NewFigure(2, 2, f"Basic Statistics: {books[0][0]} vs other books")
    BarByBook(axes[0][0], books, lambda s: s["words"], "Total Words", "Words", "{:,.0f}")
    BarByBook(axes[0][1], books, lambda s: len(s["uniqueWords"]), "Unique Words", "Words", "{:,.0f}")
    BarByBook(axes[1][0], books, lambda s: Avg(s["sentenceLengths"]),
              "Average Words per Sentence", "Words", "{:.1f}")
    BarByBook(axes[1][1], books,
              lambda s: Percent(len(s["uniqueWords"]), CountedWords(s)),
              "Lexical Diversity (unique / total words)", "Percent (%)", "{:.1f}%")
    ShowFigure(figure, books)

def PlotWordComparison(books):
    figure, axes = NewFigure(2, 2, f"Word Analysis: {books[0][0]} vs other books")

    DrawWordHeatmap(figure, axes[0][0], books)
    DrawWordLengths(axes[0][1], books)

    BarByBook(axes[1][0], books, lambda s: Percent(len(s["uniqueWords"] & books[0][1]["uniqueWords"]),
                                                   len(books[0][1]["uniqueWords"])),
              "% of Selected Book's Vocabulary Found in Each Book", "Shared vocabulary (%)",
              "{:.1f}%", first=1)

    DrawTypicalWords(axes[1][1], books)
    ShowFigure(figure, books)

def PlotSentenceComparison(books):
    step, bins = 5, 10
    labels = [f"{i * step}-{i * step + step - 1}" for i in range(bins)] + [f"{bins * step}+"]
    colors = BookColors(len(books))

    figure, (lines, bars) = NewFigure(1, 2, f"Sentence Analysis: {books[0][0]} vs other books")
    for i, (name, stats) in enumerate(books):
        lines.plot(range(len(labels)), SentenceBins(stats, step, bins), marker="o",
                   color=colors[i], linewidth=3 if i == 0 else 1.6)
    lines.set_xticks(range(len(labels)))
    lines.set_xticklabels(labels, rotation=45, ha="right")
    lines.set_title("Sentence Length Distribution")
    lines.set_xlabel("Sentence length (words)")
    lines.set_ylabel("Share of sentences (%)")

    BarByBook(bars, books, lambda s: Avg(s["sentenceLengths"]),
              "Average Sentence Length", "Words per sentence", "{:.1f}")
    ShowFigure(figure, books)

def PlotCharacterComparison(books):
    main_stats = books[0][1]
    top = [letter for letter, count in TopItems(main_stats["letterCounts"], 8)]
    figure, (letters, others) = NewFigure(1, 2, f"Character Analysis: {books[0][0]} vs other books")

    GroupedBars(letters, top, books,
                lambda s, l: Percent(s["letterCounts"].get(l, 0), s["letters"]),
                "Selected Book's Top Letters in Every Book",
                "Letters", "Share of all letters (%)")

    # Letters are left out here: they are ~75% in every book and hide the differences.
    kinds = {
        "Spaces\n(% of chars)": lambda s: Percent(s["spaces"], s["charsWspace"]),
        "Punctuation\n(% of chars)": lambda s: Percent(s["punctuation"], s["charsWspace"]),
        "Digits\n(% of chars)": lambda s: Percent(s["digits"], s["charsWspace"]),
        "Uppercase\n(% of letters)": lambda s: Percent(s["uppercase"], s["letters"]),
    }
    GroupedBars(others, list(kinds), books, lambda s, k: kinds[k](s),
                "Spaces, Punctuation, Digits and Uppercase",
                "", "Share (%)", "{:.1f}")
    ShowFigure(figure, books)

def PlotReadabilityComparison(books):
    figure, axes = NewFigure(1, 3, f"Readability: {books[0][0]} vs other books")
    BarByBook(axes[0], books, FleschScore, "Flesch Reading Ease\n(higher = easier)", "Score", "{:.1f}")
    BarByBook(axes[1], books, FleschKincaid, "Flesch-Kincaid Grade Level", "School grade", "{:.1f}")
    BarByBook(axes[2], books, LixScore, "LIX Score\n(lower = easier)", "Score", "{:.1f}")
    ShowFigure(figure, books)


def PlotNgramComparison(books):
    figure, axes = NewFigure(1, 2, f"Common Phrases: {books[0][0]} vs other books")
    DrawPhraseHeatmap(figure, axes[0], books, "bigramCounts", "Selected Book's Top Two-Word Phrases")
    DrawPhraseHeatmap(figure, axes[1], books, "trigramCounts", "Selected Book's Top Three-Word Phrases")
    ShowFigure(figure, books)
