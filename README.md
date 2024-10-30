# Whatsapp chat analysis
Analyze and visualize WhatsApp messages, with statistics on frequency and activity per user.

## Steps to follow:
1. Export the WhatsApp chat (without files), you should get a .txt file
2. Place the file in the same folder as the python files
3. Install the dependencies by running `python -m pip install -r requirements.txt` or `pip install -r requirements.txt`
4. Run the `whatsapp_to_dataframe.py` file first to get the Excel file with the messages.
5. Run the remaining .py files

## Codes
### whatsapp_to_dataframe.py
Reads the WhatsApp chat in .txt format and processes it by exporting an Excel file with the date, time, member who sent the message and the message sent.

**Remark:** You can change the Excel file to a .csv by changing the last line of the code `data.to_excel('chat.xlsx', index=False)` to `data.to_excel('chat.csv', index=False)`.

## messages_per_hour.py
Gives a bar graph with the messages sent in each hour of the day. The colors of each bar will be a gradient of a color defined in the variable `base_color` and will increase to lighter tones as the number of messages decreases.

# messages_analysis.py
Prints to the console:
- Messages sent by each user
- Total messages
- Percentage of messages sent by each user
- Most used word
- Most used emoji

**Remark:** The text shown is in Spanish, for the moment.

## Features to be implemented:
- Most used words
- Chart with most used emojis
- Quantity of multimedia sent
- Who starts more conversations?