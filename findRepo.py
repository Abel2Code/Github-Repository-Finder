import requests

username = input("Input a GitHub Username: ")
URL = "https://api.github.com/users/" + username + "/repos"

try:
    r = requests.get(url = URL, params = {})
    data = r.json()

    print("Printing Repositories for " + username)
    for repo in data:    
        print(repo['html_url'])
except:
    print("ERROR: Check if valid input")
