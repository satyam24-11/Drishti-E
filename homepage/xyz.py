import imaplib

imap_url = 'imap.gmail.com'
email_address = 'worksatyamkumar437@gmail.com'
password = 'snibspdgxjdliojd'

try:
    conn = imaplib.IMAP4_SSL(imap_url)
    conn.login(email_address, password)
    print("Login successful!")
except Exception as e:
    print(f"Error: {e}")
