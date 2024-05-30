# para ejecutar:
# $ python3 -m venv myenv
# $ source myenv/bin/activate
# $ python3 main.py
# para salir del entorno:
# $ deactivate

import json
from web_scraper import check_sites
from email_sender import send_email

# Load sites from JSON
with open('sites.json', 'r') as file:
    sites = json.load(file)

# Check sites and get the list of down sites
down_sites = check_sites(sites)

# If there are down sites, send an email
if down_sites:
    # send_email(down_sites)
    print("There are some sites down.")
else:
    print("All sites are up. No email sent.")
