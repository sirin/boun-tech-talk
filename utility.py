#!/usr/local/bin/python3.4

import oauth2
import json

def create_authenticated_client(token_key, token_secret):
	consumer = oauth2.Consumer(key=consumer_key, secret=consumer_secret)
	token = oauth2.Token(key=token_key, secret=token_secret)
	client = oauth2.Client(consumer, token)
	return client


def pretty_print_timeline(content, search_api):
	results = json.loads(content.decode(encoding="utf-8", errors="strict"))
	if search_api is True:
		for result in results['statuses']:
			print(result['text'])
	else:
		for result in results:
			user = result['user']
			line = user['name'] + ' --- ' + result['text']
			print(line)

def get_twit_id_list(content):
	id_list = []
	results = json.loads(content.decode(encoding="utf-8", errors="strict"))
	for result in results:
		id_list.append(result['id'])
	return id_list

def print_retweet_result(content):
	results = json.loads(content.decode(encoding="utf-8", errors="strict"))
	print(results.get("retweeted", "not fetch"))
