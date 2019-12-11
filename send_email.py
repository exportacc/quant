from email.mime.text import MIMEText
from email.header import Header as hd
from email.utils import parseaddr , formataddr
import smtplib 

def _format_addr(s):
    name ,addr = parseaddr(s)
    return formataddr((hd(name,'utf-8').encode(),addr))

def send_mail(from_addr , password , to_addr, text):

    smtp_server = 'smtp.gmail.com'
    msg = MIMEText(text,"plain","utf-8")
    msg['From'] = _format_addr('from <%s>' % from_addr)
    msg["to"] = _format_addr("to <%s>" % to_addr)
    msg["Subject"] = hd('Backtest Status','utf-8').encode()
    try: 
        server = smtplib.SMTP_SSL(smtp_server , 465)
        server.login(from_addr ,password)
        server.sendmail(from_addr , [to_addr],msg.as_string() )
        server.quit()
        print("Successfully")
    except: 
        print("Error")
password = 'input your password'
send_mail('email@gmail.com',password,'email@gmail.com',
         text='Python Backtest Finished ! ')
