import smtplib
import ssl

def mailer(str_message):
    port = 465  # For SSL
    smtp_server = ""
    sender_email = ""  # Enter your address
    receiver_email = [""]  # Enter receiver address
    password = ''

    print(str_message)
    message = f"""From: contact@essaylancing.com \n
        To: {receiver_email} \n
        This message is sent from Python.\n
        {str_message}"""

    print(message)
    
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        try:
            server.login(sender_email, password)
            print('logged in')
            # server.sendmail(message["From"], message['To'], message)
            server.sendmail(sender_email, receiver_email, message)
            print('mail sent?')
        except Exception as e:
        # Print any error messages to stdout
            print(e