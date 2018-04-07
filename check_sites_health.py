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


def get_domain_expiration_date(domain_name):
    try:
        date = whois.whois(domain_name).expiration_date
        if type(date) == list:
            return date[0]
        else:
            return date
    except whois.socket.gaierror:
        return None


if __name__ == '__main__':
    try:
        file_with_sites = sys.argv[1]
        month_ahead = datetime.now() + timedelta(weeks=4)
        list_with_sites = load_urls4check(file_with_sites)
        for site in list_with_sites:
            expiration_date = get_domain_expiration_date(site)
            print('-'*40)
            print('Web site: {}'.format(site))
            print('Is server return status 200 ?: {}'
                  .format(is_server_respond_with_200(site)))
            if expiration_date is None:
                print('If domain prepaid for the next month?: Site not exist')
            elif expiration_date > month_ahead:
                print('If domain prepaid for the next month?: Yes')
            elif expiration_date <= month_ahead:
                print('If domain prepaid for the next month?: No')
        print('\n')
    except (FileNotFoundError, IndexError):
        print('Please specify or check your file with sites')
