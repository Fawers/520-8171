from pprint import pprint  # pretty print

import requests

API_ENDPOINT = 'https://rickandmortyapi.com/api'
API_CHARACTER_ENDPOINT = f'{API_ENDPOINT}/character'
API_EPISODE_ENDPOINT = f'{API_ENDPOINT}/episode'

def rick_and_morty_characters():
    response = requests.get(API_CHARACTER_ENDPOINT)
    data = response.json()
    next_page = data["info"]["next"]
    results = data["results"]

    for r in results:
        yield r

    while next_page is not None:
        data = requests.get(next_page).json()
        next_page = data["info"]["next"]
        results = data["results"]

        yield from results


def main():
    data = enumerate(rick_and_morty_characters(), start=1)
    for index, character in data:
        print(f"{index:03d}", character["name"])


if __name__ == '__main__':
    main()
