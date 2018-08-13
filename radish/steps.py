# -*- coding: utf-8 -*-

from radish import given, when, then
from urllib import request

API_HEALTH_URL = '127.0.0.1:8000'


@given("The API is up")
def api_is_up(step):
    api_response = request.urlopen(API_HEALTH_URL)
    assert api_response.getcode() == 200
    

# @given('Next {elements:g} are:')
# def have_the_string(step, elements):
#     pass
