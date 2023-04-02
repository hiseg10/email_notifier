import imaplib
import email
import json
from win10toast import ToastNotifier
'''
SERVER = 'imap.gmail.com'
PORT = 993
USERNAME = 'hiseg.tec@gmail.com'
PASSWORD = 'senha do app'
'''
enviro = 'dev_env.json'
with open(enviro, 'r') as f:
    config = json.load(f)



mail = imaplib.IMAP4_SSL(config['SERVER'], config['PORT'])
mail.login(config['USERNAME'], config['PASSWORD'])

mail.select('inbox')
status, data = mail.search(None, 'UNSEEN')

notifier = ToastNotifier()
ler_email = []
for num in data[0].split():
    status, data = mail.fetch(num, '(RFC822)')
    email_msg = email.message_from_bytes(data[0][1])
    ler_email.append('Remetente:', email_msg['From'])
    #print('Remetente:', email_msg['From'])
    #print('Assunto:', email_msg['Subject'])
    #print('Corpo:', email_msg.get_payload())
    corpo = notifier.show_toast('Novo e-mail',
                         'De: ' + email_msg['From'] + '\nAssunto: ' + email_msg['Subject'],
                         duration=5)
arquivo = 'text.txt'
with open(arquivo, '+a') as file:
    for x in file:
        ler_email = x.replace()
mail.close()
mail.logout()