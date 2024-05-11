msg = "www.my_site.com#about"
print(msg.replace("#", "/"))

word_list = ["run", "go", "lie"]
for word in word_list:
    "{word}ing"
word_list_ing = " ".join(f"{word}ing" for word in word_list)
print(word_list_ing)

stroka = "Ivanou Ivan"
spaceIndex = stroka.find(" ")
word1 = stroka[:spaceIndex + 1]
word2 = stroka[spaceIndex + 1:]
print(word2 + " " + word1)

s = " Hello World! "
s = s.strip()
print(s)

txt = "pARiS"
print(txt.capitalize())
