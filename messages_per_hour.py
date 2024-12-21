import os
import pandas as pd
import matplotlib.pyplot as plt
# os.system('cls')

data = pd.read_excel('chat.xlsx')

# Get messages per hour for every hour of the day
time_format = lambda string: int(string[:-6])%12 if string[-2:] == 'am' else int(string[:-6])%12 + 12
hour_data = data['Hora'].apply(time_format)
messages_per_hour = [0 for i in range(24)]
for i in hour_data:
    messages_per_hour[i] += 1

X_axis = [str(i) + 'h' for i in range(24)]

# Add a unit (in base 16)
def nextIntensityValue(value):
    letters = ['a', 'b', 'c', 'd', 'e', 'f']
    if value in letters:
        return letters[letters.index(value) + 1] if value != 'f' else 'f'
    else:
        value = str(int(value) + 1)
        return value if value != '10' else 'a'

# Add a unit to the color code
def increaseColor(color_hex_code):
    j = 6
    for i in color_hex_code[::-1]:
        if i != 'f':
            break
        j -= 1
    p1 = color_hex_code[:j]
    chance = nextIntensityValue(color_hex_code[j])
    p2 = color_hex_code[j+1:]
    if j != 6:
        p2 = '0' + color_hex_code[j+2:]
    return p1 + chance + p2

# Add n units to the color code
def increaseColorSeveralTimes(color_hex_code, n):
    for i in range(n):
        color_hex_code = increaseColor(color_hex_code)
    return color_hex_code

# Sort the color intensities based on number of message per hour 
def asignColorString(messages_number, base_color):
    messages_number = messages_number.copy()
    messages_number_ordered = messages_number.copy()
    messages_number_ordered.sort()
    colors = [0 for i in range(len(messages_per_hour))]
    for i in range(len(messages_per_hour)):
        current_message_number = messages_number_ordered[i]
        index_color = messages_per_hour.index(current_message_number)
        if i == 0:
            colors[index_color] = base_color
        else:
            if messages_number_ordered[i] != messages_number_ordered[i-1]:
                base_color = increaseColorSeveralTimes(base_color, 6)
                colors[index_color] = base_color
            if messages_number_ordered[i] == messages_number_ordered[i-1]:
                colors[index_color] = base_color
        messages_number[index_color] = ''
    return colors

base_color = '#f8c0cb'
base_color = '#00ba11'
colors = asignColorString(messages_per_hour, base_color)

# Plotting
fig, ax = plt.subplots(figsize=(10,5))
ax.bar(X_axis, messages_per_hour, color=colors)
plt.savefig('plots/mensajes por hora.png')
plt.show()