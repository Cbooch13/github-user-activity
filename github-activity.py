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
        with open("events.json", "w") as file:
            file.write(json.dumps(events, indent=4))
        
        print("Output:")
        for event in events:
            print("- ",end="")
            if event['type'] == 'CommitCommentEvent':
                print(f"Created comment on commit in {event['repo']['name']}")
            elif event['type'] == 'CreateEvent':
                print(f"Created {event['payload']['ref_type']} in {event['repo']['name']}")
            elif event['type'] == 'DeleteEvent':
                print(f"Deleted {event['payload']['ref_type']} in {event['repo']['name']}")
            elif event['type'] == 'ForkEvent':
                print(f"Forked {event['repo']['name']} to {event['payload']['forkee']['full_name']}")
            elif event['type'] == 'GollumEvent':
                print(f"Updated wiki pages in {event['repo']['name']}")
            elif event['type'] == 'IssueCommentEvent':
                print(f"{event['payload']['action'].capitalize()} comment on issue #{event['payload']['issue']['number']} in {event['repo']['name']}")
            elif event['type'] == 'IssuesEvent':
                print(f"{event['payload']['action'].capitalize()} an issue in {event['repo']['name']}")
            elif event['type'] == 'MemberEvent':
                print(f"{event['payload']['action'].capitalize()} a member in {event['repo']['name']}")
            elif event['type'] == 'PublicEvent':
                print(f"Made {event['repo']['name']} public")
            elif event['type'] == 'PullRequestEvent':
                
            elif event['type'] == 'PullRequestReviewEvent':

            elif event['type'] == 'PullRequestReviewCommentEvent':

            elif event['type'] == 'PullRequestReviewThreadEvent':

            elif event['type'] == 'PushEvent':

            elif event['type'] == 'ReleaseEvent':

            elif event['type'] == 'SponsorshipEvent':

            elif event['type'] == 'WatchEvent':

            else:
                print(f"User {username} : {event['type']}")

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