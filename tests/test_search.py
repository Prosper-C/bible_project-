import pytest
import json
from app import search


def load_sample_data():
    with open("bible_data/kjv_sample.json", "r", encoding="utf-8") as file:
        return json.load(file)

def test_search_verse_found():
    data = load_sample_data()
    results = search.search_verse(data, "God")
    assert len(results) == 2  # We expect 2 matches in sample data

def test_search_verse_not_found():
    data = load_sample_data()
    results = search.search_verse(data, "unicorn")
    assert len(results) == 0  # No matches for 'unicorn'
