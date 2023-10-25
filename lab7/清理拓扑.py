import subprocess

commands = [
    'sudo mn -c',
]

for command in commands:
    full_command = "{}".format(command)
    subprocess.Popen(full_command, shell=True)

