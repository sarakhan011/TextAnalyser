def LoadFile(filename):
    stats = BasicStats()
    # utf-8-sig reads English letters, many other languages, symbols and emojis
    with open(filename, "r", encoding="utf-8-sig", errors="replace") as f:
        for line in f:
            TextAnalyse(line, stats)
    FinishSentence(stats)
    return stats


def LoadCached(filename, cache):
    # Analyse a file only once; later requests reuse the stored result.
  
    if filename not in cache:
        print(f"  Analysing \"{filename}\" ...")
        cache[filename] = LoadFile(filename)
    return cache[filename]
