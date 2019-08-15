# Goal

This is a simple python library for utilizing sslmate's certspotter v1 API.

## How to use this library

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

## Helpful Documentation

[The Certspotter V1 API](https://sslmate.com/certspotter/api/docs-v1)
