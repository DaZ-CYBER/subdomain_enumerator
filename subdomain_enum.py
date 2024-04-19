# This is a subdomain enumerator developed by DaZ
# Please use ethically
import sys
import requests
import argparse

def subdomain_enum(wordlist, domain):
    print("Wordlist: " + wordlist)
    print("Domain: " + domain)
    list = open(wordlist).read()
    subdomains = list.splitlines()

    for sub in subdomains:

        sub_d = f"http://{sub}.{domain}"
        sub_d_nc = sub_d.lstrip("http://")

        try:
            # print(f"Trying: {sub_d_nc}") - If you'd like to see verbose output
            requests.get(sub_d)
        except requests.ConnectionError:
            pass
        else:
            print(f"+++ {sub_d} +++")

def argument_parser():
    # Initializing argument parser / parser title
    parser = argparse.ArgumentParser(description="Subdomain Enumerator developed by DaZ", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    # Adding arguments to script
    parser.add_argument('-w', '--wordlist', type=str, help="path to wordlist", default=argparse.SUPPRESS)
    parser.add_argument('domain', type=str, help="domain to enumerate", default=argparse.SUPPRESS)
    # Condensing args for configuration to be called in any other function
    args = parser.parse_args()
    config = vars(args)
    return(config)

def main():
    # Initializing argument parser()
    config = argument_parser()

    for k, v in config.items():
        if(k == 'wordlist'):
            wordlist = v
        elif(k == 'domain'):
            domain = v

    subdomain_enum(wordlist, domain)

main()

