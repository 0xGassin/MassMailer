import os
import pandas as pd
import sys
import getopt
from email.message import EmailMessage
import ssl
import smtplib
from dotenv import load_dotenv
from pathlib import Path

#Help Menu
def helpMenu():
    print('Usage:')
    print('[+] python3 main.py -i <inputfile>')
    print('[+] python3 main.py --input <inputfile>\n')
    print('Templates:')
    print('[+] Option 1: Uses template 1')
    print('[+] You can add as many templates as you need,\nhowever you will need to rewrite the logic for chosing the templates if you add more than the default amount (3)')

#Main Code
def main(argv):
    dotenv_path = Path('credentials.env')
    load_dotenv(dotenv_path=dotenv_path)
    opts, args = getopt.getopt(argv,"hi:",["file=","help="])

    for opt, arg in opts:
        if opt == '-h':
            helpMenu()
            sys.exit()
        elif opt in ("-i", "--file"):
            csv_loc = arg
            print("[/] What email position is this? ('1','2','3')")
            print("[/] Default value set to '1' (for initial email)")
            type = int(input("Value: "))
            try:
                df = pd.read_csv(csv_loc, sep=',', header=0)
                generateEmail(df, type)
            except:
                print("[-] An error has occurred...")
                print("[-] We could not read your CSV file or CSV file has not been mounted.")
                print("[-] Please check that you are inputting CSV files only, and that they have a 'Name','Title','Company','Contact','Location' and 'Industry' column header")
                print("[-] Closing Program...")
        else:
            helpMenu()

#Email Generator
def generateEmail(csv, type):
    log_file = open("sent.log", "a+")
    try:
        for i in range(0, len(csv)):
            autoEmailer(csv, i, type)
            log_file.write(f"{csv['Contact'][i]}\n")
    except:
        print("[-] CSV not properly formatted.")

#Email Automation
def autoEmailer(csv, index, type):
    emailSender = os.getenv('EMAILADDRESS')
    emailPassword = os.getenv('APPPASSWORD')
    emailRecipient = f'{csv["Contact"][index]}'
    emailScript = f""""""

    subject = f'Security Analysis for {csv["Company"][index]}'
    template1 = f"""
Hi {csv['Name'][index]},
        
I hope you're doing well! My name is ... and I recently came across {csv['Company'][index]} and you seem to be doing some great work! I am messaging you since you are the {csv['Title'][index]} of {csv['Company'][index]} and wanted to setup a meeting with you in the near future.

Also, great work with the website at {csv['Website'][index]} , I'd love to talk more!
    """

    template2 = f"""
Hi {csv['Name'][index]},
    
How are things? You have not yet replied to my email so i though i'd send a follow up regarding {csv['Company'][index]}!
Let me know if you'd like to talk further regarding the points on my first email.
    """

    template3 = f"""
Hi {csv['Name'][index]},

Still no reply... Maybe this email went into spam?
        """

    if(type == 3):
        emailScript = template3
    elif(type == 2):
        emailScript = template2
    else:
        emailScript = template1

    em = EmailMessage()
    em['From'] = emailSender
    em['To'] = emailRecipient
    em['Subject'] = subject
    em.set_content(emailScript)

    context = ssl.create_default_context()

    replied_log = open("replied.log", "r+")
    replied_data = replied_log.read()
    replied_list = replied_data.splitlines()

    replied_status = False

    for i in range(0, len(replied_list)):
        if(emailRecipient == replied_list[i]):
            print("[+] This email already replied!")
            replied_status = True

    if (replied_status == False):
        try:
            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                smtp.login(emailSender, emailPassword)
                smtp.sendmail(emailSender, emailRecipient, em.as_string())
        except:
            print("[-] Couldn't send email!")

        print("[+] Email Sent!")
        print(f"[+] Total Count: {index + 1}")
    else:
        pass

#Init Code
if __name__ == "__main__":
    main(sys.argv[1:])