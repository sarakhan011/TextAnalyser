def CleanWords(text):
    return re.findall(WORD_PATTERN, text.lower())


def CountSyllables(word):
    # Rough English syllable count (groups of vowels, minus a silent final 'e').
   
    word = word.lower()
    count = len(re.findall(r"[aeiouy]+", word))
    if count > 1 and word.endswith("e") and not word.endswith(("le", "ee")):
        count -= 1
    return max(count, 1)


def CountWords(text, stats):
    for word in CleanWords(text):
        stats["wordCounts"][word] = stats["wordCounts"].get(word, 0) + 1
        stats["uniqueWords"].add(word)
        stats["wordLengths"].append(len(word))
        stats["syllables"] += CountSyllables(word)
        if len(word) > LONG_WORD:
            stats["longWords"] += 1
