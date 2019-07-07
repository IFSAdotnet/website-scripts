import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from team_templates import *

# can use name and group description for a better page results
group_list = ['direction@ifsa.net', 'council@ifsa.net', 'LO@ifsa.net', 'cdc.commission@ifsa.net',
              'ipc.commission@ifsa.net', 'communication.commission@ifsa.net', 'rrs@ifsa.net']

# group_list = ['web.commission@ifsa.net']

default_photo = [{'url': 'https://lh4.googleusercontent.com/-MT7weC2IONE/AAAAAAAAAAI/AAAAAAAAAAc/UYN61ez5s-o/s100/photo.jpg'}]

f = open('out.txt', 'w')

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/admin.directory.user',
          'https://www.googleapis.com/auth/admin.directory.group',
          'https://www.googleapis.com/auth/contacts']



creds = None
# The file token.pickle stores the user's access and refresh tokens, and is
# created automatically when the authorization flow completes for the first
# time.
if os.path.exists('token.pickle'):
    with open('token.pickle', 'rb') as token:
        creds = pickle.load(token)
# If there are no (valid) credentials available, let the user log in.
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES)
        creds = flow.run_local_server()
    # Save the credentials for the next run
    with open('token.pickle', 'wb') as token:
        pickle.dump(creds, token)

service_admin = build('admin', 'directory_v1', credentials=creds)
service_people = build('people', 'v1', credentials=creds)


def print_user(user_mail):
    user = service_admin.users().get(userKey=user_mail).execute()
    print(user_mail)
    subs = {
        'description': "",
        'job_title': user['organizations'][0]['title'],
        'name': user['name']['fullName'],
        'name_link': mail2id(user['primaryEmail']),
        'email': user['primaryEmail'],
        # 'pic_url': user.get('thumbnailPhotoUrl', default_photo),
        'pic_link': "",

    }
    photo = service_people.people().get(resourceName="people/"+user['id'], personFields='photos').execute()
    subs['pic_url'] = photo.get('photos', default_photo)[0]['url']
    #print(photo)
    f.write(str(person.substitute(subs)))


def print_group(group_mail):
    members = service_admin.members().list(groupKey=group_mail).execute()
    for m in members['members']:
        if m['type'] == 'USER':
            print_user(m['email'])
        elif m['type'] == 'GROUP':
            print_group(m['email'])


def mail2id(mail):
    return mail[:mail.index('@')]


def main():
    f.write(str(head.substitute()))
    for g in group_list:
        # group name nice way removing ifsa.net suffix and replacing . with spaces
        f.write(str(group_head.substitute(group_link=mail2id(g), group_title=mail2id(g).replace('.', ' ').capitalize())))
        print_group(g)
        f.write(str(group_tail.substitute()))
    f.close()







if __name__ == '__main__':
    main()
