'''
9.4 Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
'''
name = raw_input("Enter file:")

if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

message_list = list()

for line in handle:
    if line.startswith("From") and not line.startswith("From:"):
        message_list.append(line)  # append messages to a list

dic = dict()
for message in message_list:
    address = message.split()[1]
    dic[address] = dic.get(address, 0) + 1  # go through the list and count

max_name = None
max_time = None

for name, time in dic.items():
    if max_time is None or time > max_time:
        max_time = time
        max_name = name

print max_name, max_time
