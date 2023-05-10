import socket

HOST = ''  # Symbolic name, meaning all available interfaces
PORT = 12345  # Arbitrary non-privileged port

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
s.bind((HOST, PORT))

# Listen for incoming connections
s.listen(1)

print('Listening on port', PORT)

while True:
    # Wait for a client to connect
    conn, addr = s.accept()
    print('Connected by', addr)

    # Send a greeting message to the client
    message = 'Hello, welcome to the chat bot!'
    conn.sendall(message.encode('utf-8'))

    # Close the connection
    conn.close()
