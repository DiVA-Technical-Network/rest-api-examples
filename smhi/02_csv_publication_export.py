import csv
import requests
import xml.etree.ElementTree as ET

search_data = """<?xml version="1.0" encoding="UTF-8"?>
    <search>
        <include>
            <includePart>
                <permissionUnitLinkedRecordIdSearchTerm>permissionUnit_smhi</permissionUnitLinkedRecordIdSearchTerm>
                <genericSearchTerm>nederbörd</genericSearchTerm>
            </includePart>
        </include>
        <start>1</start>
        <rows>100</rows>
    </search>
"""

search_data = "".join(line.lstrip() for line in search_data.splitlines())

response = requests.get(
    "https://mig-smhi.pre.diva-portal.org/rest/record/searchResult/outputPublicSearch",
    params={"searchData": search_data},
    headers={"Accept": "application/vnd.cora.recordList+xml"},
)

response.raise_for_status()

xml = ET.fromstring(response.text)

with open("smhi/data/results.csv", "w", newline="", encoding="utf-8") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["id", "title"])
    for record in xml.findall("./data/record/data"):
        record_id = record.findtext("./output/recordInfo/id")
        title = record.findtext("./output/titleInfo/title")
        writer.writerow([record_id, title])
