BASIC_METRICS = [
    ("Lines", lambda s: s["lines"], "{:,}"),
    ("Sentences", lambda s: len(s["sentenceLengths"]), "{:,}"),
    ("Words", lambda s: s["words"], "{:,}"),
    ("Unique words", lambda s: len(s["uniqueWords"]), "{:,}"),
    ("Characters (with spaces)", lambda s: s["charsWspace"], "{:,}"),
    ("Characters (without spaces)", lambda s: s["charsWNspace"], "{:,}"),
    ("Average words per line", lambda s: Ratio(s["words"], s["lines"]), "{:.1f}"),
    ("Average word length (chars)", lambda s: Ratio(s["charsWNspace"], s["words"]), "{:.1f}"),
    ("Average words per sentence", lambda s: Avg(s["sentenceLengths"]), "{:.1f}"),
    ("Lexical diversity (unique/total)", lambda s: Percent(len(s["uniqueWords"]), CountedWords(s)), "{:.1f}%"),
]

WORD_METRICS = [
    ("Total words", CountedWords, "{:,}"),
    ("Unique words", lambda s: len(s["uniqueWords"]), "{:,}"),
    ("Words appearing only once", WordsUsedOnce, "{:,}"),
    ("Once-only share of vocabulary", lambda s: Percent(WordsUsedOnce(s), len(s["uniqueWords"])), "{:.1f}%"),
    ("Shortest word (chars)", lambda s: min(s["wordLengths"]) if s["wordLengths"] else 0, "{}"),
    ("Longest word (chars)", lambda s: max(s["wordLengths"]) if s["wordLengths"] else 0, "{}"),
    ("Average word length (chars)", lambda s: Avg(s["wordLengths"]), "{:.1f}"),
]

SENTENCE_METRICS = [
    ("Total sentences", lambda s: len(s["sentenceLengths"]), "{:,}"),
    ("Average words per sentence", lambda s: Avg(s["sentenceLengths"]), "{:.1f}"),
    ("Shortest sentence (words)", lambda s: min(s["sentenceLengths"]) if s["sentenceLengths"] else 0, "{}"),
    ("Longest sentence (words)", lambda s: max(s["sentenceLengths"]) if s["sentenceLengths"] else 0, "{}"),
    ("Most common sentence length", MostCommonSentenceLength, "{}"),
    ("Sentences over 25 words", LongSentencePercent, "{:.1f}%"),
]

CHARACTER_METRICS = [
    ("Letters (% of characters)", lambda s: Percent(s["letters"], s["charsWspace"]), "{:.1f}%"),
    ("Digits (% of characters)", lambda s: Percent(s["digits"], s["charsWspace"]), "{:.1f}%"),
    ("Spaces (% of characters)", lambda s: Percent(s["spaces"], s["charsWspace"]), "{:.1f}%"),
    ("Punctuation (% of characters)", lambda s: Percent(s["punctuation"], s["charsWspace"]), "{:.1f}%"),
    ("Uppercase (% of letters)", lambda s: Percent(s["uppercase"], s["letters"]), "{:.1f}%"),
    ("Lowercase (% of letters)", lambda s: Percent(s["lowercase"], s["letters"]), "{:.1f}%"),
]

READABILITY_METRICS = [
    ("Flesch Reading Ease (higher=easier)", FleschScore, "{:.1f}"),
    ("  Flesch reading level", lambda s: FleschLabel(FleschScore(s)) if CountedWords(s) else "n/a", "{}"),
    ("Flesch-Kincaid grade level", FleschKincaid, "{:.1f}"),
    ("LIX (lower=easier)", LixScore, "{:.1f}"),
    ("  LIX difficulty", lambda s: LixLabel(LixScore(s)) if CountedWords(s) else "n/a", "{}"),
    ("Long words (>6 letters) %", lambda s: Percent(s["longWords"], CountedWords(s)), "{:.1f}%"),
    ("Syllables per word", lambda s: Ratio(s["syllables"], CountedWords(s)), "{:.2f}"),
]
