[![CircleCI](https://circleci.com/gh/fartbagxp/certspotter-api.svg?style=svg)](https://circleci.com/gh/fartbagxp/certspotter-api)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)
[![MIT License](https://img.shields.io/github/license/dawnlabs/carbon.svg)](https://github.com/dawnlabs/carbon/blob/master/LICENSE)
[![codecov](https://img.shields.io/codecov/c/github/fartbagxp/certspotter-api?style=flat-square)](https://codecov.io)

# Goal

This is a simple python library for utilizing sslmate's certspotter v1 API.

## How to use this library

Installation:

```python
pip install certspotter
```

```python
from certspotter.api import CertSpotter

api = CertSpotter("api key")
subdomains, retryinsec = api.getdomains("example.com")
```

## Development

1. Install [Python 3.7+](https://www.python.org/downloads/).
1. Install [pyenv](https://github.com/pyenv/pyenv).
1. Git clone the repository: `git clone git@github.com:fartbagxp/certspotter-api.git`
1. Setup python development environment by running: `pipenv shell && pipenv install`
1. Get an API key from certspotter.
1. Run unit test: `cd certspotter-api/src && python -m unittest discover -v`

## Deploy new version

1. Update `VERSION` in [setup.py](setup.py).
1. Run `git tag <VERSION>`.
1. Run git push --tags.

## Helpful Documentation

[The Certspotter V1 API](https://sslmate.com/certspotter/api/docs-v1)
