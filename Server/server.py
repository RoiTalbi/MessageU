
# ----------------------------------------------------------------
# Imports
# ----------------------------------------------------------------
from errors import *
from globals import *
from server_codes import *

from server_request_handler import ServerRequestsHandler 
import logging
import sys
import selectors
import socket



# ----------------------------------------------------------------
# Globals
# ----------------------------------------------------------------

OPCODE_REGISTER = 1000
OPCODE_GET_CLIENTS_LIST = 1001
OPCODE_GET_CLIENT_PUBLIC_KEY = 1002
OPCODE_SEND_MESSAGE = 1003
OPCODE_GET_PENDING_MESSAGES = 1004


SERVER_MAXIMUM_CLIENTS = 100



# ----------------------------------------------------------------
# Classes
# ----------------------------------------------------------------


class Server():

    def parse_request(data):

        # Parse request using struct

        # Handle request
        ServerRequestsHandler.handle_request(None);


    def accept(sock, mask):
        conn, addr = sock.accept()  # Should be ready
        print('accepted', conn, 'from', addr)
        conn.setblocking(False)
        Server.selector.register(conn, selectors.EVENT_READ, Server.read)


    def read(connection, mask):
        data = connection.recv(SERVER_PACKET_SIZE)

        if data:
            print('Handling request - ', repr(data), 'from', connection)
            Server.parse_request(data)
            
        else:
            print('closing', connection)
            sel.unregister(connection)
            connection.close()


    def start_server(port_num):
        print(f"Start server on {port_num}")

        Server.selector = selectors.DefaultSelector()

        server_socket = socket.socket()
        server_socket.bind(('localhost', port_num))
        server_socket.listen(SERVER_MAXIMUM_CLIENTS)
        server_socket.setblocking(False)
        Server.selector.register(server_socket, selectors.EVENT_READ, Server.accept)  

        while True:
            events = Server.selector.select()
            for key, mask in events:
                callback = key.data
                callback(key.fileobj, mask)






