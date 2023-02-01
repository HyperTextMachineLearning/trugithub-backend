from fastapi import FastAPI, Request
import requests
import json
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


token = os.getenv('github_API_key')


@app.get("/profile/")
async def get_profile(request: Request):
    REQUIRED_DETAILS_KEYS = [
        'avatar_url',
        'name',
        'location',
        'bio',
        'twitter_username',
        'html_url',
        'public_repos'
    ]
    REQUIRED_REPO_KEYS = [
        'name',
        'html_url',
        'description',
    ]
    HEADERS = {
        'Authorization': f'token {token}', 
        'Access-Control-Allow-Origin': '*'
    }
    
    params = request.query_params
        
    repos_url = f"https://api.github.com/users/{params['username']}/repos?per_page=9"
    
    try:
        page_no = params['page']
        repos_url = repos_url + "&page=" + page_no
        repos = requests.get(url=repos_url, headers=HEADERS)
        repos_list = repos.json()
        revised_repos = []
        for repo in repos_list:
            revised_repo = {}

            for key in REQUIRED_REPO_KEYS:
                revised_repo[key] = repo[key]

            # Obtain languages->enlist->insert them
            l = requests.get(url=repo['languages_url'], headers=HEADERS)
            revised_repo['languages'] = list(l.json())
            revised_repos.append(revised_repo)

        return json.dumps(revised_repos)
    except KeyError:
        pass

    # repos is of Type Response[]
    repos = requests.get(url=repos_url, headers=HEADERS)

    # Submitted username not found or contains invalid characters like space
    if repos.status_code == 404:
        return json.dumps({'message': 'Invalid User'})

    user_details_url = f"https://api.github.com/users/{params['username']}"
    user_details = requests.get(url=user_details_url, headers=HEADERS)
    user_details = user_details.json() # Convert user_details from JSON to dict

    # Prepare trimmed down object for user details
    final_user_details = {}
    print(f'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA {user_details}')
    for key in REQUIRED_DETAILS_KEYS:
        final_user_details[key] = user_details[key]


    # repos_list is of type dict[]
    repos_list = repos.json()
    revised_repos = []
    for repo in repos_list:
        revised_repo = {}

        for key in REQUIRED_REPO_KEYS:
            revised_repo[key] = repo[key]

        # Obtain languages->enlist->insert them
        l = requests.get(url=repo['languages_url'], headers=HEADERS)
        revised_repo['languages'] = list(l.json())
        
        revised_repos.append(revised_repo)
    
    response = { # response combines user details and all their repos
        'user_details': final_user_details,
        'repo_details': revised_repos
    }
    return json.dumps(response)
