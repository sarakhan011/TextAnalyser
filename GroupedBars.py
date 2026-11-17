def GroupedBars(axis, categories, books, valueFor, title, xlabel, ylabel, fmt=None):
    # One group per category, one bar per book. valueFor(stats, category) -> number.
    colors = BookColors(len(books))
    width = 0.8 / len(books)
    for i, (name, stats) in enumerate(books):
        positions = [x + i * width for x in range(len(categories))]
        values = [valueFor(stats, category) for category in categories]
        bars = axis.bar(positions, values, width, color=colors[i])
        if fmt and len(books) <= 3:
            LabelBars(axis, bars, values, fmt)
    centre = (len(books) - 1) * width / 2
    axis.set_xticks([x + centre for x in range(len(categories))])
    axis.set_xticklabels(categories)
    axis.set_title(title)
    axis.set_xlabel(xlabel)
    axis.set_ylabel(ylabel)
