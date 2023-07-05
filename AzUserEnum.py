import requests, crayons, concurrent.futures, time
from requests_ip_rotator import ApiGateway
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('-f',"--file", help='File name', required=True)
parser.add_argument('-d',"--domain", help='Domain Name', required=True)
parser.add_argument('--output-file', help='Provide output file path (Optional)', required=False)
parser.add_argument('-t', '--thread', help='Thread Count', required=False)
args = parser.parse_args()

start_time = time.time()

try:
    gateway = ApiGateway("https://login.microsoftonline.com", verbose=False)
    gateway.start()
except Exception as e:
    print(crayons.red("[-] Error: " + str(e), bold=True))
    print("Please verify if AWS IAM users are properly configured and if an API Gateway has been created with the necessary permissions granted.")
    exit()

if args.thread:
    thread_count = int(args.thread)
else:
    thread_count = 10

session = requests.Session()
session.mount("https://login.microsoftonline.com/common/GetCredentialType", gateway)


vaild_emails = []
def verify_email_managed_by_azure(email):
    email = email +"@" +args.domain
    url = "https://login.microsoftonline.com/common/GetCredentialType"
    payload = {"Username": email}
    headers = {"Content-Type": "application/json"}

    response = session.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        result = response.json()
        if result["IfExistsResult"] == 0:
            vaild_emails.append(email)
            return email + " " + crayons.green("True", bold=True)
        elif result["IfExistsResult"] == 1:
            return email + " " +  crayons.red("False", bold=True)
    else:
        return "Error"

def verify_emails_in_file(filename):
    print(crayons.yellow("Verifying...", bold=True))
    with open(filename, "r") as file:
        emails = file.readlines()

    def verify_email(email):
        email = email.strip()
        return verify_email_managed_by_azure(email)

    with concurrent.futures.ThreadPoolExecutor(max_workers=thread_count) as executor:
        results = executor.map(verify_email, emails)

        for result in results:
            print(result)


print('''

\033[1;32m                   _    _                       ______                             
     /\           | |  | |                     |  ____|                            
    /  \     ____ | |  | |  ___    ___   _ __  | |__     _ __    _   _   _ __ ___  
   / /\ \   |_  / | |  | | / __|  / _ \ | '__| |  __|   | '_ \  | | | | | '_ ` _ \ 
  / ____ \   / /  | |__| | \__ \ |  __/ | |    | |____  | | | | | |_| | | | | | | |
 /_/    \_\ /___|  \____/  |___/  \___| |_|    |______| |_| |_|  \__,_| |_| |_| |_|
 ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
 \033[1;34m@trouble1_raunak\033[0m


''')
filename = args.file
verify_emails_in_file(filename)

if vaild_emails != []:
    print("---------------------------------------")
    print(crayons.green("[+] List of vaild Emails", bold=True))
    print("---------------------------------------")
    for email in vaild_emails:
        print(email)

    if args.output_file:
        file = open(args.output_file,'w')
        for item in vaild_emails:
            file.write(item+"\n")
        file.close()
        print()
        print(crayons.green(f'Valid users list saved to {args.output_file}', bold=True))
        print()


print()
print("--- {:.2f} seconds ---".format(time.time() - start_time))
print()
