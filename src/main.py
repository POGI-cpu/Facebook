pip install facebook-sdk

import facebook
# Replace 'your-access-token' with your actual Facebook access token
access_token = 'your-access-token'
graph = facebook.GraphAPI(access_token)
profile = graph.get_object('me')
print(profile)



