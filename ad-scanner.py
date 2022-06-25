import nmap
import argparse
import os

def main():
    Parser = argparse.ArgumentParser()
    Parser.add_argument('-ip', help='Specify domain controller IP', required=True)
    Args = Parser.parse_args()
    IPADDR = Args.ip
    print(f"[i] Scanning : {IPADDR}")

# Création d'une fonction pour chaque vulnérabilités et la call dans main()

def eternalblue_check():
    print("Scanning for MS17-010")

def zerologon_check():
    print("Scanning for CVE-2020-1472")

def ms_14_068():
    print("Scanning for MS14-068")

if __name__ == '__main__':
    main()
