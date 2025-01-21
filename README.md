
# Multithreaded Term Frequency

## Overview
This program calculates the term frequency of words across multiple text files. It uses Python threading to process each file concurrently, demonstrating efficient file processing and multithreading.

## Features
1. Processes multiple text files in a directory.
2. Counts word frequencies concurrently using threads.
3. Outputs the top 40 most frequent words across all files.

## Usage

### Prerequisites
- Python 3.x
- Basic knowledge of how to run Python scripts from the terminal.

### Running the Program
1. Place your text files in a directory (e.g., `data/`).
2. Run the program by specifying the directory path as a command-line argument.

Example:
```bash
python tf.py data/
```

### Example Output
```plaintext
the: 500
and: 320
of: 275
...
```

## Project Structure
- `src/tf.py`: The main Python script for processing files and calculating word frequencies.
- `data/`: Contains sample text files for testing the program.

## How It Works
1. The program scans the specified directory for text files.
2. Each file is processed in a separate thread.
3. Word frequencies are aggregated and sorted to find the top 40 words.
