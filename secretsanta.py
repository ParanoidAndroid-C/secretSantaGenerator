import smtplib, ssl
import random

port = 587  # For starttls
smtp_server = "smtp.gmail.com"
# don't forget to turn on access to less secure apps on sender's google acc or it won't be able to sign in from this app
sender_email = "sender@gmail.com" # enter email address that will send emails 
password = input("Type your password and press enter: ")


# "name : email address"
myDict = { "someone" : "someone@gmail.com", "someone1" : "someone1@gmail.com", "someone2" : "someone2@gmail.com", "someone3" : "someone3@gmail.com" }

names = list(myDict.keys())

random.shuffle(names)
print(names)
for i in range(len(names)):
    name = names[i]
    if i != (len(names)-1):
        secret_santa_email = myDict[names[i+1]]
    else:
        secret_santa_email = myDict[names[0]]
          
    receiver_email = secret_santa_email  

    message = """\
    Subject: Hi there

    You are {}'s secret santa! 
    """.format(name)
    
    #print(name, secret_santa_email)


    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
        
    
    print("sent successfully")
       
