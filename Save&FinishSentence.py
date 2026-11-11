def SaveSentence(sentence, stats):
    length = len(CleanWords(sentence))
    if length == 0:
        return
    stats["sentenceLengths"].append(length)
    shortText = sentence if len(sentence) <= 100 else sentence[:100] + "..."
    if stats["shortestSentence"] is None or length < stats["shortestSentence"][0]:
        stats["shortestSentence"] = (length, shortText)
    if stats["longestSentence"] is None or length > stats["longestSentence"][0]:
        stats["longestSentence"] = (length, shortText)


def FinishSentence(stats):
    leftover = stats["pending"].strip()
    if leftover:
        SaveSentence(leftover, stats)
    stats["pending"] = ""
