def BasicStats():
    return {
        "lines": 0,
        "words": 0,

        "charsWspace": 0,
        "charsWNspace": 0,

        "wordCounts": {},
        "uniqueWords": set(),
        "wordLengths": [],

        "sentenceLengths": [],
        "shortestSentence": None,
        "longestSentence": None,
        "pending": "",

        "letters": 0,
        "digits": 0,

        "spaces": 0,
        "punctuation": 0,

        "uppercase": 0,
        "lowercase": 0,

        "letterCounts": {},
        "punctuationCounts": {},

        "syllables": 0,
        "longWords": 0,
        "bigramCounts": {},
        "trigramCounts": {},
        "tail": [],
    }
