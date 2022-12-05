import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#login  and data entry function
def login():
    YOUR_EMAIL = input("Enter Your Email Address : ")
    YOUR_PASSWORD = input("Enter Your Password : ")
    YOUR_DESTINATION_EMAIL = input("Enter Email Destination : ")
    YOUR_SUBJECT_EMAIL = input("Enter Subject : ")
    YOUR_BODY_EMAIL = input("Enter Message : ")
    return YOUR_EMAIL, YOUR_PASSWORD, YOUR_DESTINATION_EMAIL, YOUR_SUBJECT_EMAIL, YOUR_BODY_EMAIL




#Setup the MIME
def mime_setup(youremail, destemail, subjectemail):
    message = MIMEMultipart()
    message['From'] = youremail
    message['To'] = destemail
    message['Subject'] = subjectemail   #The subject line
    return message




#Create SMTP session for sending the mail
def create_send(youremail, password, destemail):
    try:
        session = smtplib.SMTP('smtp.gmail.com', 587 ) #use gmail with port
        session.ehlo()
        session.starttls() #enable security
        session.ehlo()
        session.login(youremail, password) #login with mail_id and password
        text = message.as_string()
        session.sendmail(youremail, destemail, text)
        session.quit()
        print('Mail Sent')
    except:
        print('failed to send email')


#----------------------------------------------Calling functions--------------------------------------------------------------------
#Calling function login
YOUR_EMAIL, YOUR_PASSWORD, YOUR_DESTINATION_EMAIL, YOUR_SUBJECT_EMAIL, YOUR_BODY_EMAIL = login()

#Calling function mime_setup
message = mime_setup(YOUR_EMAIL, YOUR_DESTINATION_EMAIL, YOUR_SUBJECT_EMAIL)

#The body and the attachments for the mai
message.attach(MIMEText(YOUR_BODY_EMAIL, 'plain'))

#Calling function send email
create_send(YOUR_EMAIL, YOUR_PASSWORD, YOUR_DESTINATION_EMAIL)