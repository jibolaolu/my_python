import smtplib
import getpass

smtp_object = smtplib.SMTP('smtp.gmail.com', 587)
print(smtp_object.ehlo())

mtls = smtp_object.starttls()
print(mtls)

password = getpass.getpass('Password please')