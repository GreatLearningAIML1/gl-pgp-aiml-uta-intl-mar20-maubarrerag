from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk
nltk.download('punkt')


text = "This is quiz about Natural Language Processing"

stop_words = ['is', 'about', 'this']           # Defined custom stopword's list.
words = word_tokenize(text)
new_words = []

for w in words:
    if w not in stop_words:
        new_words.append(w)
length = len(new_words)
print(length)
