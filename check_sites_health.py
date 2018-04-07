import whois
import requests
from datetime import datetime, timedelta
import sys


def load_urls4check(path):
    with open(path, mode='r') as file:
        return [site.strip() for site in file]


def is_server_respond_with_200(url):
    try:
        if requests.request('GET', url).status_code == 200:
            return 'Yes'
        else:
            return 'No'
    except requests.exceptions.ConnectionError:
        return 'Site not exist'


def check_domain_expiration_date(domain_name):
    month_ahead = datetime.now() + timedelta(weeks=4)
    date = whois.whois(domain_name).expiration_date
    if date is None:
        return 'No data'
    if type(date) == list:
        if date[0] > month_ahead:
            return 'Yes'
    else:
        if date <= month_ahead:
            return 'No'


if __name__ == '__main__':
    try:
        file_with_sites = sys.argv[1]
        list_with_sites = load_urls4check(file_with_sites)
        for site in list_with_sites:
            print('-'*40)
            print('Web site: {}'.format(site))
            print('Is server return status 200 ?: {}'
                  .format(is_server_respond_with_200(site)))
            print('If domain prepaid for the next month?: {}'
                  .format(check_domain_expiration_date(site)))
        print('\n')
    except (FileNotFoundError, IndexError):
        print('Please specify or check your file with sites')
