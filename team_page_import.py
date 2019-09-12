import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from team_templates import *
import datetime

users_dir = {'IFSA Board':
    [
        'amos.amanubo',
        'damiano.cilio',
        'catharina.schmidt',
        'kirsten.langmaid',
        'maximilian.schubert',
        'daniel.guerra',
        'jiayi.chew'
    ],
    'Liason Officers':
    [
        'itzhak.lopez',
        'mahtuf.ikhsan',
        'matus.urbancik',
        'volodymyr.kravets',
        'yulia.cuthbertson'
    ],
    'Communication Commission':
    [
        'annebel.soer',
        'simone.massaro',
        'sylvannisa.putri',
        'ece.acaroglu',
        'ezhilan.nambi'
    ],
    'International Processes Commission':
    [
        'oindrila.basu',
        'barbara.oellerer',
        'sara.reimanis',
        'frederik.buchholz',
        'alina.lehikoinen',
        'stipan.cupic'
    ],
    'Capacity Development Commission':
    [
        'junaid.peters',
        'fergus.price',
        'luisa.gragnaniello'
    ],
    "Regional Representatives":
    [
        'angel.goldsmith',
        'addison.riddle',
        'felipe.astorga',
        'estefani.arroyo',
        'jilian',
        'yutung.hung',
        'mari.tuvikene',
        'bo.kofod',
        'elif.duman'
    ]
}

default_photo = [{
    'url': 'https://lh4.googleusercontent.com/-MT7weC2IONE/AAAAAAAAAAI/AAAAAAAAAAc/UYN61ez5s-o/s100/photo.jpg'}]

f = open('out.txt', 'w')

# connect to google API ----
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


def print_user(user_mail, f):
    print(user_mail)
    user = service_admin.users().get(userKey=user_mail).execute()
    photo = service_people.people().get(resourceName="people/" + user['id'], personFields='photos').execute()
    subs = {
        'description': "",
        'job_title': user['organizations'][0]['title'],
        'name': user['name']['fullName'],
        'name_link': mail2id(user['primaryEmail']),
        'email': user['primaryEmail'],
        'pic_url': photo.get('photos', default_photo)[0]['url'],
        'pic_link': ""
    }
    f.write(str(person.substitute(subs)))


# def print_group_users(group_mail, f):
#     members = service_admin.members().list(groupKey=group_mail).execute()
#     if not 'members' in members:  # guard against empty groups, need to refactor!!
#         return False
#     for m in members['members']:
#         if m['type'] == 'USER':
#             print_user(m['email'], f)
#         elif m['type'] == 'GROUP':
#             print_group_users(m['email'], f)


# def print_group_info(group_mail, f):
#     # get group name
#     group_title = service_admin.groups().get(groupKey=group_mail).execute()['name']
#     f.write(str(group.substitute(group_link=group_mail), group_title=group_title)))

def print_group_info(group_name, f):
    print(group_name)
    f.write(str(group.substitute(group_link=group_name.replace(' ', '-').lower(), group_title=group_name)))


def mail2id(mail):
    return mail[:mail.index('@')]


def id2mail(id):
    return id + "@ifsa.net"


def print_import_info(f):
    f.write(f"<!-- team members imported on {datetime.datetime.now()}-->\n\n")


def main():
    print_import_info(f)
    f.write(str(head.substitute()))
    for name, users in users_dir.items():
        print_group_info(name, f)
        for user in users:
            print_user(id2mail(user), f)
    f.close()


if __name__ == '__main__':
    main()
