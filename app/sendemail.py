import smtplib


def sendemail(fromaddr,fromname,subject,msg):
    toaddr = 'shaq.grant.95@gmail.com'
    message = """From: {} <{}>
    To: {} Shaq
    Subject: {}

    {}
    """

    messagetosend = message.format(
                                 fromaddr,
                                 fromname,
                                 toaddr,
                                 subject,
                                 msg)

    # Credentials (if needed)
    username = 'shaq.grant.95@gmail.com'
    password = 'adgjlxvyynmioopl'

    # The actual mail send
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username, password)
    server.sendmail(fromaddr, toaddr, messagetosend)
    server.quit()



