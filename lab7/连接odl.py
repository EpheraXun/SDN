import subprocess


directory_path = 'controller/odl'


custom_command = 'Carbon/bin/karaf'

command = 'gnome-terminal -- bash -c "cd {} && {} && bash -i"'.format(directory_path, custom_command)
subprocess.Popen(command, shell=True)

