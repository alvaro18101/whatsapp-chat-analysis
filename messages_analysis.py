import os
import pandas as pd
import emoji
os.system('cls')

data = pd.read_excel('chat.xlsx')

# --- GENERAL STATS ---
def get_general_stats(data):
    general_stats = pd.DataFrame(columns=['Total messages', 'Text messages', 'Multimedia', 'Links'])

    general_stats['Total messages'] = [len(data)]
    general_stats['Multimedia'] = (data['Mensaje'] == '<Media omitted>').sum()

    messages_counter = data['Mensaje'].value_counts()
    links_sent = 0
    for i in messages_counter.keys():
        if 'https://' in i:
            links_sent += 1

    general_stats['Links'] = links_sent
    general_stats['Text messages'] = len(data) - ((data['Mensaje'] == '<Media omitted>').sum() + links_sent)
    return general_stats

general_stats = get_general_stats(data)

print('--- GENERAL STATS ---')
for i in general_stats:
    print(f'{i}: {general_stats[i][0]}')



# --- Message per person. Who sent more messages? ---
print()
print()
print('--- MESSAGES PER PERSON ---')
members =  data['Miembro'].unique()
data_member_1 = data[data['Miembro'] == members[0]]
data_member_2 = data[data['Miembro'] == members[1]]

general_stats_1 = get_general_stats(data_member_1)
general_stats_2 = get_general_stats(data_member_2)

print(f'General Stats of {members[0]}')
for i in general_stats_1:
    print(f'\t{i}: {general_stats_1[i][0]}')
print()
print(f'General Stats of {members[1]}')
for i in general_stats_2:
    print(f'\t{i}: {general_stats_2[i][0]}')

messages_number = []
for i in range(len(members)):
    messages_number.append(len(data[data['Miembro'] == members[i]]))
print()
print('Percent of sent messages:')
for i in range(len(members)):
    print(f'\t{members[i]}: {round(messages_number[i]/sum(messages_number)*100, 2)}%')

# --- MOST USED WORDS ---
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

word_counter_sorted = dict(sorted(word_counter.items(), key=lambda item: item[1], reverse=True))
print()
print()
print('--- MOST USED WORDS ---')
print(f'Total words used: {sum(word_counter_sorted.values())}')
j = 0
for i in list(word_counter_sorted.keys()):
    if i not in emoji.EMOJI_DATA:
        print(f'{i}: {word_counter_sorted[i]}')
        j +=1
    if j == 10: 
        break

# --- MOST USED EMOJIS ---
emojis_sent = {}
for i in total_messages:
    for j in i:
        if j in emoji.EMOJI_DATA:
            if j in emojis_sent.keys():
                emojis_sent[j] += 1
            else:
                emojis_sent[j] = 1
emojis_sent_sorted = dict(sorted(emojis_sent.items(), key=lambda item: item[1], reverse=True))

print()
print()
print('--- MOST USED EMOJIS ---')
print(f'Total emojis used: {sum(emojis_sent.values())}')
if len(emojis_sent)<10:
    for i in emojis_sent_sorted:
        print(f'{i}: {emojis_sent_sorted[i]}')
else:
    for i in list(emojis_sent_sorted.keys())[0:10]:
        print(f'{i}: {emojis_sent_sorted[i]}')