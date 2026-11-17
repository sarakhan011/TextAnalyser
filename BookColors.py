def BookColors(count):
    colors = [SELECTED_COLOR]
    for i in range(count - 1):
        colors.append(OTHER_COLORS[i % len(OTHER_COLORS)])
    return colors
