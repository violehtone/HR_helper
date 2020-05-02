# HR Helper
An API that helps HR people to quickly fetch relevant information about a candidate by utilizing information from Github API v3.

## Getting started
To run the API locally, you need to have Flask installed (you can install it with pip install flask)

To start this server locally, simply input the following on command line:
```
#$ export FLASK_APP=HR_helper.py
#$ flask run
```

Or you can also access the API online at https://.... (work in progress)

## Using the HR helper API
The HR helper API currently accepts only one type of requests as shown below. Given the github username, the API just simply fetches all the relevant information of this user.

Example:
```
GET http://...?user=violehtone
```

```json
{
    "user_information": {
        "name": "Ville Lehtonen",
        "avatar_url": "https://avatars1.githubusercontent.com/u/33144646?v=4",
        "html_url": "https://github.com/violehtone",
        "public_repos": 33
    },
    "Most_significant_work": {
        "Repository name": "SB1",
        "Programming language used": "Python",
        "Project size (in rows)": 95465,
    },
    "Programming languages used (%)": {
        "HTML": "13%",
        "Java": "13%",
        "JavaScript": "33%",
        "Python": "30%",
        "R": "10%"
    },
    "programmer_level": "Rising star",
}
```

## Author
Ville Lehtonen