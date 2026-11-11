def LixScore(stats):
    # LIX = words per sentence + percentage of long words (over 6 letters).

    # LIX = (words/ sentences) + (long words x 100 / words)

    
    words = CountedWords(stats)
    if words == 0 or not stats["sentenceLengths"]:
        return 0.0
    return AvgSentenceWords(stats) + Percent(stats["longWords"], words)

def LixLabel(score):
  
    # A LIX Label is the text description assigned to a LIX Score. 
    # It tells the user the reading difficulty in simple words.

     #  Example :  LIX Score (Below 25)     LIX Label(Very Easy)
	
    for limit, label in ((30, "Very easy"), (40, "Easy"), (50, "Medium"), (60, "Difficult")):
        if score < limit:
            return label
    return "Very difficult"
