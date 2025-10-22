
import smtplib
from email.mime.text import MIMEText


# first we will add the email part 

def send_notification(subject, notification):
    
    try:
        sender="springboardmentor579@gmail.com"
        password="xyyk ejbz nzwf roiy"
        receiver="kashishvarshney63@gmail.com"


        # create message
        msg = MIMEText(f"{notification}")
        msg["Subject"]=subject
        msg["From"]= f"Kashish <{sender}>"
        msg["To"]= receiver


        #connect to the Gmail SMTP server
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls() #start TLS encrytion
            server.login(sender, password)
            server.send_message(msg)
            
        print("Email sent Successfully!")
        
    except Exception as e:
        print("Error Occured",e)