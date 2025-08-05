import json


with open("../bible_data/kjv_sample.json", "r") as file:
    bible = json.load(file)


query = input("What do you want to search for in the Bible? ").lower()


results = []
for verse in bible:
    if query in verse["text"].lower():
        results.append(verse)
        if len(results) == 3:
            break


if results:
    print("\nTop Bible verses found:\n")
    for verse in results:
        reference = f"{verse['book']} {verse['chapter']}:{verse['verse']}"
        print(f"{reference} — {verse['text']}\n")
else:
    print("Sorry, no verses found.")
