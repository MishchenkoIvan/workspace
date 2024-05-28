import requests


class GitHub:
    def get_user(self, username):
        r = requests.get(f"https://api.github.com/users/{username}")
        body = r.json()
        
        return body
    
    def search_repo(self, name):
        r = requests.get(
            "https://api.github.com/search/repositories",
            params = {"q": name}
            )
        body = r.json()
        
        return body 
    
    def get_metadata(self, owner, repo):
        r = requests.get(f"https://api.github.com/repos/{owner}/{repo}")
        body = r.json()
        return body
    
    def get_tags(self, owner, repo):
        r = requests.get(f"https://api.github.com/repos/{owner}/{repo}/tags")
        body = r.json()
       
        return body