'''


UNDERSTAND
- Input: list of words (string), possible with repeated words
- Output: a dictionary where key = word, value = frequency
- Edge Cases: empty list --> empty dict

PLAN
- start with an empty dict
- loop through each word in the list
- if the word is already in the list, increment its count
- if not, add it to dict with count 1

IMPLEMENT
'''

def word_count(words: list[str]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts
