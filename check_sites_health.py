import whois
import requests
from datetime import datetime, timedelta
import sys


def load_urls4check(path):
    with open(path, mode='r') as file:
        return [site.strip() for site in file]


def is_server_respond_with_200(url):
    try:
        if requests.request('GET', url).status_code == requests.codes['ok']:
            return True
        else:
            return False
    except requests.exceptions.ConnectionError:
        return None


def check_domain_expiration_date(domain_name, day_number):
    month_ahead = datetime.now() + timedelta(days=day_number)
    date = whois.whois(domain_name).expiration_date
    if date is None:
        return None
    elif type(date) == list:
        if date[0] > month_ahead:
            return True
    else:
        if date <= month_ahead:
            return False


if __name__ == '__main__':
    try:
        file_with_domains = sys.argv[1]
        list_with_domains = load_urls4check(file_with_domains)
        for domain in list_with_domains:
            print('-'*40)
            print('Web site: {}'.format(domain))
            respond_check = is_server_respond_with_200(domain)
            if respond_check is True:
                print('Is server return status 200 ?: Yes')
            elif respond_check in (False, None):
                print('Is server return status 200 ?: No')
            expiration_check = check_domain_expiration_date(domain, 30)
            if expiration_check is True:
                print('If domain prepaid for the next month?: Yes')
            elif expiration_check in (False, None):
                print('If domain prepaid for the next month?: No')
        print('\n')
    except (FileNotFoundError, IndexError):
        print('Please specify or check your file with sites')
