from urllib.request import urlopen

story = urlopen('http://sixty-north.com/c/t.txt')
story_words = []

for line in story:
    line_words = line.split()
    for words in line_words:
        story_words.append(words)

story.close()



