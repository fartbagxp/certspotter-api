import unittest
import os

from certspotter.api import CertSpotter


class TestBasicFunction(unittest.TestCase):

  def certspot(self, site):
    api = CertSpotter(os.environ["CERTSPOTTER_TOKEN"])
    subdomains_list = []

    subdomains, retryinsec = api.getdomains([site])
    numEntries = len(subdomains)
    totalEntries = 0
    totalEntries += numEntries
    if numEntries > 0:
      after = subdomains[-1]['id']
    subdomains_list.extend(subdomains)
    if retryinsec != 0:
      print(f"Retry after: {retryinsec} seconds.")

    while numEntries > 0:
      subdomains, retryinsec = api.getdomains([site], after)
      numEntries = len(subdomains)
      subdomains_list.extend(subdomains)

      if retryinsec != 0:
        print(f"Retry after: {retryinsec} seconds.")

      if numEntries != 0:
        after = subdomains[-1]['id']

      totalEntries += numEntries

    return totalEntries, retryinsec

  def test_good_case(self):
    totalEntries, retryinsec = self.certspot('dhs.gov')
    self.assertFalse(totalEntries == 0)
    self.assertFalse(retryinsec == 0)

  def test_bad_case(self):
    totalEntries, retryinsec = self.certspot('dfkslfjaekx.com')
    self.assertTrue(totalEntries == 0)
    self.assertFalse(retryinsec == 0)


if __name__ == '__main__':
  unittest.main()
