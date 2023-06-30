import requests
import argparse

def get_followed_accounts(username, bearer_token):
    url = f"https://api.twitter.com/1.1/friends/list.json"
    params = {
        "screen_name": username,
        "count": 10000  # Maximum number of accounts to retrieve (adjust as needed)
    }
    headers = {
        "Authorization": f"Bearer {bearer_token}"
    }
    response = requests.get(url, params=params, headers=headers)
    
    if response.status_code == 200:
        followed_accounts = response.json()["users"]
        return [account["screen_name"] for account in followed_accounts]
    elif response.status_code == 401:
        raise Exception("Authentication error. Please check if the provided Bearer Token is valid.")
    elif response.status_code == 404:
        raise Exception(f"User '{username}' not found or account is private.")
    else:
        raise Exception(f"Failed to retrieve followed accounts for '{username}'. Twitter API returned status code {response.status_code}.")

def main():
    parser = argparse.ArgumentParser(description="Get the accounts followed by a Twitter user.")
    parser.add_argument("target_username", nargs="?", help="The target Twitter username")
    parser.add_argument("--file", help="Path to a .txt file containing a list of Twitter usernames")
    parser.add_argument("--bearer_token", required=True, help="Your Twitter Bearer Token")
    args = parser.parse_args()

    if args.target_username:
        usernames = [args.target_username]
    elif args.file:
        with open(args.file, "r") as file:
            usernames = [line.strip() for line in file]
    else:
        print("Please provide either a target_username or a --file argument.")
        return

    for username in usernames:
        try:
            followed_accounts = get_followed_accounts(username, args.bearer_token)
            print(f"The account '{username}' follows: {', '.join(followed_accounts)}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
