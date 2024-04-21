from win32com import client
from sys import argv

def send_mail(to, title, text):
    outlook = client.Dispatch("Outlook.Application")
    mail = outlook.CreateItem(0)
    mail.bodyFormat = 1
    mail.to = to
    mail.Subject = title
    mail.Body = text
    mail.Send()
def main():
    global To, Title, Text
    print("This is a MailTo.py")
    print("This soft is send mail.")
    if len(argv) == 1:
        while True:
            print("Send mail.")
            send_mail(input("To : "), input("Title : "), input("Text : "))
            print("done send mail.")
    elif len(argv) == 3 or len(argv) == 4:
        if len(argv) == 3:
            To = argv[1]
            Title = argv[2]
            Text = argv[2]
        else:
            To = argv[1]
            Title = argv[2]
            Text = argv[3]
        send_mail(To, Title, Text)
    print("Done send mail.")
    return

if __name__ == '__main__':
    main()