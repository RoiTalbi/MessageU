
# ----------------------------------------------------------------
# Imports
# ----------------------------------------------------------------
import server
import logging
import sys

from errors import *

# ----------------------------------------------------------------
# Globals
# ----------------------------------------------------------------

PORT_INFO_FILE_PATH = 'port.info'


# ----------------------------------------------------------------
# Main
# ----------------------------------------------------------------

def main():

    port_num = 0

    # Open port info file 
    try:
        config_file = open(PORT_INFO_FILE_PATH, 'r')
        port_str = config_file.readline()
        port_num = int(port_str)

    except:
        logging.error("Could not open port.info file")
        sys.exit(SERVER_CONFIG_ERROR)


    # Create and run server on given port
    server_instance = server.Server(port_num)
    server_instance.run()



if __name__ == '__main__':
    main()


