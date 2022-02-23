def capitalisation(text):
    listText = text.split('.')
    output = ""
    i = 0
    while i < len(listText):
        currentString = listText[i]
        output += currentString.capitalize() + "."
        i += 1

    return output

print(capitalisation("hallo"))
print(capitalisation("hallo. testerdetest"))