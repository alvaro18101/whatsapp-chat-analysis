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

dic_messages_per_hour = {}
for i in range(len(messages_per_hour)):
    dic_messages_per_hour[i] = messages_per_hour[i]

# Add a unit (in base 16)
def next_intensity_value(value):
    letters = ['a', 'b', 'c', 'd', 'e', 'f']
    if value in letters:
        return letters[letters.index(value) + 1] if value != 'f' else 'f'
    else:
        value = str(int(value) + 1)
        return value if value != '10' else 'a'

# Add a unit to the color code
def increase_color(color_hex_code):
    j = 6
    for i in color_hex_code[::-1]:
        if i != 'f':
            break
        j -= 1
    p1 = color_hex_code[:j]
    chance = next_intensity_value(color_hex_code[j])
    p2 = color_hex_code[j+1:]
    if j != 6:
        p2 = '0' + color_hex_code[j+2:]
    return p1 + chance + p2

# Add n units to the color code
def increase_color_several_times(color_hex_code, n):
    for i in range(n):
        color_hex_code = increase_color(color_hex_code)
    return color_hex_code

# Sort the color intensities based on number of message per hour
def asign_color_string(dic_messages_number, base_color):
    dic_messages_number_ordered = dict(sorted(dic_messages_number.items(), key=lambda item: item[1])) # Order messages for amount of messages
    dic_colors = dic_messages_number_ordered.copy()
    colors = []
    previus_hour_index = -1
    for i in dic_messages_number_ordered:
        if dic_messages_number_ordered[i] == 0:
            colors.append('#000000')
        else:
            current_amount_messages = dic_messages_number_ordered[i]
            try:
                previus_amount_messages = dic_messages_number_ordered[previus_hour_index]
                if current_amount_messages == previus_amount_messages:
                    colors.append(base_color)
                else:
                    colors.append(base_color)
                    base_color = increase_color_several_times(base_color, 6)
            except:
                colors.append(base_color)
                base_color = increase_color_several_times(base_color, 6)
        previus_hour_index = i
    j = 0
    for i in dic_colors:
        dic_colors[i] = colors[j]
        j += 1
    dic_colors_ordered = dict(sorted(dic_colors.items(), key=lambda item: item[0]))
    return list(dic_colors_ordered.values())

base_color = '#00ba11'

colors = asign_color_string(dic_messages_per_hour, base_color)

# Plotting
fig, ax = plt.subplots(figsize=(10,5))
ax.bar(X_axis, messages_per_hour, color=colors)
plt.savefig('plots/mensajes por hora.png')
plt.show()