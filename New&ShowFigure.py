def NewFigure(rows, cols, title):
    figure, axes = plt.subplots(rows, cols, figsize=(7 * cols, 5 * rows))
    figure.suptitle(title, fontweight="bold", fontsize=14)
    return figure, axes


def ShowFigure(figure, books):
    # Colour key for every book under the charts, then display.
    
    names = PlotNames(books)
    colors = BookColors(len(books))
    handles = [Patch(facecolor=c, label=n) for c, n in zip(colors, names)]
    per_row = 4
    key_rows = (len(handles) + per_row - 1) // per_row
    bottom = 0.05 + 0.04 * key_rows
    figure.tight_layout(rect=[0, bottom, 1, 0.95])
    figure.legend(handles=handles, loc="lower center", ncol=min(len(handles), per_row),
                  frameon=False, fontsize=10)
    plt.show()
