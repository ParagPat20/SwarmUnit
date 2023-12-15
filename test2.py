import socket
import time
def log(msg):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cli:
            cli.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            try:
                cli.connect(('192.168.170.101',61234))
                msg = str(msg)
                cli.send(msg.encode())
                print('Message sent')
                cli.close()
            except Exception as e:
                raise ConnectionError("Error connecting to the server: " + str(e))
    except Exception as e:
        raise Exception("Error in log function: " + str(e))

while True:
    time.sleep(0.1)
    log("hello")