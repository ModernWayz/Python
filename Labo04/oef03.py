stopped = False
words = []

while stopped == False:
    word = input("geef een woord: ")
    if word == "":
        stopped = True
        break
    if word not in words:
        words.append(word)

if stopped == True:
    for i in words:
        print(i)