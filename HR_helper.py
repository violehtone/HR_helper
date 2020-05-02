from flask import Flask, jsonify, request, abort
import requests
import json


app = Flask(__name__)

# command line to run:
#$ export FLASK_APP=hello_world.py
#$ flask run

# Some github API calls
# - GET https://api.github.com/users/violehtone
# - GET https://api.github.com/users/violehtone/repos?per_page=50

#TODO:
# Add error handling (i.e. if key is not in dictionary or it is None etc.)
# Test with multiple github accounts
# Host on Heroku
# IDEA: recruiter helper
    # -> Find the languages where the candidate is most proficient
    # -> Find the level of the programmer
    # -> Find the most important project of the candidate to further look at it
    # -> Provide some basic information about candidate (i.e. picture etc.)
    # -> Future ideas: develop algorithms further and add functionalities


@app.route('/', methods = ['GET'])
def get_user():
    baseurl = "https://api.github.com/users/"
    username = request.args.get('user')

    try:
        # Get information about the user and his/her (public) repositories
        user_data = requests.get(f"{baseurl}{username}").json()
        repo_data = requests.get(f"{baseurl}{username}/repos?per_page=50").json()

        # Filter only name, github url, # of public repos, and avatar image from the user data
        result = {i: user_data[i] for i in ('name', 'html_url', 'public_repos', 'avatar_url')}
    except:
        #if user was not found, return 404
        abort(404)

    # Find repo with biggest size
    biggest_repo_size = 0
    biggest_repo_index = 0
    programming_languages = {}

    for i in range(0, len(repo_data)):
        # Store the index of the biggest repo
        print("DEBUGGING repo_data[i]:", repo_data[i]["size"], type(repo_data[i]["size"]), " BIGGEST: ", biggest_repo_size)

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
    biggest_repo = {"name" : name_of_repo, "language" : planguage, "size" : biggest_repo_size}

    # Count the % of programming languages used
    total = sum(programming_languages.values())
    perc_programming_languages = {k: v / total for total in (sum(programming_languages.values()),) for k, v in programming_languages.items()}

    # Add a 'programmer level' for the user based on the amount of repos
    if result['public_repos'] >= 40:
        programmer_level = 'Godlike developer'
    elif result['public_repos'] >= 20:
        programmer_level = 'Rising star'
    else:
        programmer_level = 'Beginner :)'

    # Add information on biggest repo
    result["biggest_repo"] = biggest_repo
    # Add programming rank
    result['programmer_level'] = programmer_level
    # Add percentages of programming languages used
    result['percentage_of_programming_languages_used'] = perc_programming_languages
    
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug = True)