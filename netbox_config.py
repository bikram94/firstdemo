import pynetbox
#import ipdb
import requests
import json

requests.packages.urllib3.disable_warnings()

session = requests.Session()
session.verify = False

nb = pynetbox.api(url="http://127.0.0.1:8000/", token="0123456789abcdef0123456789abcdef01234567")
nb.http_session = session

devices = nb.dcim.devices.all()


for nb_device in devices:
    platform = str(nb_device.platform)
    pri_ip = str(nb_device.primary_ip)
    asset = nb_device.device_role
    site = nb_device.site.id
    print (nb_device,platform,pri_ip,asset, site)


#
# result = nb.dcim.devices.create(
#     name="dc1-leaf13",
#     device_type=2,
#     device_role="1",
#     site="1",
# )
