import requests

def number_of_subscribers(subreddit):
    """
    Retrieves the number of subscribers for a given subreddit.

    Parameters:
    - subreddit (str): The name of the subreddit.

    Returns:
    - int: The number of subscribers for the subreddit. Returns 0 if the subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': '0x16-api_advanced:project: v1.0.0'}  # Set a custom User-Agent
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
