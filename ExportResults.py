def ExportResults(books):
    # Write the whole comparison to results/<selected book>_comparison.txt.
    
    os.makedirs("results", exist_ok=True)
    path = os.path.join("results", books[0][0] + "_comparison.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(BuildReport(books)) + "\n")
    return path
