# DNA

## Background

DNA, the carrier of genetic information, has been a cornerstone in forensic science for decades. This project demonstrates how DNA profiling works by identifying to whom a given DNA sequence belongs using Short Tandem Repeats (STRs).

STRs are short sequences of DNA bases that repeat consecutively at specific locations in a genome. The number of repeats varies among individuals, providing a unique identifier when analyzed. By using multiple STRs, the likelihood of accurately identifying a match increases significantly.

## Features

- Parses a CSV database containing individuals' STR counts.
- Reads a DNA sequence from a text file.
- Computes the longest run of consecutive STR repeats in the DNA sequence.
- Matches the STR counts against a database to identify the individual or determine if no match exists.

## Usage

Run the program as follows:

```bash
python3 dna.py <database.csv> <sequence.txt>
```

Examples:
```bash
$ python3 dna.py databases/small.csv sequences/1.txt
Bob

$ python3 dna.py databases/small.csv sequences/2.txt
No match

$ python3 dna.py databases/large.csv sequences/5.txt
Lavender
```

### Error Handling

If the incorrect number of arguments is provided, the program will display an error message:
```bash
$ python dna.py
Usage: python dna.py <database.csv> <sequence.txt>
```

## Project Structure

```
|── dna/
│   ├── databases/
│   │   ├── small.csv
│   │   └── large.csv
│   ├── dna.py
│   └── sequences/
│       ├── 1.txt
│       ├── 2.txt
│       ├── ...
│       └── 20.txt
└── README.md
```

## Implementation Details

1. **Input**:
   - A CSV file containing individuals' STR counts.
   - A text file containing a DNA sequence.

2. **Output**:
   - The name of the individual whose STR counts match the DNA sequence.
   - "No match" if no individual matches the DNA sequence.

3. **Steps**:
   - Parse the CSV file to extract STRs and their counts.
   - Analyze the DNA sequence to calculate the longest consecutive repeats for each STR.
   - Compare the computed STR counts against the database.
   - Print the matching individual's name or "No match."

## Example Data

### Database (CSV)
```csv
name,AGAT,AATG,TATC
Alice,28,42,14
Bob,17,22,19
Charlie,36,18,25
```

### DNA Sequence (Text)
```
AAGATAGATAGATAGATAATGTATC
```

### Sample Output
```bash
$ python dna.py databases/small.csv sequences/4.txt
Alice
```

## Development Notes

- The program leverages Python's `csv` module for handling CSV files and efficient data processing.
- String slicing is used to identify and count STR sequences within the DNA string.
- A dictionary is used to store STR counts for easy comparison with the database.

## Requirements

- Python 3.x

## Authors

Developed by [Shahir Ahmed](https://github.com/Shahir-47/).

## License

This project is licensed under the [MIT License](LICENSE).
