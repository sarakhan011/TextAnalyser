WORD_PATTERN = re.compile(r"[^\W_]+(?:['’][^\W_]+)*")
SENTENCE_END = re.compile(r'[.!?]+["\'”’)\]]*\s+')
ABBREVIATIONS = {"mr", "mrs", "ms", "dr", "st", "prof", "sr", "jr"}

# Words ignored at the START or END of a phrase (so "of the" does not win).

STOPWORDS = {
    "a", "an", "the", "and", "or", "but", "if", "of", "in", "on", "at", "to", "for",
    "from", "by", "with", "as", "is", "are", "was", "were", "be", "been", "it", "its",
    "he", "she", "they", "we", "you", "i", "him", "her", "his", "them", "their", "my",
    "me", "our", "your", "this", "that", "these", "those", "not", "no", "so", "than",
    "then", "had", "has", "have", "do", "did", "does", "would", "could", "will", "shall",
    "there", "which", "who", "what", "when", "up", "out", "into", "said",
}

LONG_WORD = 6   # LIX counts words with MORE than 6 letters as "long"

LABEL_WIDTH = 34
COLUMN_WIDTH = 18
