import socket
from requests import get
import smtplib

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)


router_ip = get('https://api.ipify.org').text


# Send Email Function
def send_email(recipient, subject, msg):
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    gmail_username = '' # Your email goes here
    gmail_password = '' # Your password goes here
    headers = ["From: " + gmail_username, "Subject: " + subject, "To: " + recipient,
               "MIME-Version: 1.0", "Content-Type: text/html"]
    headers = "\r\n".join(headers)

    session = smtplib.SMTP(smtp_server, smtp_port)
    session.ehlo()
    session.starttls()
    session.ehlo()

    session.login(gmail_username, gmail_password)

    session.sendmail(gmail_username, recipient, headers + "\r\n\r\n" + msg)
    session.quit()


msg = "Your new router IP is " + str(router_ip) + ", and your internal IP is " + str(ip_address)

send_email('benchaffe@icloud.com', "IP Change", msg)
