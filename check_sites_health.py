import whois
import requests
from datetime import datetime, timedelta
import sys


def load_urls4check(path):
    with open(path, mode='r') as file:
        return [domain.strip() for domain in file]


def is_server_respond_with_200(url):
    try:
        return requests.request('GET', url).status_code == requests.codes['ok']
    except requests.exceptions.ConnectionError:
        return None


def check_domain_expiration_date(domain_name, days_number):
    days_ahead = datetime.now() + timedelta(days=days_number)
    date = whois.whois(domain_name).expiration_date
    if date is None:
        return None
    elif type(date) == list:
        if date[0] > days_ahead:
            return True
    else:
        if date <= days_ahead:
            return False


def print_to_console(domain, cnt_days, respond_check, expiration_check):
    print('-'*40)
    print('Web site: {}'.format(domain))
    if respond_check:
        print('Is server return status 200 ?: Yes')
    else:
        print('Is server return status 200 ?: No')
    if expiration_check:
        print('If domain prepaid for the next month?: Yes')
    else:
        print('If domain prepaid for the next month?: No')


if __name__ == '__main__':
    try:
        file_with_domains = sys.argv[1]
        list_with_domains = load_urls4check(file_with_domains)
        cnt_days = 30
        for domain in list_with_domains:
            respond_check = is_server_respond_with_200(domain)
            expiration_check = check_domain_expiration_date(domain, cnt_days)
            print_to_console(domain, cnt_days, respond_check, expiration_check)
        print('\n')
    except (FileNotFoundError, IndexError):
        print('Please specify or check your file with sites')
