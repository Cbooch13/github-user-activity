# CLI program to fetch github user activity through API.  Roadmap.sh project
# Caleb Bucci
# 2024-10-07

import argparse
import requests
import json

#Fetches public github events for user: username
def fetchGithubActivity(username: str, printJSON: bool):
    api_url = f"https://api.github.com/users/{username}/events"
    response = requests.get(api_url)
    #Verifys that request is valid
    if response.status_code == 200:
        events = response.json()
        
        #Optionally prints user activity to json file
        if (printJSON):
            with open("events.json", "w") as file:
                file.write(json.dumps(events, indent=4))
        
        #Prints output depending on event type
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
                print(f"{event['payload']['action'].capitalize()} a pull request in {event['repo']['name']}")
            elif event['type'] == 'PullRequestReviewEvent':
                print(f"Reviewed pull request #{event['payload']['pull_request']['number']} in {event['repo']['name']}")
            elif event['type'] == 'PullRequestReviewCommentEvent':
                print(f"Commented on pull request #{event['payload']['pull_request']['number']} in {event['repo']['name']}")
            elif event['type'] == 'PullRequestReviewThreadEvent':
                print(f"Updated review thread in pull request #{event['payload']['pull_request']['number']} in {event['repo']['name']}")
            elif event['type'] == 'PushEvent':
                commitNum = len(event['payload']['commits'])
                plural = "s"
                if commitNum == 1:
                    commitNum = 'a'
                    plural = ""
                print(f"Pushed {commitNum} commit{plural} to {event['repo']['name']}")
            elif event['type'] == 'ReleaseEvent':
                print(f"Released version {event['payload']['release']['tag_name']} in {event['repo']['name']}")
            elif event['type'] == 'SponsorshipEvent':
                print(f"{event['payload']['action'].capitalize()} sponsorship in {event['repo']['name']}")
            elif event['type'] == 'WatchEvent':
                print(f"- Starred {event['repo']['name']}")
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
    parser.add_argument('-p', "--print", action='store_true', help="Prints user activity to json file")
    args = parser.parse_args()

    fetchGithubActivity(args.username, args.print)


if __name__ == "__main__":
    main()