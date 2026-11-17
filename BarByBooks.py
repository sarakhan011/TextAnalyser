def BarByBook(axis, books, getter, title, ylabel, fmt="{:,.1f}", first=0):
    # One bar per book. Bars sit at fixed positions, so two books can never merge.
    values = [getter(stats) for name, stats in books[first:]]
    colors = BookColors(len(books))[first:]
    names = PlotNames(books)[first:]
    bars = axis.bar(range(len(values)), values, color=colors)
    LabelBars(axis, bars, values, fmt)
    SetBookTicks(axis, names)
    axis.set_title(title)
    axis.set_ylabel(ylabel)
