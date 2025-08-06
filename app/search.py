import json

def load_bible_data(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        return json.load(file)

def search_verse(data, keyword):
    results = []
    for verse in data:
        if keyword.lower() in verse["text"].lower():
            results.append(verse)
    return results

def main():
    bible_data = load_bible_data("bible_data/kjv_sample.json")
    keyword = input("Enter a word to search in the Bible: ")
    matches = search_verse(bible_data, keyword)

    if matches:
        print(f"\nFound {len(matches)} result(s):\n")
        for verse in matches:
            print(f"{verse['book']} {verse['chapter']}:{verse['verse']} - {verse['text']}")
    else:
        print("No results found.")

if __name__ == "__main__":
    main()

