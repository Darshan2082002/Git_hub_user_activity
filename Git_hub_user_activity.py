import os 
import sys
import json 
import urllib.error
import urllib.request 
class git_hub_user():
    def __init__(self,username):
        self.username=username
        self.url=f"https://api.github.com/users/{username}/events"
    def fetch_activity(self):
        req=urllib.request.Request(
            self.url, headers={"User-Agent": "Python-GitHub-CLI"}
        )
        try:
            with urllib.request.urlopen(req) as response:
                return json.loads(response.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            if e.code == 404:
                print(f"Error: User '{self.username}' not found.")
            elif e.code == 403:
                print("Error: API rate limit exceeded. Please try again later.")
            else:
                print(f"Error: HTTP {e.code}")
            sys.exit(1)
        except urllib.error.URLError as e:
             print(f"Network error: {e.reason}")
             sys.exit(1)





class git_hub():
    def __init__(self,cache_file="cache.json"):
        self.cache_file= cache_file
        
    def save_file(self,data):
        with open(self.cache_file,"w") as f:
            json.dump(data,f,indent=4)


    def load_file(self,filename="text.json"):
        if os.path.exists(self.cache_file):
            with open(self.cache_file,"r") as f:
                return json.load(f)
        return {}
    
    def get_user_activity(self,username):
        cache=self.load_file()
        user=git_hub_user(username)
        events=user.fetch_activity()
        cache[username]=events
        self.save_file(cache)
        return events
    def display_activity(self,username,events):
        if not events:
            print(f"No recent activity found for {username}.")
            return

        print(f"\nRecent activity for {username}:\n")
        for event in events[:10]:
            event_type = event.get("type")
            repo_name = event.get("repo", {}).get("name", "unknown")
            payload = event.get("payload", {})

            if event_type == "PushEvent":
                count = len(payload.get("commits", []))
                print(f"- Pushed {count} commit(s) to {repo_name}")
            elif event_type == "IssuesEvent":
                action = payload.get("action", "updated").capitalize()
                print(f"- {action} an issue in {repo_name}")
            elif event_type == "WatchEvent":
                print(f"- Starred {repo_name}")
            elif event_type == "CreateEvent":
                ref_type = payload.get("ref_type", "resource")
                print(f"- Created {ref_type} in {repo_name}")
            else:
                clean_type = event_type.replace("Event", "")
                print(f"- {clean_type} on {repo_name}")





def main():
    if len(sys.argv) < 2:
        print("Error: Please provide a GitHub username.")
        print("Usage: python script.py <username>")
        sys.exit(1)

    username = sys.argv[1]
    app = git_hub()
    events = app.get_user_activity(username)
    app.display_activity(username, events)



if __name__=="__main__":
    main()



