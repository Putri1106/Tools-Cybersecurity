import time
import psutil
import pyfiglet
import smtplib
from twilio.rest import Client

ascii_banner = pyfiglet.figlet_format("SANDRINA")
print(ascii_banner)

def monitor_bandwidth():
    last_received = psutil.net_io_counters().bytes_recv
    last_sent = psutil.net_io_counters().bytes_sent
    last_total = last_received + last_sent

    while True:
        bytes_received = psutil.net_io_counters().bytes_recv
        bytes_sent = psutil.net_io_counters().bytes_sent
        bytes_total = bytes_received + bytes_sent

        new_received = bytes_received - last_received
        new_sent = bytes_sent - last_sent
        new_total = bytes_total - last_total

        mb_new_received = new_received / 1024 / 1024
        mb_new_sent = new_sent / 1024 / 1024
        mb_new_total = new_total / 1024 / 1024

        print(f"{mb_new_received:.2f} MB received, {mb_new_sent:.2f} MB sent, {mb_new_total:.2f} MB total")

        last_received = bytes_received
        last_sent = bytes_sent
        last_total = bytes_total

        time.sleep(1)

def send_email():
    email = input("SENDER EMAIL: ")
    receiver_email = input("RECEIVER EMAIL: ")
    subject = input("SUBJECT: ")
    message = input("MESSAGE: ")

    text = f"Subject: {subject}\n\n{message}"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    server.login(email, "cqwrtiyrwnzxlmsp")

    server.sendmail(email, receiver_email, text)

    print("Email has been sent to " + receiver_email)


def send_whatsapp_message():
    account_sid = 'AC68db866710d7225a30769d12654aa202'  # Replace with your Account SID
    auth_token = '2e96e7a5078837c23a1276945bf06d3e'  # Replace with your Auth Token
    from_whatsapp_number = 'whatsapp:+14155238886'  # Your Twilio WhatsApp number
    to_whatsapp_number = 'whatsapp:+6288973624521'  # Replace with your recipient's WhatsApp number

    client = Client(account_sid, auth_token)
    
    message = client.messages.create(
        body='Hai guys!',
        from_=from_whatsapp_number,
        to=to_whatsapp_number
    )
    
    print(f"Message SID: {message.sid}")

def main():
    while True:
        print("\nChoose an option:")
        print("1. Monitor Bandwidth")
        print("2. Send Email")
        print("3. Send WhatsApp Message")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            print("Starting bandwidth monitor...")
            monitor_bandwidth()
        elif choice == '2':
            send_email()
        elif choice == '3':
            send_whatsapp_message()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
