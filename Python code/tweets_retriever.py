class tweets:
    def get(self, search_text, number_of_tweets):
        client_key = 'U0zHy6gQlsMpQumbEgHWXb7nm'
        client_secret = 'CbsDAod2sb31pLqVzBctFdoNMsTQPUZTm1ZInaXm62gmDP7J7I'

        import base64

        key_secret = '{}:{}'.format(client_key, client_secret).encode('ascii')
        b64_encoded_key = base64.b64encode(key_secret)
        b64_encoded_key = b64_encoded_key.decode('ascii')

        import requests

        base_url = 'https://api.twitter.com/'
        auth_url = '{}oauth2/token'.format(base_url)

        auth_headers = {
            'Authorization': 'Basic {}'.format(b64_encoded_key),
            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
        }

        auth_data = {
            'grant_type': 'client_credentials'
        }

        auth_resp = requests.post(auth_url, headers=auth_headers, data=auth_data)

        access_token = auth_resp.json()['access_token']

        search_headers = {
            'Authorization': 'Bearer {}'.format(access_token)
        }


        search_params = {
            'q': search_text,
            'result_type': 'recent',
            'count': number_of_tweets
        }

        search_url = '{}1.1/search/tweets.json?tweet_mode=extended'.format(base_url)

        search_resp = requests.get(search_url, headers=search_headers, params=search_params)
        tweet_data = search_resp.json()
        list_of_tweets = []
        for x in tweet_data['statuses']:
            try:
                list_of_tweets.append(x['retweeted_status']['full_text'] + '\n')
            except KeyError:
                list_of_tweets.append(x['full_text'] + '\n')
        return list_of_tweets

