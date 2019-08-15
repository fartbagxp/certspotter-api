#!/usr/bin/env python
from datetime import datetime
import csv
import api

'''
A simple function to print all the fields
'''


def print_subdomains(subdomains):
  for subdomain in subdomains:
    print(subdomain['id'])
    print(subdomain['tbs_sha256'])
    print(subdomain['dns_names'])
    print(subdomain['pubkey_sha256'])
    print(subdomain['issuer'])
    print(subdomain['not_before'])
    print(subdomain['not_after'])
    print(subdomain['cert'])


'''
A simple function to sort the certificate by expiration,
where upcoming expiration is top of the list
'''


def order_by_cert_expiration(subdomains):
  sortedSubdomains = sorted(subdomains, key=lambda i: datetime.strptime(
      i['not_after'], '%Y-%m-%dT%H:%M:%S-%f:00'), reverse=False)
  return sortedSubdomains


'''
A way to write a csv for the results provided the path and the results
'''


def write_csv(filepath, subdomains):
  with open(filepath, mode='w') as csv_file:
    fieldnames = ['id', 'dns_names', 'issuer', 'not_before', 'not_after']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    for subdomain in subdomains:
      dns_names = ','.join(subdomain['dns_names'])
      writeResult = {
          'id': subdomain['id'],
          'dns_names': dns_names,
          'issuer': subdomain['issuer'],
          'not_before': subdomain['not_before'],
          'not_after': subdomain['not_after']
      }
      writer.writerow(writeResult)


'''
