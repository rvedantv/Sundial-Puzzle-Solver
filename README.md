# Sundial Solver

A simple Python program that filters valid words from a dictionary file based on puzzle rules.  
It is inspired by *The Sun* UK's **Sundial** puzzle, where you must form words using a set of letters with one **mandatory central letter**. Repetition of letters beyond what is given is not allowed. 

---

## Features
- Ensures every word contains the **central letter**.
- Only allows use of **central + side letters**.
- Checks that no letter is used more times than it appears in the allowed set.
- Filters out words shorter than 4 letters.

---

## How It Works
1. The program loads a word list from `words.txt`.
2. You provide:
   - **Central letter** (must appear in every word).
   - **Side letters** (additional letters allowed).
3. The script outputs all valid words.

---

## Example

### Input

```
Enter central letter: a
Enter rest of the letters: bcdef
```

### Output

```
['abed', 'aced', 'bade', 'bead', 'cade', 'cafe', 'dace', 'deaf', 'decaf', 'ecad', 'face', 'faced', 'fade']
```
