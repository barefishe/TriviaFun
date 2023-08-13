import requests


def get_trviadb(difficulty, qz_number):

    response = requests.get(url=f"https://opentdb.com/api.php?amount={qz_number}&difficulty={difficulty}&type=boolean")
    trivia_db = response.json()["results"]

    return trivia_db



