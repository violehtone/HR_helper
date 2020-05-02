# HR Helper
Are you a technical recruiter who is looking for talented software developers?

Does the following situation sound familiar to you? - You publish a job ad for a software developer position, and immediately you'll get hundreds (if not thousands) of applications. How to quickly determine which of these applicants you should invite to an interview?

**Don't worry!** The 'HR helper API' is here to help you :)

HR helper is an API that helps HR people to quickly fetch relevant information about a developer candidate by utilizing information from Github API v3.

By using the github username as an input, this api provides relevant information about the user, such as his/her greatest project and the different programming languages he/she has worked with so far.

_this project is still work in progess and is currently only a POC!_

## Getting started
**Running server locally**
To run the API locally, you need to have Flask installed (you can install it with pip install flask)

To start this server locally, simply clone the repository and input the following on command line:
```
$ export FLASK_APP=HR_helper.py
$ flask run
```

and then you can fetch the user information with the following command:
```
http://{port}?user={username}
```

where {port} is the port that the service is running in and {username} is the person's github username that you are looking for.


**Accessing the API online**

This HR-helper API is also running online on Heroku. You can  access the API  at

```
https://violehtonen-hrhelper.herokuapp.com/?user={username}
```

where {username} is the github account of the person you're looking for


## Using the HR helper API
The HR helper API currently accepts only one type of requests as shown above. Given the github username, the API just simply fetches all the relevant information of this user.

Example output of the api with the following GET request
```
https://violehtonen-hrhelper.herokuapp.com/?user=violehtone
```

```json
{
    "user_information": {
        "name": "Ville Lehtonen",
        "avatar_url": "https://avatars1.githubusercontent.com/u/33144646?v=4",
        "html_url": "https://github.com/violehtone",
        "public_repos": 33
    },
    "most_significant_work": {
        "repository_name": "SB1",
        "programming_language_used": "Python",
        "repository_size": 95465
    },
    "programming_languages_used": {
        "HTML": "13%",
        "Java": "13%",
        "JavaScript": "33%",
        "Python": "30%",
        "R": "10%"
    },
    "programmer_level": "Rising star"
}
```
- The **'user information'** contains only the relevant information about the person (i.e. name, number of repositories, and url to profile pic and github account)

- The **'most significant work'** is the largest project (in terms of code) that the person has worked on. This could (potentially?) be a good project to further discuss on an interview.

- The **'programming languages used'** gives the different programming languages that the person has worked with as well as their relative percentage i.e. how many projects out of all projects have been written with this language

- Last, the **'programmer level'** is a simple indication of the expertise of the person and it is (currently) simply determined by the amount of projects that the person has worked with.


## Author
Ville Lehtonen