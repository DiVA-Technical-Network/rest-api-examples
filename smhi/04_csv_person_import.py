import requests
import csv

login_id = "demo@smhi.se"
app_token = "your-apptoken"


def main():
    auth_token = login(login_id, app_token)

    with open("smhi/data/person_import.csv", newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            first_name = row["firstName"]
            last_name = row["lastName"]
            email = row["email"]
            import_person(first_name, last_name, email, auth_token)


def login(login_id, app_token):
    login_response = requests.post(
        "https://mig-smhi.pre.diva-portal.org/login/rest/apptoken",
        headers={
            "Content-Type": "application/vnd.cora.login",
            "Accept": "application/vnd.cora.authentication+json",
        },
        data=f"{login_id}\n{app_token}",
    )

    login_response.raise_for_status()
    login_data = login_response.json()
    for child in login_data["authentication"]["data"]["children"]:
        if child["name"] == "token":
            return child["value"]
    raise ValueError("Authentication token not found")


def import_person(first_name, last_name, email, auth_token):
    person_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
    <person>
        <recordInfo>
            <validationType>
                <linkedRecordType>validationType</linkedRecordType>
                <linkedRecordId>diva-person</linkedRecordId>
            </validationType>
            <dataDivider>
                <linkedRecordType>system</linkedRecordType>
                <linkedRecordId>divaData</linkedRecordId>
            </dataDivider>
        </recordInfo>
        <authority>
            <name type="personal">
                <namePart type="given">{first_name}</namePart>
                <namePart type="family">{last_name}</namePart>
            </name>
        </authority>
        <email repeatId="0">{email}</email>
    </person>"""

    response = requests.post(
        "https://mig-smhi.pre.diva-portal.org/rest/record/diva-person",
        headers={
            "Content-Type": "application/vnd.cora.recordgroup+xml",
            "Accept": "application/vnd.cora.record+xml",
            "AuthToken": auth_token,
        },
        data=person_xml,
    )
    response.raise_for_status()


main()
