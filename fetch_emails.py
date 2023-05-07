import imaplib
import email
import pprint
import datetime
import yaml

with open("gmail.yaml") as f:
    content = f.read()

my_credentials = yaml.load(content, Loader=yaml.Loader)
user, password = my_credentials["user"], my_credentials["password"]
imap_url = 'imap.gmail.com'

my_mail = imaplib.IMAP4_SSL(imap_url)
my_mail.login(user, password)
my_mail.select('Inbox')

# calculate the date 3 days ago
three_days_ago = datetime.date.today() - datetime.timedelta(days=3)
date_format = three_days_ago.strftime('%d-%b-%Y')

# search for unread emails from the last 3 days
_, data = my_mail.search(None, f'(UNSEEN SINCE "{date_format}")')
latest_unread_emails = data[0].split()

for num in latest_unread_emails:
    _, data = my_mail.fetch(num, '(RFC822)')
    msg = email.message_from_bytes(data[0][1])
    sender_name, sender_addr = email.utils.parseaddr(msg['From'])
    print(f'Subject: {msg["Subject"]}')
    print(f'Sender: {sender_name}')
    print(f'Date: {msg["Date"]}')
    print()

my_mail.close()
