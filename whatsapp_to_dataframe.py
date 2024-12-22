import re
import os
import pandas as pd
os.system('cls')

chat_name = 'WhatsApp Chat with Norka.txt'
with open(chat_name, encoding='utf-8') as file:
    chat = file.read()

chat = chat[chat.index('\n')+1:-1] # Remove the first message (encryption information) and the last one (empty string)
chat_split = chat.split('\n')


def verifyMessage(line_message):
    try:
        re.search(r'[0-9]+/[0-9]+/[0-9]+,\s[0-9]+:[0-9]+\s(a|p)m\s-\s', line_message).group()
        return True
    except:
        return False


def getData(line_message):
    date = re.search(r'[0-9]+/[0-9]+/[0-9]+', line_message).group()
    time = re.search(r'[0-9]+:[0-9]+\s(a|p)m', line_message).group()
    line_message = line_message.replace(date + ', ' + time + ' - ','')
    contact = line_message[0:line_message.index(':')]
    message = line_message[line_message.index(':')+2:]
    return date, time, contact, message

i = 0
for line_message in chat_split:
    if verifyMessage(line_message) == False:
        chat_split[i] = '---'
    i += 1


for i in range(chat_split.count('---')):
    chat_split.remove('---')

print('Cantidad de mensajes: ', len(chat_split))

data = pd.DataFrame(columns=['Fecha', 'Hora', 'Miembro', 'Mensaje'])
for line_message in chat_split:
    date = re.search(r'[0-9]+/[0-9]+/[0-9]+', line_message).group()
    time = re.search(r'[0-9]+:[0-9]+\s(a|p)m', line_message).group()
    line_message = line_message.replace(date + ', ' + time + ' - ','')
    contact = line_message[0:line_message.index(':')]
    message = line_message[line_message.index(':')+2:]

    data = data._append({'Fecha': date, 'Hora': time, 'Miembro': contact, 'Mensaje': message}, ignore_index=True)

data['Hora'] = data['Hora'].str.replace('\u202f', ' ')

data.to_excel('chat.xlsx', index=False)