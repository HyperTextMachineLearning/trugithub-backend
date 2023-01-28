from fastapi import FastAPI, Request
import requests
import json
app = FastAPI()

@app.get("/profile/")
async def get_profile(request: Request):
    params = request.query_params
    url = f"https://api.github.com/users/{params['username']}/repos"

    # repos is of Type Response[]
    repos = requests.get(url=url)

    # repos_list is of type dict[]
    repos_list = repos.json()

    required_keys = [
        'name',
        'full_name',
        'html_url',
        'description',
    ]

    # First element for revised_repos is the user's avatar URL
    revised_repos = []
    avatar_extracted = False
    for repo in repos_list:
        revised_repo = {}

        if not avatar_extracted:
            revised_repos.append(
                {
                    'avatar_url': repo['owner']['avatar_url']
                }
            )
            avatar_extracted = True

        for key in required_keys:
            revised_repo[key] = repo[key]

        # Obtain languages->enlist->insert them
        l = requests.get(url=repo['languages_url'])
        revised_repo['languages'] = list(l.json())
        
        revised_repos.append(revised_repo)

    return revised_repos
