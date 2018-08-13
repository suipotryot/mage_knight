# -*- coding: utf-8 -*-

from radish import given, when, then
from urllib import request
import requests

API_BASE_URL = "http://127.0.0.1:8000"

API_URLS = {
    HEALTH = "%s/_health" % API_BASE_URL,
    NEW_GAME = "%s/new_game" % API_BASE_URL,
}


@given(r"The API is up")
def api_is_up(step):
    r = requests.get(API_BASE_URL)
    assert r.status_code == 200, \
        "Epected code %s to be 200" % r.status_code

@given(r"I start a new game with the following parameters:")
def start_new_game(step):
    r = requests.post(API_BASE_URL, data=step.table)
    assert r.status_code == 200, \
        "Epected code %s to be 200" % r.status_code
    

# @given('Next {elements:g} are:')
# def have_the_string(step, elements):
#     pass
