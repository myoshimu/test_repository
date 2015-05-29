
import argparse

from apiclient.discovery import build
from oauth2client.client import SignedJwtAssertionCredentials

import httplib2
from oauth2client import client
from oauth2client import file
from oauth2client import tools



def get_service(api_name, api_version, scope, key_file_location,
                service_account_email):

  f = open(key_file_location, 'rb')
  key = f.read()
  f.close()

  credentials = SignedJwtAssertionCredentials(service_account_email, key,
    scope=scope)

  http = credentials.authorize(httplib2.Http())

  # Build the service object.
  service = build(api_name, api_version, http=http)

  return service


def main():
  # Define the auth scopes to request.
  scope = ['https://www.googleapis.com/auth/analytics.manage.users']

  # Use the developer console and replace the values with your
  # service account email and relative location of your key file.
  service_account_email = '147782209718-vcsucghmlq9l0frg309donuqs3rn5d50@developer.gserviceaccount.com'
  key_file_location = 'project-cd5c4096a5a5.p12'

  # Authenticate and construct service.
  service = get_service('analytics', 'v3', scope, key_file_location,
    service_account_email)
 # This request creates a new Property User Link.
  try:
    service.management().webpropertyUserLinks().insert(
      accountId='40985606',
      webPropertyId='UA-40985606-3',
      body={
          'permissions': {
              'local': [
                  'EDIT',
                  'MANAGE_USERS'
              ]
          },
          'userRef': {
              'email': 'miki120111@gmail.com'
          }
      }
    ).execute()

  except TypeError, error:
   # Handle errors in constructing a query.
    print 'There was an error in constructing your query : %s' % error



if __name__ == '__main__':
  main()
