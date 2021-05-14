import smtplib 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from secrets import *


def send_plot(email, comp_name, from_date, to_date):
    from_email= email_login
    from_password= email_password
    to_email=email


    subject="Stock Exchange App- requested data"
    message=f"Hello!<br><br> Please find attached your requested Stock Exchange data for <b>{comp_name}</b> for period between <b>{from_date}</b> and <b>{to_date}</b>. <br><br> Thank you for using our app! "


    msg=MIMEMultipart()
    msg.attach(MIMEText(message, "html"))
    msg["Subject"]=subject
    msg["To"]=to_email
    msg["From"]="SE-Data@se-app.lab"


    filename="stock_data.html"
    attachment=open("new_plot.html", "rb")
    p=MIMEBase('application', 'octet-stream')
    p.set_payload((attachment).read())
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', "attachment; filename=%s" %filename)
    msg.attach(p)


    ready_mail=smtplib.SMTP(smtp_address, 587)
    ready_mail.ehlo()
    ready_mail.starttls()
    ready_mail.login(from_email, from_password)
    ready_mail.send_message(msg)
    ready_mail.quit()


