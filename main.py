import tweepy
import time
import numpy as np
def randstring():
	trump = open('speeches.txt', encoding='utf8').read()
	corpus = trump.split()
	def make_pairs(corpus):
			for i in range(len(corpus)-1):
					yield (corpus[i], corpus[i+1])
	pairs = make_pairs(corpus)
	word_dict = {}
	for word_1, word_2 in pairs:
			if word_1 in word_dict.keys():
					word_dict[word_1].append(word_2)
			else:
					word_dict[word_1] = [word_2]
	first_word = np.random.choice(corpus)
	while first_word.islower():
			first_word = np.random.choice(corpus)
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
	time.sleep(60)
	string = randstring()
	if len(string) <= 280:
		print(string + '\n' + str(len(string)))
		api.update_status(string)