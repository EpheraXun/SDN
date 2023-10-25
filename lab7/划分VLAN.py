import subprocess

directory_path = 'python_files'

commands = [
    'curl -X DELETE http://127.0.0.1:8080/stats/flowentry/clear/1',
    'curl -X DELETE http://127.0.0.1:8080/stats/flowentry/clear/2',
    'python3 vlan.py',
]

for command in commands:
    full_command = "cd {} && {}".format(directory_path, command)
    subprocess.Popen(full_command, shell=True)

