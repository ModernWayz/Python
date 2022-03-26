from ipaddress import ip_address
import os
import sys

try:
    ip_address = sys.argv[1]
    if os.system("ping -c 1 " + ip_address) == 0:
        print(f"The ip: '{ip_address}' is up.")
    else:
        print(f"The ip: '{ip_address}' is down.")
except Exception:
    print("ERROR: Argument 'ip address' not given.")