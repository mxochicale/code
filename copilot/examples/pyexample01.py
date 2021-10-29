import requests
import json

def is_positive(text) :
    """Use a webserver to determine whether the sentiment of the text is positive"""
    url = 'http://text-processing.com/api/sentiment/'
    payload = {'text': text}
    r = requests.post(url, data=payload)
    return r.json()['label'] == 'pos'

positive_examples = [
    'I love this movie',
    'This is a great movie',
    'I love this movie',    
    'I am so exited to go a concert']

negative_examples = [
    'I hate this movie',
    'This is a bad movie',
    'I hate this movie',
    'I am not looking forward to the concert']

for text in positive_examples:
    print(text, is_positive(text))

for text in negative_examples:
    print(text, is_positive(text))
