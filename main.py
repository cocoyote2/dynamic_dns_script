import os
import ovh
import json
from dotenv import load_dotenv

load_dotenv()

DNS_ZONE_NAME = os.getenv("DNS_ZONE_NAME")
SUBDOMAIN_NAME = os.getenv("SUBDOMAIN_NAME")

client = ovh.Client(
    endpoint='ovh-eu',
    application_key=os.getenv("APPLICATION_KEY"),
    application_secret=os.getenv("APPLICATION_SECRET"),
    consumer_key=os.getenv("CONSUMER_KEY"),
)

dns_zone_id = client.get(f"/domain/zone/{DNS_ZONE_NAME}/record", subDomain=SUBDOMAIN_NAME,  fieldType="A")[0]

result = client.get(f"/domain/zone/{DNS_ZONE_NAME}/record/{dns_zone_id}")

print(json.dumps(result, indent=4))