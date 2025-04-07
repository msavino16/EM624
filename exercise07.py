# Author: Michael Savino

#"I pledge my honor that i have abided by the Stevens Honor System"

# Exercise 07
# Text Analysis program

# This program analyzes text files about gig work pros and cons

# Importing the required libraries
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import nltk
from wordcloud import WordCloud
import matplotlib.pyplot as plt

pros_file = open('GigPros.txt', 'r', encoding='utf-8') #Used ChatGPT to figure out the encoding, since it wouldnt read the file otherwise
cons_file = open('GigsCons.txt', 'r', encoding='utf-8') #Used ChatGPT to figure out the encoding, since it wouldnt read the file otherwise
stopwords_file = open('stopwords_en.txt', 'r')

word_list_pros = []
word_list_cons = []

stopwords = [word.strip() for word in stopwords_file if word.strip()]
additional_stopwords = ['work','gig','workers','hours']
stopwords.extend(additional_stopwords)

#Clean the texts
pros_text = pros_file.read()
cleaned_pros = ""
for char in pros_text:
    if char.isalnum() or char.isspace():
        cleaned_pros += char.lower()
pros_words = cleaned_pros.split()
for word in pros_words:
    if word not in stopwords and len(word) >= 3 and word.strip():
        word_list_pros.append(word)

cons_text = cons_file.read()
cleaned_cons = ""
for char in cons_text:
    if char.isalnum() or char.isspace():
        cleaned_cons += char.lower()
cons_words = cleaned_cons.split()
for word in cons_words:
    if word not in stopwords and len(word) >= 3 and word.strip():
        word_list_cons.append(word)

pros_file.close()
cons_file.close()
stopwords_file.close()

#Using the library "vader", calculate the sentiment for the 2 texts
analyzer = SentimentIntensityAnalyzer()

clean_pros_str = ' '.join(word_list_pros)
clean_cons_str = ' '.join(word_list_cons)

pros_sentiment = analyzer.polarity_scores(clean_pros_str)
cons_sentiment = analyzer.polarity_scores(clean_cons_str)

print('\nThe following is the distribution of the sentiment for the Pros text:')
print('\n--- It is positive for', '{:.1%}'.format(pros_sentiment['pos']))
print('\n--- It is negative for', '{:.1%}'.format(pros_sentiment['neg']))
print('\n--- It is neutral for', '{:.1%}'.format(pros_sentiment['neu']), '\n')

print('\nThe following is the distribution of the sentiment for the Cons text:')
print('\n--- It is positive for', '{:.1%}'.format(cons_sentiment['pos']))
print('\n--- It is negative for', '{:.1%}'.format(cons_sentiment['neg']))
print('\n--- It is neutral for', '{:.1%}'.format(cons_sentiment['neu']), '\n')

#Extract bigrams
pros_bigrams = list(nltk.bigrams(word_list_pros))
cons_bigrams = list(nltk.bigrams(word_list_cons))

print('\n------the following are the bigrams extracted from the pros text:')
print(pros_bigrams)

print('\n------the following are the bigrams extracted from the cons text:')
print(cons_bigrams)

#Calculate the Lexical Diversity Ratio
pros_unique_words = len(set(word_list_pros))
pros_total_words = len(word_list_pros)
pros_diversity_ratio = pros_unique_words / pros_total_words

cons_unique_words = len(set(word_list_cons))
cons_total_words = len(word_list_cons)
cons_diversity_ratio = cons_unique_words / cons_total_words

print('\nLexical Diversity Ratios:')
print(f'Pros text: {pros_diversity_ratio:.3f} ({pros_unique_words} unique words out of {pros_total_words} total words)')
print(f'Cons text: {cons_diversity_ratio:.3f} ({cons_unique_words} unique words out of {cons_total_words} total words)')

#Create word clouds for the 2 texts
pros_wc = WordCloud(background_color='white', max_words=2000)
pros_wc.generate(clean_pros_str)
plt.imshow(pros_wc)
plt.axis('off')
plt.title('Pros Word Cloud')
plt.show()

cons_wc = WordCloud(background_color='white', max_words=2000)
cons_wc.generate(clean_cons_str)
plt.imshow(cons_wc)
plt.axis('off')
plt.title('Cons Word Cloud')
plt.show()

