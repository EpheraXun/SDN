import subprocess

directory_path = 'python_files'

commands = [
    'python3 show.py',
]

for command in commands:
    full_command = "cd {} && {}".format(directory_path, command)
    subprocess.Popen(full_command, shell=True)


