def BuildBookList(main_name, other_names, cache):
    # List of (filename, stats) tuples. The selected book is always first.
    
    books = [(main_name, cache[main_name])]
    for name in other_names:
        books.append((name, cache[name]))
    return books



def Percent(part, total):
    return 100 * part / total if total else 0.0


def Ratio(part, total):
    return part / total if total else 0.0


def Avg(values):
    return sum(values) / len(values) if values else 0.0


def Short(name, limit):
    # Shorten a long name but keep its start AND end, so similar names stay different.
   
    if len(name) <= limit:
        return name
    keep = limit - 2
    head = (keep + 1) // 2
    return name[:head] + ".." + name[len(name) - (keep - head):]

