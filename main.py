import imaplib
import email
from win10toast import ToastNotifier
import json

#import config
# config = {
#     'SERVER': 'imap.gmail.com',
#     'PORT': 993,
#     'USERNAME': 'seu_email@gmail.com',
#     'PASSWORD': 'sua_senha'
# }

#Configurações através de um arquivo na pasta do projeto 
enviro = 'dev_env.json'
with open(enviro, 'r') as f:
    config = json.load(f)

  


mail = imaplib.IMAP4_SSL(config['SERVER'], config['PORT'])
mail.login(config['USERNAME'], config['PASSWORD'])

mail.select('inbox')
status, data = mail.search(None, 'UNSEEN')

notifier = ToastNotifier()

keywords = ['git', 'github', 'commit']
emails = {}

year = 2022
search_query = f'SINCE "01-JAN-{year}" BEFORE "01-JAN-{year + 1}"'
status, data = mail.search(None, search_query)

qnt_x = 0
qnt_x1 = 0

for num in data[0].split():
    status, data = mail.fetch(num, '(RFC822)')
    email_msg = email.message_from_bytes(data[0][1])
    sender = email_msg['From']
    subject = email_msg['Subject']
    body = email_msg.get_payload()
    date = email.utils.parsedate_to_datetime(email_msg['Date'])
    print('Procurando no ano de {}, {} de {} encontrados'.format(date.year ,qnt_x, qnt_x1))
    #print('Status: {} por {}'.format(status, qnt_x))
	#if date.year == year:
    for keyword in keywords:
        qnt_x +=1
        if keyword in subject.lower():
            emails[num] = {'sender': sender, 'subject': subject, 'body': body}
            print(f'Palavra-chave "{keyword}" encontrada no e-mail {num}!')
            qnt_x1 +=1

            
        
	
		
        	
for email in emails.values():
    print('Remetente:', email['sender'])
    print('Assunto:', email['subject'])
    print('Corpo:', email['body'])
    notifier.show_toast('Novo e-mail',
                         'De: ' + email['sender'] + '\nAssunto: ' + email['subject'],
                         duration=5)

mail.close()
mail.logout()
