#!/usr/local/bin/python3.4

import oauth2
import utility
import sys


def main():
	#given parameters are token key and token secret
	client = utility.create_authenticated_client(token_key, token_secret)

	#Step 1 fetching tweet id
	url = "https://api.twitter.com/1.1/statuses/home_timeline.json?count=20"
	resp, content = client.request(url, method="GET")
	id_list_for_retweet = utility.get_twit_id_list(content)
	
	#Step 2 retweet via post call
	for tweet_id in id_list_for_retweet:
		post_url = "https://api.twitter.com/1.1/statuses/retweet/{id}.json"
		post_url = post_url.replace('{id}',str(tweet_id))
		resp, content = client.request(post_url, method="POST")
		utility.print_retweet_result(content)


if __name__ == '__main__':
	print("Diving into Twitter")
	main()
