# CLI program to fetch github user activity through API.  Roadmap.sh project
# Caleb Bucci
# 2024-09-23

import argparse
import requests
import json

def fetchGithubActivity(username: str):
    api_url = f"https://api.github.com/users/{username}/events"
    response = requests.get(api_url)
    if response.status_code == 200:
        events = response.json()
        with open("temp.json", "w") as file:
            file.write(json.dumps(events, indent=4))
        
        print("Output:")
        for event in events:
            if event['type'] == 'PushEvent':
                pass

    else:
        print(f"Status code: {response.status_code}")


def main():
    
    #Argument parser
    parser = argparse.ArgumentParser(
        prog="github-activity",
        description="CLI program to fetch Github user activity"
    )
    parser.add_argument("username", help="Github username")

    args = parser.parse_args()

    fetchGithubActivity(args.username)


if __name__ == "__main__":
    main()