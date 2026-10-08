import requests
from xml.dom.minidom import parseString

res = requests.get(
    "https://mig-smhi.pre.diva-portal.org/rest/record/diva-output/2159",
    headers={"Accept": "application/vnd.cora.record+xml"},
)

print(parseString(res.content).toprettyxml(indent="  "))
