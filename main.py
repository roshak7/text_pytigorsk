import os
import matplotlib.pyplot as plt

start_path = os.getcwd()
local = start_path
localfile = os.path.join(start_path, 'text.txt')

words_counts = []
wordscounts = []
wordcounts = []
mestoimenia = ["я", "ты", "он", "она", "оно", "а", "будто", "если", "если бы", "зато", "зачем", "и", "как", "когда",
               "но", "почему", "потому что", "потому", "причем", "пусть", "так как", "также", "тоже", "только", "хотя",
               "чем", "чтоб", "чтобы",
               "без", "из-за", "из-под", 'между', 'на', 'над', 'перед', 'под', 'про', 'а', 'ба', 'всё', 'да-да', 'и',
               'их', 'м', 'но', 'ну', 'о', 'ок', 'оу', 'хм']

with open(localfile, 'r', encoding='utf8') as f:
    text = f.read()
    sentences = text.split('.')
    word_list = ['что', 'чтобы']
    count = 0
    for word in sentences:
        for char in word:
            if char.lower() in word_list:
                count += 1

    for sentence in sentences:
        words = sentence.split(' ')
        words_counts.append(sentence)
        wordcounts.append(len(words))
        average = len(wordcounts)
        average_wordcount = sum(wordcounts) / len(wordcounts)
        for i in words:
            wordscounts.append(len(i))
            average_wordscounts = len(wordscounts)
            count_wordscounts = sum(wordscounts) / len(wordscounts)

with open(localfile, encoding="utf8") as file:
    text = file.read()
    text = text.replace("\n", " ")
    text = text.replace(",", "").replace(".", "").replace("?", "").replace("!", "").replace(")", "").replace("(", "")
    text = text.lower()
    words = text.split()

# подготовка данных
nums = [i for i in wordcounts]
labels = [i for i in wordcounts]
# Нарисуйте круговую диаграмму с помощью Matplotlib
plt.pie(x=nums, labels=labels)

print("Длина предложений в тексте", wordcounts)
print("Максимальная длина предложения:", max(wordcounts))
print('Средняя длина строки:', round(average_wordcount, 1))
print("Средняя длина слова: ", round(count_wordscounts, 1))
print("Количество служебных слов в тексте", count)
plt.show()
