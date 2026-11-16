def DrawPhraseHeatmap(figure, axis, books, key, title, number=8):
    top = [gram for gram, count in TopPhrases(books[0][1], key, number)]
    if not top:
        axis.set_title(title)
        axis.text(0.5, 0.5, "No repeated phrases found", ha="center", va="center",
                  transform=axis.transAxes)
        axis.set_axis_off()
        return
    grid = [[Ratio(stats[key].get(gram, 0), CountedWords(stats)) * 10000
             for name, stats in books] for gram in top]
    image = axis.imshow(grid, cmap="YlOrRd", aspect="auto")
    figure.colorbar(image, ax=axis, fraction=0.04, pad=0.02, label="Uses per 10,000 words")
    highest = max(max(row) for row in grid)
    for r, row in enumerate(grid):
        for c, value in enumerate(row):
            dark = highest > 0 and value > highest * 0.6
            axis.text(c, r, f"{value:.1f}", ha="center", va="center", fontsize=8,
                      color="white" if dark else "black")
    axis.set_yticks(range(len(top)))
    axis.set_yticklabels([" ".join(g) for g in top])
    SetBookTicks(axis, PlotNames(books))
    axis.set_title(title)
