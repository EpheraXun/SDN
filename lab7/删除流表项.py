import subprocess

directory_path = 'python_files'

commands = [
    'python3 delete.py',
]

for command in commands:
    full_command = "cd {} && {}".format(directory_path, command)
    subprocess.Popen(full_command, shell=True)

