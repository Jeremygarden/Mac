# coding=utf8
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import sys
import getpass

reload(sys)
sys.setdefaultencoding('utf-8')


'''
    mailto  # Receiver list email address
    mailcc  # Cc' list email address
    sub     # subject
    cont    # content
'''

mail_host = "smtp.163.com"                       # your email host
mail_user = "XXXX@163.com"                       # your email account
mail_pass = getpass.getpass("Password here:")    # your email password
mail_subject = "Text Email to you by python"
mail_postfix = "163.com"




me = "hello" + "<" + mail_user + "@" + mail_postfix + ">"


def send_mail(mailto, mailcc, sub, cont):

    msg = MIMEText(cont, _subtype='plain', _charset='utf8')

    msg['subject'] = unicode(sub)  # subjuct must encode by unicode
    msg['From'] = me
    msg['To'] = ';'.join(mailto)
    msg['Cc'] = ';'.join(mailcc)

    try:
        s = smtplib.SMTP()
        s.connect(mail_host)
        s.login(mail_user, mail_pass)
        s.sendmail(me, mailto, msg.as_string())
        s.close()
        return True
    except smtplib.SMTPException:
        #print "Error: unable to send email"
        return False


def send_attach(mailto, mailcc, sub, path):
    msg = MIMEMultipart()
    att = MIMEText(open(path, 'rb').read(), 'base64', 'utf-8')
    att["Content-Disposition"] = 'attachment; filename="attachname.png"'

    msg.attach(att)
    msg['subject'] = unicode(sub)  # Encoded by unicode
    msg['From'] = me
    msg['To'] = ';'.join(mailto)
    msg['Cc'] = ';'.join(mailcc)


# the file of messages would be sent out.
f = open("mail.txt", 'r')
messages = f.readlines()
f.close()
messages = "".join(messages)


if __name__ == '__main__':

    mail_to_list = ['yeon_1032@163.com']
    mail_cc_list = ['black-johnson@163.com']

    path = '/Users/Jeremy-Li/Download/1M.png'

    if send_mail(mail_to_list, mail_cc_list, mail_subject, messages):
        print "Mail has been sent!"
    elif send_attach(mail_to_list, mail_cc_list, mail_subject, path):
        print "Attach has been sent!"
    else:
        print "Error happens during sending"
