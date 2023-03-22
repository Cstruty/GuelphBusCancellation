import facebook

# Step 1: Create a Facebook Developer account and an app
# Step 2: Obtain an access token to authenticate your requests to the API
# You can get a long-lived user access token using the Facebook Graph API Explorer:
# https://developers.facebook.com/tools/explorer/
access_token = 'YOUR_ACCESS_TOKEN_HERE'

# Step 3: Use the API to retrieve the page's posts
graph = facebook.GraphAPI(access_token)
page_id = 'PAGE_ID_HERE'
posts = graph.get_connections(page_id, 'posts')

# Get the latest post
latest_post = posts['data'][0]

# Output the content of the latest post
print(latest_post['message'])