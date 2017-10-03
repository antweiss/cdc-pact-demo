import requests


def get_welcome_message():
    """Fetch the welcome message ."""
    uri = 'http://localhost:32768/'
    print requests.get(uri).text


def build(buildnum):
    """Fetch a build by number ."""
    uri = 'http://localhost:1234/builds/' + str(buildnum)
    return requests.get(uri).json()

#print build(3455)
