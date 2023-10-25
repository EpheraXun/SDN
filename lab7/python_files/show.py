import requests


def show():
    controller_url = "http://127.0.0.1:8181"
    auth = ("admin", "admin")

    topology_url = f"{controller_url}/restconf/operational/network-topology:network-topology"
    response = requests.get(topology_url, auth=auth)

    if response.status_code == 200:
        topology_data = response.json()
        print(topology_data)
    else:
        print(f"Failed to retrieve topology data. Status code: {response.status_code}")
if __name__ == "__main__":
    show()

