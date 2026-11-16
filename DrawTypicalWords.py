 def DrawTypicalWords(axis, books, number=8):
    # Words the selected book uses far more than the other books, per 10,000 words.
    
    main_total = CountedWords(books[0][1])
    others_total = sum(CountedWords(stats) for name, stats in books[1:])
    rows = DistinctiveWords(books, number)[::-1]          # reversed: best word ends up on top
    if not rows:
        axis.set_title("Words Typical of the Selected Book")
        axis.text(0.5, 0.5, "Not enough repeated words to compare",
                  ha="center", va="center", transform=axis.transAxes)
        axis.set_axis_off()
        return
    words = [word for score, word, in_main, in_others in rows]
    main_rate = [Ratio(in_main, main_total) * 10000 for s, w, in_main, in_others in rows]
    other_rate = [Ratio(in_others, others_total) * 10000 for s, w, in_main, in_others in rows]
    y = list(range(len(words)))
    axis.barh([v + 0.2 for v in y], main_rate, height=0.4, color=SELECTED_COLOR,
              label="Selected book")
    axis.barh([v - 0.2 for v in y], other_rate, height=0.4, color="lightgray",
              label="All other books")
    axis.set_yticks(y)
    axis.set_yticklabels(words)
    axis.set_title("Words Most Typical of the Selected Book")
    axis.set_xlabel("Uses per 10,000 words")
    axis.legend(fontsize=8, loc="lower right")
