#log add
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Function to read logs and check for warnings
def check_warnings(log_file):
    warnings = []
    with open(log_file, 'r') as file:
        for line in file:
            if 'WARNING' in line:
                warnings.append(line)
    return warnings

# Function to send an email with the warnings
def send_email(warnings, recipient_email):
    # Email configuration
    sender_email = "your_email@example.com"
    sender_password = "your_password"
    subject = "Log Warnings Detected"
    
    # Email content
    body = "The following warnings were detected in the logs:\n\n" + "\n".join(warnings)
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = recipient_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))
    
    # Send the email
    try:
        with smtplib.SMTP('smtp.example.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, message.as_string())
        print(f"Email sent successfully to {recipient_email}")
    except Exception as e:
        print(f"Failed to send email: {e}")

if __name__ == "__main__":
    # Path to the combined log file
    log_file = "/path/to/backups/combined_logs_YYYY-MM-DD.txt"
    
    # Check for warnings
    warnings = check_warnings(log_file)
    
    if warnings:
        # Email recipient
        recipient_email = "recipient@example.com"
        send_email(warnings, recipient_email)
    else:
        print("No warnings found in the logs.")
