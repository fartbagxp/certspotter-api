#!/usr/bin/env python

import requests
from requests.exceptions import HTTPError

'''
This is a simple class to emulate a Certspotter API call based on their API document.
By default, it includes returning all fields for a particular domain.
'''


class CertSpotter:
  def __init__(self, api_token):
    self.token = api_token

  def getdomains(self, domains, after=-1):
    try:
      payload = {'domain': domains,
                 'include_subdomains': 'true', 'expand': ['dns_names', 'issuer', 'cert']}
      if after != -1:
        payload['after'] = after
      url = "https://api.certspotter.com/v1/issuances"
      headers = {'Authorization': 'Bearer ' + self.token}
      response = requests.get(url, headers=headers, params=payload)
      if response.status_code != 200 or response.json() is None:
        print(f'HTTP error occurred: status code was {response.status_code}.')
        return [], 0
      if len(response.json()) == 0 and 'Retry-After' in response.headers:
        return [], response.headers['Retry-After']
      return response.json(), 0
    except HTTPError as http_err:
      print(f'HTTP error occurred: {http_err}')
      return [], 0
    except Exception as err:
      print(f'Other error occurred: {err}')
      return [], 0
