import os
from six.moves import urllib_parse as urlparse
import requests

from flex.core import load, validate_api_call
import tests

BASE_DIR = os.path.dirname(tests.__file__)


def test_validate_api_call(httpbin):
    schema = load(os.path.join(BASE_DIR, 'schemas', 'httpbin.yaml'))

    response = requests.get(urlparse.urljoin(httpbin.url, '/get'))

    validate_api_call(schema, request=response.request, response=response)
