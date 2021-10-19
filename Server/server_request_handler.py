# ----------------------------------------------------------------
# Imports
# ----------------------------------------------------------------
from errors import *
from globals import *
from server_codes import *

import logging
import sys


# ----------------------------------------------------------------
# Globals
# ----------------------------------------------------------------



# ----------------------------------------------------------------
# Request Handlers
# ----------------------------------------------------------------


class ServerRequestsHandler():

    def handle_request(request):

        # Invoke matching handler function by using request code
        handler_function = REQUEST_HANDLERS[1000]
        handler_function(request)

    def _request_register(request):
        print("REGISTER4!!!!");
        pass

    def _request_get_clients_list(request):
        pass

    def _request_get_client_public_key(request):
        pass

    def _request_send_message(request):
        pass

    def _request_get_pending_messages(request):
        pass





# ----------------------------------------------------------------
# Request Handlers Map
# ----------------------------------------------------------------

REQUEST_HANDLERS = {
OPCODE_REGISTER : ServerRequestsHandler._request_register,                           \
OPCODE_GET_CLIENTS_LIST : ServerRequestsHandler._request_get_clients_list,           \
OPCODE_GET_CLIENT_PUBLIC_KEY : ServerRequestsHandler._request_get_client_public_key, \
OPCODE_SEND_MESSAGE : ServerRequestsHandler._request_send_message,                   \
OPCODE_GET_PENDING_MESSAGES : ServerRequestsHandler._request_get_pending_messages  }










