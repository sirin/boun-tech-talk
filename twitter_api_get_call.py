#!/usr/local/bin/python3.4

import oauth2
import utility
import sys

def main():
	#given parameters are token key and token secret
	client = utility.create_authenticated_client(token_key, token_secret)

	if sys.argv[1] == "timeline":
		print("My precious timeline is streaming...")
		url = "https://api.twitter.com/1.1/statuses/home_timeline.json"
		search_api = False
	elif sys.argv[1] == "from_nasa":
		print("Houston, we've a problem")
		url = "https://api.twitter.com/1.1/search/tweets.json?q=from%3ANASA&result_type=popular&count=20"
		search_api = True
	elif sys.argv[1] == "hashtag_election":
		print("Underwood 2016")
		url = "https://api.twitter.com/1.1/search/tweets.json?q=%23Election2016&result_type=popular&count=20"
		search_api = True

	resp, content = client.request(url, method="GET")
	utility.pretty_print_timeline(content, search_api)		

if __name__ == '__main__':
	print("Diving into Twitter")
	main()
