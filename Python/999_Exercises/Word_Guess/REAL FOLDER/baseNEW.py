import random
word_list = []
with open('allow_words.txt') as f:
    for line in f:
        l = line.strip()
        word_list.append(l)

a = 0
number = random.randrange(0,12972)
answer = word_list[number]
print(answer)

for i in range(0,6):
    guess = input("Guess a word!: ")
    if guess == answer:
        print("W, you win!!")
        a = 1
        break
    else:
        print("L, guess again!!")
        
if a == 0:
    print("You lose! The answer was "+answer)
f.close()

