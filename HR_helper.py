from flask import Flask, jsonify, request, abort
import requests
import json


app = Flask(__name__)


@app.route('/', methods = ['GET'])
def get_user():
    # Handle query parameter (username)
    baseurl = "https://api.github.com/users/"
    username = request.args.get('user')

    try:
        # Fetch user and repository information from Github api 
        user_data = requests.get(f"{baseurl}{username}").json()
        repo_data = requests.get(f"{baseurl}{username}/repos?per_page=50").json()

        # From user information, filter only relevant information and store it into the result object
        user_information = {i: user_data[i] for i in ('name', 'html_url', 'public_repos', 'avatar_url')}
        result = {}
        result["user_information"] = user_information
    except:
        # If user was not found, return Not Found (404)
        abort(404)

    #Parse repository data and get the biggest repository (in rows of code) and the percentage of different programming languages used
    biggest_repo_and_languages = getBiggestRepoAndProgrammingLanguagesUsed(repo_data)
    biggest_repo = biggest_repo_and_languages[0]
    programming_languages = biggest_repo_and_languages[1]

    # Add a 'programmer level' for the user based on the amount of repos
    result['programmer_level'] = defineProgrammerLevel(result)

    # Add information about the most significant piece of work (i.e. the biggest repo)
    result["Most_significant_work"] = biggest_repo

    # Add the percentages of different programming languages used
    result['Programming languages used (%)'] = calculatePercentageOfProgrammingLanguagesUsed(programming_languages)
    
    return jsonify(result)


def defineProgrammerLevel(result):
    """ Takes a json object with a key 'public_repos' and defines the level of the programmer  """
    n_public_repos = result["user_information"]['public_repos']

    if n_public_repos >= 40:
        programmer_level = 'Godlike developer'
    elif n_public_repos >= 20:
        programmer_level = 'Rising star'
    else:
        programmer_level = 'Beginner :)'
    
    return programmer_level


def calculatePercentageOfProgrammingLanguagesUsed(programming_languages):
    total = sum(programming_languages.values())
    for key in programming_languages.keys():
        programming_languages[key] = str(round((programming_languages[key] / total) * 100)) + "%"

    return programming_languages
    

def getBiggestRepoAndProgrammingLanguagesUsed(repo_data):
    # Find repo with biggest size
    biggest_repo_size = 0
    biggest_repo_index = 0
    programming_languages = {}

    for i in range(0, len(repo_data)):
        # Store the index of the biggest repo
        if repo_data[i]["size"] > biggest_repo_size:
            biggest_repo_size = repo_data[i]["size"]
            biggest_repo_index = i

        # Update the amount of repos of specific programming languages
        if repo_data[i]["language"] in programming_languages and repo_data[i]["language"] is not None:
            programming_languages[repo_data[i]["language"]] += 1
        else:
            if repo_data[i]["language"] is not None:
                programming_languages[repo_data[i]["language"]] = 1

    name_of_repo = repo_data[biggest_repo_index]["name"]
    planguage = repo_data[biggest_repo_index]["language"]
    biggest_repo = {"Repository name" : name_of_repo, "Programming language used" : planguage, "Project size (in rows)" : biggest_repo_size}

    return biggest_repo, programming_languages


if __name__ == '__main__':
    app.run(debug = True)