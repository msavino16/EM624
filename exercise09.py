# Author: Michael Savino

#"I pledge my honor that i have abided by the Stevens Honor System"

#Exercise 09

#This program will analyze music data from given csv files

#Import required libraries
import matplotlib.pyplot as plt
import pandas as pd

#read the data
song_data = pd.read_csv('Song.csv')
music_sales = pd.read_csv('Music Sales Data 1973-2021.csv')

print(song_data.count())

#1 the most popular artists (2-3), songs (2-3) and medium (streaming, downloaded, radio) [using the Song.csv file]
#top 3 artists by their average rating
top_artists = song_data.groupby('Artist')['Rating'].mean().sort_values(ascending=False).head(3)
print()
print("Top 3 artists by their average rating:")
print(top_artists)

#top 3 songs by their rating
top_songs = song_data.sort_values('Rating', ascending=False)[['Artist', 'Title', 'Rating']].head(3)
print()
print("Top 3 songs by their rating:")
print(top_songs)

#medium usages
total_streams = song_data['Streams'].sum()
total_downloads = song_data['Downloads'].sum()
total_radio = song_data['Radio Plays'].sum()
print()
print("Medium usage:")
print(f"Streaming: {total_streams:.2f}")
print(f"Downloads: {total_downloads:.2f}")
print(f"Radio Plays: {total_radio:.2f}")
print()

#2 the correlation between sales and rating with the medium [using the Song.csv file]
print("Correlations between sales and each medium:")
for medium in ['Streams', 'Downloads', 'Radio Plays']:
    corr = song_data['Sales'].corr(song_data[medium])
    print(f"{medium}: {corr:.2f}")
    
print() 
print("Correlations between rating and each medium:")
for medium in ['Streams', 'Downloads', 'Radio Plays']:
    corr = song_data['Rating'].corr(song_data[medium])
    print(f"{medium}: {corr:.2f}")

#3 the medium with the highest return per song [using the Song.csv file]
#calculate average return per song for each medium
avg_streams = song_data['Streams'].mean()
avg_downloads = song_data['Downloads'].mean()
avg_radio = song_data['Radio Plays'].mean()

print()
print("Average return per medium:")
print(f"Streaming: {avg_streams:.2f}")
print(f"Downloads: {avg_downloads:.2f}")
print(f"Radio Plays: {avg_radio:.2f}")
print()

#4 the evolution of the medium over the years in terms of monetary value  [using the Music Sales Data file]
music_sales_data = pd.read_csv('Music Sales Data 1973-2021.csv')
music_sales_data['Format Value # (Million)'] = music_sales_data['Format Value # (Million)'].str.replace('$', '').str.replace('M', '').astype(float)
yearly_by_format = music_sales_data.pivot_table(index='Year', columns='Format', values='Format Value # (Million)', aggfunc='sum')

#all formats
total_sales_per_format = music_sales_data.groupby('Format')['Format Value # (Million)'].sum()
top_formats = total_sales_per_format.sort_values(ascending=False).index
plt.figure(figsize=(15, 8))
for format_type in top_formats:
    plt.plot(yearly_by_format.index, yearly_by_format[format_type], label=format_type, linewidth=2)
plt.title('Music sales evolution')
plt.xlabel('Year')
plt.ylabel('Sales (Millions of Dollars)')
plt.grid(True)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

#top 5 formats
top_formats = total_sales_per_format.sort_values(ascending=False).head(5).index
plt.figure(figsize=(15, 8))
for format_type in top_formats:
    plt.plot(yearly_by_format.index, yearly_by_format[format_type], label=format_type, linewidth=2)
plt.title('Music sales evolution (top 5 formats)')
plt.xlabel('Year')
plt.ylabel('Sales (Millions of Dollars)')
plt.grid(True)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

#5 the overall most profitable medium (as monetary value) [using the Music Saled Data file]
total_sales_by_format = music_sales_data.groupby('Format')['Format Value # (Million)'].sum()
most_profitable_format = total_sales_by_format.idxmax()
highest_sales = total_sales_by_format.max()
print()
print(f"The most profitable medium is {most_profitable_format} with sales of ${highest_sales:.2f}M")
