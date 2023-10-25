import requests
from requests.auth import HTTPBasicAuth


def http_get(url):
    url = url
    headers = {'Content-Type': 'application/json'}
    return requests.get(url, headers=headers, auth=HTTPBasicAuth('admin', 'admin'))


if __name__ == '__main__':
    url = 'http://127.0.0.1:8181/restconf/operational/opendaylight-inventory:nodes/node/openflow:1/flow-node-inventory:table/0/opendaylight-flow-table-statistics:flow-table-statistics'
    resp = http_get(url)
    print(resp.content)
    
