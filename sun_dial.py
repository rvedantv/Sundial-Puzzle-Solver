word_file = "words.txt"
words = []

with open(word_file, 'r') as allwords:
    for word in allwords:
        word = word.strip().lower()
        words.append(word)


central_letter = input("Enter central letter: ").strip().lower()
side_letters = list(input("Enter rest of the letters: ").strip().lower())

allowed_letters = [central_letter]+side_letters

words2 = [] #central letter must be in word
for x in words:
    if (central_letter in x) and (all(letter in allowed_letters for letter in x)):
        words2.append(x)

invalid = []

for x in words2:
    lcopy = allowed_letters.copy()
    wcopy = list(x)
    l = len(lcopy)
    w = len(wcopy)
    for i in range(len(x)):
        lcopy = [a for a in lcopy if a!=x[i]] #allowed letters except letter x[i]
        wcopy = [b for b in wcopy if b!=x[i]] #letters in x except occurences of x[i]
        dl = l - len(lcopy) #number of x[i]'s allowed
        dw = w - len(wcopy) #number of x[i]'s in x
        if dw>dl:
            invalid.append(x) #limited letter usage
            break

valid_words = [x for x in words2 if x not in invalid]
valid_words = [x for x in valid_words if len(x)>3] #minimum length is 4
print(valid_words)