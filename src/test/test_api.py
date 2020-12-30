import unittest
import time
import os

from certspotter.api import CertSpotter


class TestBasicFunction(unittest.TestCase):

  def throttle_getdomains(self, site, after=0):
    api = CertSpotter(os.environ["CERTSPOTTER_TOKEN"])
    if after == 0:
      subdomains, retryinsec = api.getdomains([site])
      if retryinsec != 0:
        print(f'Being throttled, waiting {retryinsec} seconds')
        time.sleep(int(retryinsec)+1)
        subdomains, retryinsec = api.getdomains([site])
        return subdomains, retryinsec
      return subdomains, retryinsec
    else:
      subdomains, retryinsec = api.getdomains([site], after)
      if retryinsec != 0:
        print(f'Being throttled, waiting {retryinsec} seconds')
        time.sleep(int(retryinsec)+1)
        subdomains, retryinsec = api.getdomains([site], after)
        return subdomains, retryinsec
      return subdomains, retryinsec

  def certspot(self, site):
    subdomains_list = []

    subdomains, retryinsec = self.throttle_getdomains(site)
    numEntries = len(subdomains)
    totalEntries = 0
    totalEntries += numEntries
    if numEntries > 0:
      after = subdomains[-1]['id']
    subdomains_list.extend(subdomains)
    if retryinsec != 0:
      print(f"Retry after: {retryinsec} seconds.")

    while numEntries > 0:
      subdomains, retryinsec = self.throttle_getdomains(site, after)
      numEntries = len(subdomains)
      subdomains_list.extend(subdomains)

      if retryinsec != 0:
        print(f"Retry after: {retryinsec} seconds.")

      if numEntries != 0:
        after = subdomains[-1]['id']

      totalEntries += numEntries

    return totalEntries, retryinsec

  def test_good_case(self):
    totalEntries, retryinsec = self.certspot('example.com')
    self.assertFalse(totalEntries == 0)

  def test_bad_case(self):
    totalEntries, retryinsec = self.certspot('dfkslfjaekx.com')
    self.assertTrue(totalEntries == 0)


if __name__ == '__main__':
  unittest.main()
