class tweets:
    def get(self, search_text, number_of_tweets):
        import base64
        import requests
        import sys
        import re

        client_key = 'U0zHy6gQlsMpQumbEgHWXb7nm'
        client_secret = 'CbsDAod2sb31pLqVzBctFdoNMsTQPUZTm1ZInaXm62gmDP7J7I'

        key_secret = '{}:{}'.format(client_key, client_secret).encode('ascii')
        b64_encoded_key = base64.b64encode(key_secret)
        b64_encoded_key = b64_encoded_key.decode('ascii')

        base_url = 'https://api.twitter.com/'
        auth_url = '{}oauth2/token'.format(base_url)

        auth_headers = {
            'Authorization': 'Basic {}'.format(b64_encoded_key),
            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
        }

        auth_data = {
            'grant_type': 'client_credentials'
        }

        try:
            auth_resp = requests.post(auth_url, headers=auth_headers, data=auth_data)
            access_token = auth_resp.json()['access_token']
        except:
            sys.exit("Error: Authentication failed")


        search_headers = {
            'Authorization': 'Bearer {}'.format(access_token)
        }


        search_params = {
            'q': search_text,
            'result_type': 'recent',
            'count': number_of_tweets
        }

        search_url = '{}1.1/search/tweets.json?tweet_mode=extended'.format(base_url)
        try:
            search_resp = requests.get(search_url, headers=search_headers, params=search_params)
        except:
            print("Error in retrieving tweets from twitter API")
        tweet_data = search_resp.json()
        list_of_tweets = []
        for x in tweet_data['statuses']:
            try:
                tweet = x['retweeted_status']['full_text']
                tweet.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())
                list_of_tweets.append(tweet)
            except KeyError:
                tweet = x['full_text']
                tweet.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())
                list_of_tweets.append(tweet)
        return list_of_tweets

