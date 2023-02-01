from fastapi.testclient import TestClient
from app import app
import json

client = TestClient(app)

success_data = "{\"user_details\": {\"avatar_url\": \"https://avatars.githubusercontent.com/u/1202528?v=4\", \"name\": \"John Papa\", \"location\": \"Orlando, FL\", \"bio\": \"Winter is Coming\", \"twitter_username\": \"john_papa\", \"html_url\": \"https://github.com/johnpapa\", \"public_repos\": 141}, \"repo_details\": [{\"name\": \".github\", \"html_url\": \"https://github.com/johnpapa/.github\", \"description\": null, \"languages\": []}, {\"name\": \"aggregator-app\", \"html_url\": \"https://github.com/johnpapa/aggregator-app\", \"description\": \"serverless function with api aggregator with azure\", \"languages\": [\"JavaScript\"]}, {\"name\": \"all-contributors\", \"html_url\": \"https://github.com/johnpapa/all-contributors\", \"description\": \"\\u2728 Recognize all contributors, not just the ones who push code \\u2728\", \"languages\": [\"HTML\", \"CSS\", \"JavaScript\"]}, {\"name\": \"angular\", \"html_url\": \"https://github.com/johnpapa/angular\", \"description\": \"One framework. Mobile & desktop.\", \"languages\": [\"TypeScript\", \"JavaScript\", \"HTML\", \"Starlark\", \"CSS\", \"Shell\", \"Dockerfile\", \"PHP\", \"PowerShell\", \"JSONiq\"]}, {\"name\": \"angular-2-first-look-launcher\", \"html_url\": \"https://github.com/johnpapa/angular-2-first-look-launcher\", \"description\": \"deprecated\", \"languages\": [\"JavaScript\", \"HTML\", \"CSS\"]}, {\"name\": \"angular-architecture\", \"html_url\": \"https://github.com/johnpapa/angular-architecture\", \"description\": \"Examples of Angular Architecture Concepts\", \"languages\": [\"TypeScript\", \"HTML\", \"JavaScript\", \"CSS\"]}, {\"name\": \"angular-cli\", \"html_url\": \"https://github.com/johnpapa/angular-cli\", \"description\": \"CLI tool for Angular\", \"languages\": [\"TypeScript\", \"Python\", \"HTML\", \"JavaScript\", \"CSS\"]}, {\"name\": \"angular-cosmosdb\", \"html_url\": \"https://github.com/johnpapa/angular-cosmosdb\", \"description\": \"Cosmos DB, Express.js, Angular, and Node.js app\", \"languages\": [\"TypeScript\", \"JavaScript\", \"SCSS\", \"HTML\", \"Dockerfile\"]}, {\"name\": \"angular-event-view-cli\", \"html_url\": \"https://github.com/johnpapa/angular-event-view-cli\", \"description\": \"Angular Demo with a Little bit of a lot of features\", \"languages\": [\"TypeScript\", \"CSS\", \"HTML\", \"JavaScript\", \"Dockerfile\"]}]}"


params_success = {
    'username': 'johnpapa'
}
success_data = json.loads(success_data)

params_failure = {
    'username': 'ohnpapa'
}

failure_data = json.loads("{\"message\": \"Invalid User\"}")

# Success Case
def test_app():
    response = client.get('/profile/', params=params_success)
    assert response.status_code == 200
    assert json.loads(response.json()) == success_data

# Failure Case
def test_app():
    response = client.get('/profile/', params=params_failure)
    assert response.status_code == 200
    assert json.loads(response.json()) == failure_data

