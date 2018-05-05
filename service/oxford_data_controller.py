import requests
from urllib.parse import quote
from model.word import Word


def get_data_from_oxford(word: str):
    app_id = 'f5876586'
    app_key = '2e61f453306472a4ea3563151de8ecc4'
    url = 'https://od-api.oxforddictionaries.com/api/v1/entries/en/' + quote(word.lower())
    r = requests.get(url, headers={'app_id': app_id, 'app_key': app_key})
    if r.status_code == 200:
        return r.json()
    else:
        return None


def parse_oxford_response_data(response, word_from_request) -> []:
    result = {}
    if response is None:
        return result.values()
    json_results = response['results'][0]['lexicalEntries']
    for word_definition in json_results:
        definition = [word_definition['entries'][0]['senses'][0]['definitions'][0]]
        word_type = word_definition['lexicalCategory']
        word = Word(word_from_request, definition, word_type)
        if word.word in result.keys():
            result.get(word.word).append_definition(definition)
        else:
            result[word.word] = word
    parsed_result = []
    for value in result.values():
        parsed_result.append(value.prepare_for_quizlet())
    return parsed_result


def get_data_and_parse_it(word) -> []:
    response = get_data_from_oxford(word)
    results = parse_oxford_response_data(response, word)
    return results
