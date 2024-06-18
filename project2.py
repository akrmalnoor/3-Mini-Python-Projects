with open ('story.txt','r') as f:
    story = f.read()

words = set()
start_of_word = -1

targat_start = '<'
targat_end = '>'

for i , char in enumerate(story):
    if char == targat_start:
        start_of_word = i 

    if char == targat_end and start_of_word != -1:
        word = story[start_of_word: i + 1]
        words.add(word)
        start_of_word = -1

answers = {}

for word in words: 
    answer = input('enter a word for ' + word + ': ')
    answers[word] = answer

for word in words:
    story = story.replace(word, answers[word])

print(story)