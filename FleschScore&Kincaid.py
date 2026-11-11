def FleschScore(stats):
    # Flesch Reading Ease: higher = easier (60-70 is plain English).
    
    words = CountedWords(stats)
    if words == 0 or not stats["sentenceLengths"]:
        return 0.0
    return (206.835 - 1.015 * AvgSentenceWords(stats)
            - 84.6 * Ratio(stats["syllables"], words))


def FleschKincaid(stats):
    # Flesch-Kincaid Grade Level: roughly the US school grade needed.

    # The formula is:
    #      206.835 - 1.015 (words / sentence)
    #      -84.6 (Syllables / words)
    
    words = CountedWords(stats)
    if words == 0 or not stats["sentenceLengths"]:
        return 0.0
    return (0.39 * AvgSentenceWords(stats)
            + 11.8 * Ratio(stats["syllables"], words) - 15.59)
