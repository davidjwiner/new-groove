import nltk, re, pprint, matplotlib as mil
# import matplotlib.pyplot as plt
mil.use('TkAgg')
# plt.use('TkAgg')

script = open('new-groove-script.rtf', 'r')
raw = script.read().decode('utf8')
tokens = nltk.word_tokenize(raw)

num_char = 6

big_words = [w.lower().strip() for w in tokens if len(w) >= 6 and w.isalpha()] 
fd = nltk.FreqDist(big_words)
fd.plot(30, cumulative=False)

# plt.xlabel('Words')
# plt.ylabel('Frequency')
# plt.title('Frequency of words > ' + num_char + ' characters in The Emperors New Groove')
