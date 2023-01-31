from fastapi import FastAPI, Request
import requests
import json
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


token = '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'

@app.get("/profile/")
async def get_profile(request: Request):
    params = request.query_params
    repos_url = f"https://api.github.com/users/{params['username']}/repos?per_page=9"

    # repos is of Type Response[]
    repos = requests.get(url=repos_url, headers={'Authorization': f'token {token}'})

    # Submitted username not found or contains invalid characters like space
    if repos.status_code == 404:
        return json.dumps({'message': 'Invalid User'})

    user_details_url = f"https://api.github.com/users/{params['username']}"
    user_details = requests.get(url=user_details_url, headers={'Authorization': f'token {token}'})
    user_details = user_details.json() # Convert user_details from JSON to dict

    required_details_keys = [
        'avatar_url',
        'name',
        'location',
        'bio',
        'twitter_username',
        'html_url',
    ]

    # Prepare trimmed down object for user details
    final_user_details = {}
    for key in required_details_keys:
        final_user_details[key] = user_details[key]


    # repos_list is of type dict[]
    repos_list = repos.json()
    required_repo_keys = [
        'name',
        'html_url',
        'description',
    ]
    revised_repos = []
    for repo in repos_list:
        revised_repo = {}

        for key in required_repo_keys:
            revised_repo[key] = repo[key]

        # Obtain languages->enlist->insert them
        l = requests.get(url=repo['languages_url'], headers={'Authorization': f'token {token}'})
        revised_repo['languages'] = list(l.json())
        
        revised_repos.append(revised_repo)
    
    response = { # response combines user details and all their repos
        'user_details': final_user_details,
        'repo_details': revised_repos
    }
    return json.dumps(response)
