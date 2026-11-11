def TopItems(counts, number):
    # Biggest counts first, as a list of (item, count) tuples.
    
    pairs = []
    for item, count in counts.items():
        pairs.append((item, count))
    pairs.sort(key=lambda pair: (-pair[1], str(pair[0])))
    return pairs[:number]


def TopWords(stats, number=10):
    return TopItems(stats["wordCounts"], number)


def WordsUsedOnce(stats):
    once = 0
    for count in stats["wordCounts"].values():
        if count == 1:
            once += 1
    return once


def SentenceLengthCounts(stats):
    counts = {}
    for length in stats["sentenceLengths"]:
        counts[length] = counts.get(length, 0) + 1
    return counts


def CharacterTypes(stats):
    return {
        "Letters": stats["letters"],
        "Digits": stats["digits"],
        "Spaces": stats["spaces"],
        "Punctuation": stats["punctuation"],
    }


def CountedWords(stats):
    return len(stats["wordLengths"])


def MostCommonSentenceLength(stats):
    top = TopItems(SentenceLengthCounts(stats), 1)
    return top[0][0] if top else 0


def LongSentencePercent(stats, limit=25):
    lengths = stats["sentenceLengths"]
    long_ones = 0
    for length in lengths:
        if length > limit:
            long_ones += 1
    return Percent(long_ones, len(lengths))


# Readability 

def AvgSentenceWords(stats):
    return Ratio(CountedWords(stats), len(stats["sentenceLengths"]))

