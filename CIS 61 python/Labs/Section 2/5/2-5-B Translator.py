dictionary = ['Apple', 'Letter', 'Monster', 'Code', 'Mouse', 'Dictionary', 'Monkey', 'Pencil', 'Cat', 'Dog']

jdictionary = ['林檎', '文字', '怪獣', 'コード', '鼠', '辞書', '猿', '鉛筆', '猫', '犬']

user = str(input("Please Enter a word: "))

i = 0
k = 0
while i <= 10:
    if user == dictionary[i]:
        print("This word in Japanese is: " + jdictionary[i])
        break
    i += 1
