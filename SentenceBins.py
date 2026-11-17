def SentenceBins(stats, step=5, bins=10):
    # Share of sentences in length groups 0-4, 5-9 ... plus a last '50+' group.
    
    counts = [0] * (bins + 1)
    for length, count in SentenceLengthCounts(stats).items():
        counts[min(length // step, bins)] += count
    total = len(stats["sentenceLengths"])
    return [Percent(c, total) for c in counts]
