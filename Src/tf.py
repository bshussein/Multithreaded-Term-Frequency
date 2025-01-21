import re, collections, os 
from concurrent.futures import ThreadPoolExecutor

def is_repeated_character(word):
    # Check if a word is composed of a single repeated character.
    return len(set(word)) == 1

def process_file(filepath):
    stopwords = set(open('stop_words').read().split(','))
    with open(filepath, 'r') as file:
        content = file.read().lower() # Read content in file all in lower case
    words = re.findall(r'\w{3,}', content) # Words with 3 or more characters
    # Count all words in file (except stop words and repeated character words)
    counts = collections.Counter(
        w for w in words if w not in stopwords and not is_repeated_character(w)
    )
    return counts 

def find_txt_files(directory='.'):
    # Get all files that end with ".txt" in the directory path
    return [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith('.txt')]

def main():
    text_files = find_txt_files()
    final_count = collections.Counter()

    with ThreadPoolExecutor(max_workers=4) as executor:
        results = list(executor.map(process_file, text_files))

    for result in results:
        final_count.update(result)

    print("---------- Word counts (top 40) -----------")
    for i, (w, c) in enumerate(final_count.most_common(40), 1):
        print(f"{i}. {w} - {c}")

if __name__ == '__main__':
    main()

    

  