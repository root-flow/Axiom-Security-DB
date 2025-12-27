#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Axiom-Security-DB | Automated Payload Aggregator v1.1
# Coded by: canmitm

import requests
import os

# Veri kaynakları (Her biri binlerce payload barındıran ham dosyalar)
SOURCES = {
    "XSS": [
        "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Fuzzing/XSS/XSS-Bypass-WAF-Berenice.txt",
        "https://raw.githubusercontent.com/swisskyrepo/PayloadsAllTheThings/master/XSS%20Injection/Intrusive%20XSS.txt"
    ],
    "SQLi": [
        "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Fuzzing/SQLi/Generic-SQLi.txt",
        "https://raw.githubusercontent.com/swisskyrepo/PayloadsAllTheThings/master/SQL%20Injection/Intrusive/Exploit%20MySQL.txt"
    ],
    "SSTI": [
        "https://raw.githubusercontent.com/swisskyrepo/PayloadsAllTheThings/master/Server%20Side%20Template%20Injection/Payloads.txt"
    ],
    "XXE": [
        "https://raw.githubusercontent.com/swisskyrepo/PayloadsAllTheThings/master/XXE%20Injection/Files/Generic_XXE.txt"
    ],
    "Deserialization": [
        "https://raw.githubusercontent.com/GrrrDog/Java-Deserialization-Exploits/master/payloads.txt"
    ]
}

def sync_data():
    for folder, urls in SOURCES.items():
        print(f"[*] Syncing {folder} vectors...")
        unique_payloads = set()
        
        for url in urls:
            try:
                res = requests.get(url, timeout=15)
                if res.status_code == 200:
                    unique_payloads.update(res.text.splitlines())
            except:
                pass

        # Klasörleme: Web-Exploitation altında düzenle
        path = f"Web-Exploitation/{folder}"
        if not os.path.exists(path): os.makedirs(path)
        
        with open(f"{path}/payloads.txt", "w") as f:
            for p in sorted(list(unique_payloads)):
                if p.strip(): f.write(p + "\n")
        
        print(f"[+] {folder}: {len(unique_payloads)} total unique payloads.")

if __name__ == "__main__":
    sync_data()
