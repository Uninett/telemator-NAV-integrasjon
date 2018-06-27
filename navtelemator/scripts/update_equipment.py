import requests
import json
#Authorization: Token 7850fdbb4bef6649d58a13483a00579b0cf0aedd' https://uninav.uninett.no/api/1/netbox/


nav_base = 'https://uninav.uninett.no/api/1/netbox/'
telemator_base = 'http://srv-telemator.ikt.uninett.no:8080/telemator/equipment/'


def get_nav_equipment(id):
    response = requests.get(nav_base + '?search=' + str(id), headers={
           'Authorization': 'Token 7850fdbb4bef6649d58a13483a00579b0cf0aedd'})
    return response


def get_telemator_equipment(id):
    response = requests.get(telemator_base + id)
    return response


def nav_but_not_telemator():
    response = requests.get(nav_base + '?page_size=300', headers={
               'Authorization': 'Token 7850fdbb4bef6649d58a13483a00579b0cf0aedd'})
    response_data = json.loads(response.text)

    entry_id = []
    for entry in response_data['results']:
        entry_id.append(str(entry['sysname']).encode("utf-8"))

    in_telemator = []
    not_in_telemator = []

    for entry in entry_id:
        response = get_telemator_equipment(entry)
        if response.status_code == 404:
            not_in_telemator.append(entry)
        elif response.status_code == 200:
            in_telemator.append(entry)
        else:
            raise Exception("Error code was not expected: " + response.status_code)

    needs_to_be_updated = []
    list_of_errors = []
    for entry in in_telemator:
        temp_errors = []
        temp_errors.append(entry)
        is_same = True
        nav_equipment = get_nav_equipment(entry).json()['results']
        telemator_equipment = get_telemator_equipment(entry).json()['Equipment']
        try:
            if unicode(nav_equipment[0]['room']['description']) != unicode(telemator_equipment['Addr2']):
                if unicode(nav_equipment[0]['room']['description']) != unicode("None"):
                    print unicode(nav_equipment[0]['room']['description'])
                    is_same = False
                    temp_errors.append(unicode(nav_equipment[0]['room']['description'])+ "/" + unicode(telemator_equipment['Addr2']))
            if str(nav_equipment[0]['room']['id']).upper() != str(telemator_equipment['EqLinkToPt']).upper():
                is_same = False
                temp_errors.append(str(nav_equipment[0]['room']['id']).upper()+ "/" + str(telemator_equipment['EqLinkToPt']).upper())
            try:
                if str(round(float(nav_equipment[0]['room']['position'][0]), 6)) != str(telemator_equipment['Latitude']):
                    is_same = False
                    temp_errors.append(str(round(float(nav_equipment[0]['room']['position'][0]), 6))+ "/" + str(telemator_equipment['Latitude']))
                if str(round(float(nav_equipment[0]['room']['position'][1]), 6)) != str(telemator_equipment['Longitude']):
                    is_same = False
                    temp_errors.append(str(round(float(nav_equipment[0]['room']['position'][1]), 6))+ "/" + str(telemator_equipment['Longitude']))
            except TypeError:
                if str(telemator_equipment['Latitude']) == '0':
                    pass
                elif str(telemator_equipment['Longitude']) == '0':
                    pass
                else:
                    pass
            if str(nav_equipment[0]['chassis'][0]['serial']) != str(telemator_equipment['SerialNo']):
                is_same = False
                temp_errors.append((nav_equipment[0]['chassis'][0]['serial'])+ "/" +str(telemator_equipment['SerialNo']))
            if str(nav_equipment[0]['type']['vendor']).upper() != str(telemator_equipment['Manufact']).upper():
                is_same = False
                temp_errors.append(str(nav_equipment[0]['type']['vendor']).upper()+ "/" +str(telemator_equipment['Manufact']).upper())
            if str(nav_equipment[0]['type']['name']).upper() != str(telemator_equipment['Type']).upper():
                is_same = False
                temp_errors.append(str(nav_equipment[0]['type']['name']).upper()+ "/" +str(telemator_equipment['Type']).upper())
            if is_same is False:
                list_of_errors.append(temp_errors)
                needs_to_be_updated.append(entry)
            else:
                temp_errors = []
        except (IndexError) as e:
            print(entry)
            print(e)
            pass



    with open('in_telemator.txt', 'w') as outfile:
        for entry in in_telemator:
            outfile.write(entry + '\n')

    with open('not_in_telemator.txt', 'w') as outfile:
        for entry in not_in_telemator:
            outfile.write(str(entry + '\n'))

    with open('needs_to_be_updated.txt', 'w') as outfile:
        for entry in needs_to_be_updated:
            outfile.write(str(entry + '\n'))

    with open('errors.txt', 'w') as outfile:
        for entry in list_of_errors:
            outfile.write(str(entry))
            outfile.write('\n\n')

nav_but_not_telemator()

