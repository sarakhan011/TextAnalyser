# Text Analyser – Book Comparison

A command-line tool that analyses plain-text books and compares a **selected book** against one or more **other books**. It prints side-by-side statistics in the terminal, draws comparison charts with matplotlib, and can export a full report to a text file.

## Features

- **Basic statistics** – lines, sentences, words, unique words, character counts, averages and lexical diversity
- **Word frequency analysis** – most common words, words used only once, vocabulary overlap with the selected book, and the words most typical of the selected book
- **Sentence analysis** – sentence length statistics, most common length, share of long sentences (over 25 words), and the longest sentence in each book
- **Character analysis** – letter, digit, space and punctuation shares; uppercase/lowercase split; top letters and punctuation marks
- **Readability scores** – Flesch Reading Ease, Flesch-Kincaid Grade Level and LIX, each with a plain-language difficulty label
- **Common phrases** – the most frequent 2-word and 3-word phrases (n-grams), with usage rates per 10,000 words in every book
- **Charts** – every comparison has a matching matplotlib figure; the selected book is always drawn in crimson, with a colour key underneath
- **Export** – write the entire comparison to a text file
- **Caching** – each book is analysed only once per session, then reused

## Requirements

- Python 3.8 or newer
- [matplotlib](https://matplotlib.org/)

```bash
pip install matplotlib
```

All other imports (`os`, `re`, `datetime`) are part of the Python standard library.

## Setup

1. Save the script (for example as `text_analyser.py`).
2. Put the `.txt` books you want to analyse **in the same folder** as the script. The program lists every `.txt` file in the current working directory.
3. Run it from that folder:

```bash
python text_analyser.py
```

## Usage

The program is menu-driven:

```
========================================================
          TEXT ANALYSER - BOOK COMPARISON
========================================================
 Selected book : (none - choose option 1)
--------------------------------------------------------
 1. Load selected book
 2. Choose other books to compare with
 3. Compare basic statistics
 4. Compare word frequency analysis
 5. Compare sentence analysis
 6. Compare character analysis
 7. Compare readability scores (Flesch, LIX)
 8. Compare common phrases (2 and 3 word n-grams)
 9. Export comparison results
10. Exit
========================================================
```

### Typical workflow

1. **Option 1** – Pick your selected book by number or filename. This is the book everything else is compared against.
2. **Option 2** – Pick the books to compare with. Enter numbers or filenames separated by commas (e.g. `1, 3`), or type `all`. Press Enter to cancel and keep your previous choice.
3. **Options 3–8** – View a comparison. Each prints a table in the terminal and then opens a chart window. Close the chart window to return to the menu.
4. **Option 9** – Export all six comparisons to a single report file.

Options 3–9 require a selected book **and** at least one comparison book. Choosing a new selected book automatically removes it from the comparison list if it was in there.

## Output

### Terminal and charts

Tables show one column per book, with the selected book marked by a `*`. Long filenames are shortened while keeping both their start and end, so similar names stay distinguishable.

| Option | Chart contents |
| --- | --- |
| 3 – Basic | Total words, unique words, average sentence length, lexical diversity |
| 4 – Words | Top-word heatmap, word length distribution, shared vocabulary %, typical-word comparison |
| 5 – Sentences | Sentence length distribution, average sentence length |
| 6 – Characters | Top letters per book, spaces/punctuation/digits/uppercase shares |
| 7 – Readability | Flesch, Flesch-Kincaid and LIX bar charts |
| 8 – Phrases | Heatmaps of the selected book's top 2-word and 3-word phrases |

### Exported report

Option 9 creates a `results/` folder (if needed) and writes:

```
results/<selected book filename>_comparison.txt
```

The report includes the selected book, the comparison books, the analysis date and time, and all six comparison sections. Exporting again for the same selected book overwrites the previous report.

## How the metrics work

**Words** – A word is a run of letters/digits, optionally with internal apostrophes (so `don't` is one word). Text is lowercased before counting. Note that the "Words" line in basic statistics uses a simple whitespace split, while unique words, word frequencies and readability use the stricter pattern above, so the two numbers can differ slightly.

**Sentences** – Split on `.`, `!` or `?` (plus any closing quotes or brackets) followed by whitespace. Common abbreviations (`Mr`, `Mrs`, `Ms`, `Dr`, `St`, `Prof`, `Sr`, `Jr`) are not treated as sentence ends. Sentences continue across line breaks; a blank line ends the current sentence.

**Readability**

| Score | Formula | Reading |
| --- | --- | --- |
| Flesch Reading Ease | `206.835 − 1.015 × (words/sentence) − 84.6 × (syllables/word)` | Higher is easier; 60–70 is plain English |
| Flesch-Kincaid Grade | `0.39 × (words/sentence) + 11.8 × (syllables/word) − 15.59` | Approximate US school grade |
| LIX | `(words/sentences) + (long words × 100 / words)` | Lower is easier; long words have more than 6 letters |

LIX labels: under 30 very easy, 30–40 easy, 40–50 medium, 50–60 difficult, 60+ very difficult.

**Phrases** – Bigrams and trigrams are counted across line breaks within a paragraph. Phrases that start or end with a common stopword (`the`, `of`, `and`, …) are ignored, and a phrase must appear at least twice to be listed.

**Vocabulary overlap** – For each comparison book: the number of shared unique words, what percentage of each book's vocabulary that represents, and a similarity score (shared words ÷ all distinct words across both books).

**Typical words** – Words appearing at least 5 times in the selected book, ranked by how much more often the selected book uses them than all the other books combined.

## Graphs
<img width="1390" height="993" alt="basic_statistics" src="https://github.com/user-attachments/assets/6f2c7e5e-f82b-4f00-9460-3045033bd302" />



## Limitations

- **Syllable counting is an English-only estimate** based on vowel groups, so Flesch and Flesch-Kincaid scores for other languages are not meaningful. LIX is more language-neutral.
- Stopword filtering for phrases uses an English list.
- Sentence detection is heuristic; unusual punctuation, poetry or heavily formatted text may be split imperfectly.
- Files are read as UTF-8 (a leading BOM is handled); undecodable bytes are replaced rather than raising an error.
- Charts require a display. On a headless machine, set a non-interactive matplotlib backend or use the export option instead.
- Only `.txt` files in the current folder are listed, though you can type a path to a file elsewhere when choosing the selected book.

## Tip for Project Gutenberg texts

Books downloaded from Project Gutenberg include a licence header and footer. For the most accurate results, delete those sections before analysing.
