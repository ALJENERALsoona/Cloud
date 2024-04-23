from nltk.corpus import stopwords
from collections import Counter


def remove_stop_words_and_count(input_file):
  
  # Load stop words.
  stop_words = set(stopwords.words('english'))

  # Read text file content
  with open(input_file, 'r', encoding='utf-8') as file:
    content = file.read().lower() 

  # Split text into words and remove stop words
  words = []

  for word in content.split():
    if word not in stop_words:
      words.append(word)

  # Count word occurrences
  word_counts = Counter(words)

  # displaying word counts to console
  print("Word Counts:")
  for word, count in word_counts.items():
    print(f"{word} -> {count}")


input_file = r"C:/Users/HK/Desktop/random_paragraphs.txt"


remove_stop_words_and_count(input_file)

print("----------- DONE --------------")