
import subprocess


directory_path = 'controller'


custom_command = 'ryu-manager ryu/ryu/app/ofctl_rest.py ryu/ryu/app/simple_switch_13.py ryu/ryu/app/rest_topology.py'


command = 'gnome-terminal -- bash -c "cd {} && {} && bash -i"'.format(directory_path, custom_command)
subprocess.Popen(command, shell=True)

