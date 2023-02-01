# trugithub-backend

For any queries ping me at dev.ritik.matere@gmail.com

## Prerequisites

You need python version of `3.8` and above.

## Local Setup

### 1. Create a `python` virtual environment

In your terminal run the following:

Linux:
```sh
python3 -m venv .venv
```

Windows:
```sh
python -m venv .venv
```

MacOS I have no idea :(

### 2. Activate the virtual environment

In terminal run the following

Linux & Mac:
```sh
source .venv/bin/activate
```

Windows (In command prompt):
```sh
.venv\bin\activate
```

### 3. Install dependencies

After previous two steps, install dependencies by running:

Windows & Linux (Mac not sure):
```sh
pip install -r requirements.txt
```

### 4. Run the project

**IMPORTANT:**

Before running, please set the value of `TOKEN` in app.py as the string representation of an access token obtained from your Github account. For this project a `Fine Grained Access` token type was used; other types aren't tested.

Comment the line that goes as `TOKEN = os.getenv('github_API_key')`

After setting `TOKEN`, run the following in terminal:

```sh
uvicorn app:app --reload
```

### 5. Using the project

Following assumptions are made and are to be followed when running the project:

- There is only *ONE* endpoint namely, `http://localhost:8000/profile/`.
- To this endpoint you can add *ONE* or *TWO* query parameters:
    - *ONE* being `username`, say, `http://localhost:8000/profile/?username=johnpapa`
        - Usernames not following Github's naming conventions are dealt with at the front-end itself; hence no use trying to pass such a username here.
    - *TWO* being `username` AND `page`, (for getting paginated repo details),
    say `http://localhost:8000/profile/?username=johnpapa&page=2` .

### 6. Testing

Following is the assumption made for testing although logically abiding by the terms.

While for the success case, `status_code` is 200, for failure it is contrarily also `200` as opposed to `4XX`.

This is because the logic to deal with non-existent users on frontend isn't based on `4XX` code, but a message.

In `test_app.py` there are two function definitions, to test any _ONE_ of them, comment the _OTHER ONE_ and in a terminal run the following:

```sh
pytest
```
