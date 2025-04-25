# Win-Mal
Think before execute!
⚠️ WAARSCHUWING: Deze code is kwaadaardig van aard. Gebruik dit nooit op een productiesysteem of zonder expliciete toestemming.


📄 Ransomware Simulation - Educational Purposes Only
Overzicht:
Dit project is een volledig functionele ransomware payload geschreven in Python, bedoeld voor onderzoeksdoeleinden in een gesloten en gecontroleerde labomgeving.
Het demonstreert bestandsversleuteling, command-and-control communicatie, en ransomwaregedrag met waarschuwingstekst.


🔧 Functionaliteiten:
🔐 AES Encryptie: Versleutelt bestanden in C:/Users met AES (EAX-mode)

📁 Doelmap: Versleutelt bestanden recursief

📝 Ransom Note: Plaatst waarschuwing in C:/Users/Public/RANSOM.txt

🌐 C2 Communicatie: Contacteert een .onion C2-server

🧬 Device ID: Uniek op basis van SHA-256 van de hostname


🧨 Self-destruct: Verwijdert zichzelf bij "kill"-commando


🔐 Encryptiemechanisme:
Sleutel gebaseerd op random key + salt van hostname

AES in EAX-mode (met integriteitscontrole)

Bestanden worden overschreven met de versleutelde inhoud



📡 Command & Control Logica:
POST elke 5 minuten naar:
http://your-darkweb-server.onion/status

Payload:

json
Copy
Edit
{ "id": "<machine_id>", "status": "active" }
Mogelijke commando's van C2:

Commando	Actie
exfil	Uploadt RANSOM.txt terug naar C2
kill	Verwijdert het scriptbestand


🧪 Veilig testen:
Gebruik altijd een offline Windows VM

Pas pad aan naar bijv. ./testfolder voor dummydata

Gebruik snapshots/herstelpunten

Voeg logging toe voor inzicht



📁 Bestandsoverzicht:
heavyshit.txt: hoofdscript met payload

RANSOM.txt: waarschuwingstekst voor het slachtoffer



📜 Juridische disclaimer:
Deze code is uitsluitend bedoeld voor:

Cybersecurity educatie

Malware-analyse

Forensisch onderzoek

Red team simulaties in geautoriseerde omgevingen

Gebruik voor kwaadaardige doeleinden is strafbaar.


