# Send Email with Attachments

# Fix '5.7.8 Username and Password not accepted. Learn more at\n5.7.8  https://support.google.com/mail/?p=BadCredentials pc11sm17551706pjb.17 - gsmtp'
# turn off 2-factor authentication
# https://www.google.com/settings/security/lesssecureapps

# pip install yagmail

import yagmail

from_ = 'your email here'
password = 'your password here'
receiver = 'receiver email here'
body = 'this is a python mail'
filename = 'progit.pdf'

yag = yagmail.SMTP(from_, password)
yag.send(
    to=receiver,
    subject='test mail',
    contents=body,
    attachments=filename
    )