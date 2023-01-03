"""
Python 3.6+
Module to work with GitHub.
"""

import logging
from requests_custom.requests_custom import RequestsCustom

# Initial part of the URL to work with GitHub API.
API_URL = 'https://api.github.com/'
# URL to make test requests.
TEST_URL = 'https://api.github.com/events'

# Format: https://docs.python.org/3/library/logging.html
logging.basicConfig(format=('%(asctime)s'
                            #'- %(filename)s %(lineno)d'
                            ' - %(funcName)s - %(levelname)s'
                            ' - %(message)s'),
                    level=logging.DEBUG)

# Custom requests object.
requests = RequestsCustom().get_requests()


def get_user_repositories(user):
    """ Returns repositories of a GitHub user.
    :param user: str, target GitHub's user name to retrieve info.
    """
    logging.debug('Init')
    # Requested URL
    url = f"{API_URL}{user}"
    url = TEST_URL
    r = requests.get(url)
    logging.debug(f"Get {r.url}")
    logging.debug(r.status_code)
    #logging.debug(r.text)

def get_commit_emails():
    """ Function that retrieves emails of a commit.
    - Request to get emails:
    https://developer.github.com/v3/users/emails/
    - Any commits you made prior to changing your commit email address
    are still associated with your previous email address.
    https://help.github.com/en/github/setting-up-and-managing-your-github-user-account/setting-your-commit-email-address
    """
    logging.debug('Init')

if __name__ == '__main__':
    user = 'CarlosAMolina'
    get_user_repositories(user = user)
