import twitter


consumer_key = 'SAk1EcgwgIzYbMYK6UdgxoOjq'
consumer_secret = '5WrznTMrKTXu2DX95EIGCGuIzrIrdbeiJ77pOvH5SkrCjkNoS5'
access_token = '1441509311604133896-Hh0fS3sOBiNLqpwRrTG6TZMFUuJ4xB'
access_token_secret = 'aHvrrLjY8THLkh7JNaljhHcBaQhA8wKkVFEYm9HCw2Gj2'

api = twitter.Api(consumer_key=consumer_key,
                  consumer_secret=consumer_secret,
                  access_token_key=access_token,
                  access_token_secret=access_token_secret)

# twitter search results for a given term
search_result = api.GetSearch('a great cake')
print(search_result)

# twitter user search results for a given term
search_result = api.GetUsersSearch('a great cake')
print(search_result)


