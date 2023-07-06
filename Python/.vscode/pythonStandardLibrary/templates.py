from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
from string import Template
import smtplib

template = Template(Path("template.html").read_text())

message = MIMEMultipart()
message["from"] = "Zeljka Tot"
message["to"] = "zexicc@gmail.com"
message["subject"] = "This is a test"
# sta god zelim da posaljem ovde ubacujem, ako ne zelim templejt vec recimo diksneri ili key word arguments umesto {"name": "Zeljka"} pisem name ="Zeljka"
body = template.supstitute({"name": "Zeljka"})
message.attach(MIMEText(body, "html"))
message.attach(MIMEImage(Path("zeljka.jpg").read_bytes()))

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("zexicc@gmail.com", "Filiskitor15")
    smtp.send_message(message)
    print("Sent.")
