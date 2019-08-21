import smtplib
import random
import time
import sys
import os


reciever_email = input("Enter a valid email you would like to spam: ")
while True:
    try:
        times = int(input("Enter how many times you would like spam that email: "))
        break
    except:
        print("\nMust be a digit")

while True:
    try:
        delay = int(input("Please specify the interval between the emails (seconds): "))
        break
    except:
        print("\nMust be a digit")


def spam(reciever_email):
    try:
        
        def get_details():
            
            def file(sender_loggin,sender_password,line_count):
                f = open('login_detail.txt','r')
                details = f.readlines()
                for i in details:
                    if line_count % 2 == 0:
                        sender_password.append(i)
                        line_count = line_count + 1

                    else:
                        sender_loggin.append(i)
                        line_count = line_count + 1

                        
    
            sender_loggin = []
            sender_password = []
            line_count = 1

            file(sender_loggin,sender_password,line_count)

            x = len(sender_password)
            x = x-1
            value = random.randint(0,x)

            e = sender_loggin[value]
            e.strip()
            p = sender_password[value]
            p.strip()

            return e,p
            f.close()


            

        def get_subject():
            f = open('subjects.txt','r')
            all_sub = f.readlines()
            x = (len(all_sub))- 1
            return all_sub[random.randint(0,x)]

        def get_body():
            f = open('body.txt','r')
            all_body = f.readlines()
            x = (len(all_body))- 1
            return all_body[random.randint(0,x)]


        print("\nAttempting to retrive data from input files")
        time.sleep(2)
        d = get_details()
        email = d[0]
        password = d[1]
        subject = get_subject()
        body = get_body()
 
        
 



        print("\nData retrive successfully")
        print("\nAttempting to send a spam email to '" + str(reciever_email) + "' \nWith a subject '" + str(subject) + "' \nAnd a text msg '" + str(body) + "' \nFrom " +str(email))
        

        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            print("\nEstablishing connection with google servers")
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()
            print("Secure connection to google servers is achieved")

            smtp.login(email,password)

            msg = f'Subject: {subject}\n\n{body}'

            smtp.sendmail(email, reciever_email, msg)

        print("\nThe email was sent successfully")
    except:
        print("Oops, an ERROR occured. Please make sure that all files contain right data and none of them are empty.\nRead the 'README.txt for more information.")
        print("In case this is a network error the rpogramme will re-attempt to continiue in 10 sec\nIf this keeps happening check the input data")
        time.sleep(10)


count = 0
for i in range(times):

    if count == times-1:
        print(count)
        os.system('cls')
        spam(reciever_email)
        count = count + 1
        print("\nThere are " + str(times-count) + " emails left to send")
 
    else:
        os.system('cls')
        spam(reciever_email)
        count = count + 1
        print("\nThere are " + str(times-count) + " emails left to send")
        print("\n\n\nWaiting the set time untill sending next email...")
        time.sleep(delay)
    

print("\n\n\n***** Thank you for using our software *****")
time.sleep(5)







    

