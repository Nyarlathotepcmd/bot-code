import tweepy
import time
import numpy as np
import random
import sys
import os
def linedel():
	sys.stdout.write("\033[F") #back to previous line
	sys.stdout.write("\033[K") #clear line
def randstring():
	text = open('noMouth.txt', encoding='utf8').read()
	training_text = text.split()
	def make_pairs(training_text):
			for i in range(len(training_text)-1):
					yield (training_text[i], training_text[i+1])
	pairs = make_pairs(training_text)
	word_dict = {}
	for word_1, word_2 in pairs:
			if word_1 in word_dict.keys():
					word_dict[word_1].append(word_2)
			else:
					word_dict[word_1] = [word_2]
	first_word = np.random.choice(training_text)
	while first_word.islower():
			first_word = np.random.choice(training_text)
	chain = [first_word]
	n_words = 50
	for i in range(n_words):
			chain.append(np.random.choice(word_dict[chain[-1]]))
	' '.join(chain)
	string = ''
	for item in chain:
		string += item + ' '
	return(string)
# Authenticate to Twitter
auth = tweepy.OAuthHandler("gGi1jqPRVU8Yx1HOs26PzU4lf", "eK9bBa2gmlquBlVKXNPKY6GIUbI6zX1GEdpQ0Ka2X5iz1cziVT")
auth.set_access_token("1184084081593729024-b3hksvhFbyYpNjA6oy9JNjAy3UJUOB", "QPyI1QuqNsJf5zfGgUSYtZh9GfmJQtyje0vqBTa6W0fV1")
# Create API object
api = tweepy.API(auth)
amount = 0
while True:
	n = random.randint(10,120)
	string = randstring().lower()
	string = string.capitalize() + '.'
	if len(string) <= 278:
		print(string + '\n' + 'length: %s'%len(string))
		while n > 0:
			print (n)
			linedel()
			time.sleep(1)
			n = n - 1
			if n ==0:
				api.update_status(string)
				print('tweet made')
				time.sleep(5)
				cls = lambda: os.system('clear')
				cls()
