import os
import pandas as pd
os.system('cls')

data = pd.read_excel('chat.xlsx')

# Who sent more messages?
members =  data['Miembro'].unique()
messages_number = []

for i in range(len(members)):
    print(f'Mensajes enviados por {members[i]}: {len(data[data['Miembro'] == members[i]])}')
    messages_number.append(len(data[data['Miembro'] == members[i]]))
print(f'Mensajes totales: {sum(messages_number)}')
print('Porcentaje de mensajes enviados:')
for i in range(len(members)):
    print(f'\t{members[i]}: {round(messages_number[i]/sum(messages_number)*100, 2)}%')


# Most used word
total_messages = ''
for i in data['Mensaje']:
    try:
        if i != '<Media omitted>':
            total_messages += i + ' '
    except:
        pass
total_messages = total_messages.split()
word_counter = {}
for i in total_messages:
    if i in word_counter.keys():
        word_counter[i] += 1
    else:
        word_counter[i] = 1

previous_counter = 0
previous_key = ''
for i in word_counter.keys():
    if word_counter[i] > previous_counter:
        previous_counter = word_counter[i]
        previous_key = i

print()
print(f'La palabra más usada fue "{previous_key}", un total de {word_counter[previous_key]} veces')


# Most used emoji
import emoji
emojis_sent = {}
for i in total_messages:
    if i in emoji.EMOJI_DATA:
        if i in emojis_sent.keys():
            emojis_sent[i] += 1
        else:
            emojis_sent[i] = 1

previous_counter = 0
previous_key = ''
for i in emojis_sent.keys():
    if emojis_sent[i] > previous_counter:
        previous_counter = emojis_sent[i]
        previous_key = i
print()
print(f'El emoji más usado fue "{previous_key}", un total de {emojis_sent[previous_key]} veces')