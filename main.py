import os
import ovh
import requests
import json
from dotenv import load_dotenv

def get_old_ip():
    dns_zone_id = client.get(f"/domain/zone/{DNS_ZONE_NAME}/record", subDomain=SUBDOMAIN_NAME,  fieldType="A")[0]
    dns_zone = client.get(f"/domain/zone/{DNS_ZONE_NAME}/record/{dns_zone_id}")

    old_ip = dns_zone.get('target')
    
    return old_ip, dns_zone_id

def get_current_ip():
    try:
        return json.loads(requests.get("https://api.ipify.org?format=json", timeout=5).text.strip()).get('ip')
    except Exception as e:
        print(f'Unable to get current IP : {e}')
        return None

load_dotenv()

DNS_ZONE_NAME = os.getenv("DNS_ZONE_NAME")
SUBDOMAIN_NAME = os.getenv("SUBDOMAIN_NAME")

client = ovh.Client(
    endpoint='ovh-eu',
    application_key=os.getenv("APPLICATION_KEY"),
    application_secret=os.getenv("APPLICATION_SECRET"),
    consumer_key=os.getenv("CONSUMER_KEY"),
)

old_ip, dns_zone_id = get_old_ip()
current_ip = get_current_ip()

if old_ip != current_ip:
    client.put(f'/domain/zone/{DNS_ZONE_NAME}/record/{dns_zone_id}', subDomain=SUBDOMAIN_NAME, target=current_ip, ttl=60)

    client.post(f"/domain/zone/{DNS_ZONE_NAME}/refresh")

    print('The zone has been modified !')