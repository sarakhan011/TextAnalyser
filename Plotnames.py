def PlotNames(books):
    # Readable and always different labels for the charts (selected book has a star).
    labels = []
    for i, (name, stats) in enumerate(books):
        base = name[:-4] if name.lower().endswith(".txt") else name
        if len(base) > 22:                       # keep the start AND the end of long names
            base = base[:10] + ".." + base[-10:]
        labels.append(("* " if i == 0 else "") + base)
    for i, label in enumerate(labels):
        if labels.count(label) > 1:
            labels[i] = f"{label} ({i + 1})"
    return labels
