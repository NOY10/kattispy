num = int(input())
words = []
for i in range(num):
    word = input()
    words.append(word)
for i in range(num):
    if i%2 == 0:
        print(words[i])



