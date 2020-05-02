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
GET ?user=violehtone
```

```json
{
    "avatar_url":"https://avatars1.githubusercontent.com/u/33144646?v=4",
    "biggest_repo": {
        "language":"Python",
        "name":"SB1",
        "size":95465
        },
    "html_url":"https://github.com/violehtone",
    "name":"Ville Lehtonen",
    "percentage_of_programming_languages_used":{
        "HTML":0.13793103448275862,
        "Java":0.13793103448275862,
        "JavaScript":0.3448275862068966,
        "Python":0.27586206896551724,
        "R":0.10344827586206896
        },
 "programmer_level":"Rising star",
 "public_repos":32
 }
```

## Author
Ville Lehtonen