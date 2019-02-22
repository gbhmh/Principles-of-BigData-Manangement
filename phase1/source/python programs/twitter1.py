import codecs
import json
import sys

def parse_json_tweet(line):
	tweet = json.loads(line)
	htags=[hashtag['text']for hashtag in tweet['entities']['hashtags']]
	urls=[url['expanded_url']for url in tweet['entities']['urls']]
	return[htags,urls]

if __name__=="__main__":
	file_timeordered_json_tweets=codecs.open("C:/Python27/twitdb2.json", 'r', 'utf-8')
	fout=codecs.open("FileOutput_hash1.txt", 'w', 'utf-8')

for line in file_timeordered_json_tweets:
	try:
		
		[htags,urls] = parse_json_tweet(line)
		fout.write(str([htags,urls]) + "\n")
		print("yes")
	except:
		print("no")
		pass
file_timeordered_json_tweets.close()
fout.close()
