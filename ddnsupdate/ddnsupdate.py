import configparser
import requests
from requests.auth import HTTPDigestAuth


def read_configuration(config_file):
    config = configparser.ConfigParser()
    config.read(config_file)
    return config


def update_domain(url, auth_tuple, query):
    response = requests.get(url, auth=HTTPDigestAuth(*auth_tuple), params=query)
    if response.status_code == requests.codes.ok:
        print('ok')
    else:
        print('error {}'.format(response.status_code))
    

def run_update(config_file='domains.cfg'):

    config = read_configuration(config_file)

    for domain in config.sections():
        print('[{}]'.format(domain), end=' ')

        data = config[domain]
        url = data['url']
        auth = (data['username'], data['password'])

        query = {
            'hostname': domain,
            'type': data['type'],
            'data': data['data']
        }

        update_domain(url, auth, query)


if __name__ == '__main__':
    run_update()