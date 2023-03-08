# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import socket

HOST = '127.0.0.1'  # localhost
PORT = 1234  # choose any port you like


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # create a socket object
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        # bind the socket object to a specific address and port
        server_socket.bind((HOST, PORT))

        # listen for incoming connections
        server_socket.listen()

        print(f'Server listening on {HOST}:{PORT}')

        # accept connections from clients
        while True:
            client_socket, client_address = server_socket.accept()
            print(f'Connected by {client_address}')

            # receive data from the client and send it back
            with client_socket:
                while True:
                    data = client_socket.recv(1024)
                    print(f'{data}')
                    if not data:
                        break
                    string = f'Echo: ' + data.decode('utf-8')
                    bytes_obj = string.encode('utf-8')
                    client_socket.sendall(bytes_obj)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
