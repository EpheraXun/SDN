import json
import requests as rq

RYU_CONTROLLER = 'http://127.0.0.1:8080'

import requests

def get_topology():

    base_url = 'http://127.0.0.1:8080'
    

    switches_response = requests.get(f'{base_url}/v1.0/topology/switches')
    if switches_response.status_code != 200:
        print(f"Error: Received status code {switches_response.status_code} from server.")
        return 
    switches = switches_response.json()

    hosts_response = requests.get(f'{base_url}/v1.0/topology/hosts')
    hosts = hosts_response.json()


    links_response = requests.get(f'{base_url}/v1.0/topology/links')
    links = links_response.json()


    print("Switches:", switches)
    print("Hosts:", hosts)
    print("Links:", links)


def get_flow_entries(switch_id):
    response = rq.get(RYU_CONTROLLER + f'/stats/flow/{switch_id}')
    data = response.json()

    print(f"Flow Entries for Switch {switch_id}:")
    flows = data[str(switch_id)]
    for flow in flows:
        print(json.dumps(flow, indent=2))

if __name__ == '__main__':
    url = 'http://127.0.0.1:8080/stats/flowentry/add'
    headers = {'Content-Type': 'application/json'}
    f = open('flow.json').read()
    flows = json.loads(f)['flows']
    [rq.post(url, data=json.dumps(flows[i]), headers=headers) for i in range(0, 8)]
    get_topology()
    get_flow_entries(1)

