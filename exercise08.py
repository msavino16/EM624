# Author: Michael Savino

#"I pledge my honor that i have abided by the Stevens Honor System"

# Exercise 08
# Article Analysis program

# This program analyzes recent news articles about AI's impact on the job market

#Import required libraries
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import nltk
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import newspaper
import pandas as pd

#Define the target URLs
url1 = 'https://www.ironhack.com/us/blog/the-impact-of-ai-on-the-tech-job-market'
url2 = 'https://eastside-online.org/showcase/how-does-ai-impact-computer-science-careers/'


#Place the text into a list of words (or a pandas).
paper1 = newspaper.build(url1, memoize_articles=False, language='en', fetch_images=False, number_threads=2)
article1 = paper1.articles[0]
article1.download()
article1.parse()
article1_words = article1.text.split()

paper2 = newspaper.build(url2, memoize_articles=False, language='en', fetch_images=False, number_threads=2)
article2 = paper2.articles[0]
article2.download()
article2.parse()
article2_words = article2.text.split()

df1 = pd.DataFrame({'words': article1_words})
df2 = pd.DataFrame({'words': article2_words})

#Remove from the list the non-semantically relevant words (the “stopwords”), using the
# attached file “stopwords_en.txt” for the list of stopwords. 
stopwords_file = open('stopwords_en.txt', 'r')
stopwords = []
for word in stopwords_file:
    word = word.strip()
    if word:
        stopwords.append(word)
stopwords_file.close()

cleaned_words1 = []
for word in article1_words:
    cleaned_word = ""
    for char in word:
        if char.isalnum() or char.isspace():
            cleaned_word += char.lower()
    if cleaned_word and cleaned_word not in stopwords and len(cleaned_word) >= 3:
        cleaned_words1.append(cleaned_word)

cleaned_words2 = []
for word in article2_words:
    cleaned_word = ""
    for char in word:
        if char.isalnum() or char.isspace():
            cleaned_word += char.lower()
    if cleaned_word and cleaned_word not in stopwords and len(cleaned_word) >= 3:
        cleaned_words2.append(cleaned_word)

df1 = pd.DataFrame({'words': cleaned_words1})
df2 = pd.DataFrame({'words': cleaned_words2})

#Extract bigram, generating a separate list
bigrams1 = list(nltk.bigrams(cleaned_words1))
bigrams2 = list(nltk.bigrams(cleaned_words2))


#Outputting the bigrams to a file so that they can be fully displayed
with open('bigrams_output.txt', 'w') as f:
    f.write("\nBigrams from first article:\n")
    for bigram in bigrams1:
        f.write(f"{bigram[0]} {bigram[1]}\n")

    f.write("\nBigrams from second article:\n")
    for bigram in bigrams2:
        f.write(f"{bigram[0]} {bigram[1]}\n")

df_bigrams1 = pd.DataFrame({'bigrams': bigrams1})
df_bigrams2 = pd.DataFrame({'bigrams': bigrams2})

#Merge the list of single words with the list of bigrams
df1_combined = pd.concat([df1, df_bigrams1], ignore_index=True)
df2_combined = pd.concat([df2, df_bigrams2], ignore_index=True)

print()
print("Combined words and bigrams for first article:")
print(df1_combined)
print()
print("Combined words and bigrams for second article:")
print(df2_combined)

#Create a wordcloud, calculate the sentiment and the statistics.

wordcloud1 = WordCloud(background_color='white', max_words=2000)
wordcloud1.generate(' '.join(cleaned_words1))
plt.imshow(wordcloud1)
plt.axis('off')
plt.title('Article 1 Word Cloud')
plt.show()

wordcloud2 = WordCloud(background_color='white', max_words=2000)
wordcloud2.generate(' '.join(cleaned_words2))
plt.imshow(wordcloud2)
plt.axis('off')
plt.title('Article 2 Word Cloud')
plt.show()

analyzer = SentimentIntensityAnalyzer()

text1 = ' '.join(cleaned_words1)
text2 = ' '.join(cleaned_words2)

sentiment1 = analyzer.polarity_scores(text1)
sentiment2 = analyzer.polarity_scores(text2)

print('\nThe following is the distribution of the sentiment for Article 1:')
print('\n--- It is positive for', '{:.1%}'.format(sentiment1['pos']))
print('\n--- It is negative for', '{:.1%}'.format(sentiment1['neg']))
print('\n--- It is neutral for', '{:.1%}'.format(sentiment1['neu']), '\n')

print('\nThe following is the distribution of the sentiment for Article 2:')
print('\n--- It is positive for', '{:.1%}'.format(sentiment2['pos']))
print('\n--- It is negative for', '{:.1%}'.format(sentiment2['neg']))
print('\n--- It is neutral for', '{:.1%}'.format(sentiment2['neu']), '\n')

print(f"Article 1 - Lexical diversity: {len(set(cleaned_words1))/len(cleaned_words1):.3f}")
print(f"Article 2 - Lexical diversity: {len(set(cleaned_words2))/len(cleaned_words2):.3f}")
