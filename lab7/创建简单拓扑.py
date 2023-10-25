import subprocess


directory_path = 'python_files'


custom_command = 'sudo mn --topo=single,3 --controller=remote,ip=127.0.0.1,port=6633 --switch ovsk,protocols=OpenFlow13'


command = 'gnome-terminal -- bash -c "cd {} && {} && bash -i"'.format(directory_path, custom_command)
subprocess.Popen(command, shell=True)
