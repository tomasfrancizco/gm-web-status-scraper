import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(down_sites):

    sender_email = "coe-bi@dentsuaegis.com"
    receiver_email = "tomas.freire@dentsu.com"
    password = ""  # use environment variable
    smtp_server = ""
    smtp_port = 587  # 587 for TLS, 465 for SSL

    # Convert the list of down sites to a string
    down_sites_str = '\n'.join([site['name'] + ' - ' + site['url'] for site in down_sites])

    # Create the email message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = "List of Down Sites"

    # Email body
    email_body = f"The following sites are down:\n\n{down_sites_str}"
    message.attach(MIMEText(email_body, "plain"))

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Start TLS encryption
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
            print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")