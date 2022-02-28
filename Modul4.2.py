word = "domek"
drow = ""
for a in word:
    drow = a + drow
print(f"Is a word: {word} a palindrom?")
if word == drow:
    print("Yes")
else:
    print("No")