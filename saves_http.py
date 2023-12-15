import socket
import time
import threading
import tkinter
import tkintermapview
import flask

MCU_host = '192.168.207.122'
CD1_host = '192.168.207.43'
CD2_host = '192.168.207.225'
cmd_port = 12345
ctrl_port = 54321
selected_drone = None

def send(remote_host, immediate_command_str):
    global cmd_port
    # Create a socket object
    client_socket = socket.socket()
    client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    try:
        client_socket.connect((remote_host, cmd_port))
        client_socket.send(immediate_command_str.encode())
    
    except socket.error as error_msg:
        logger.log('PC: {} - Caught exception : {}'.format(time.ctime(), error_msg))
        logger.log('PC: {} - CLIENT_send_immediate_command({}, {}) is not executed!'.format(time.ctime(), remote_host, immediate_command_str))
        return
    finally:
        if client_socket:
            client_socket.close()


def recv_status(remote_host,status_port,param=None):
            client_socket = socket.socket()
            client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            try:
                client_socket.connect((remote_host, status_port))
                status_msg_str = client_socket.recv(1024).decode('utf-8')
                battery ,gs, lat, lon, alt, heading = status_msg_str.split(',')
                gs = gs[:6]
                if param == 'battery':
                    return battery
                elif param == 'gs':
                     return gs
                else:
                     return status_msg_str
                # logger.log("Trying")
            except socket.error as error_msg:
                logger.log('PC: {} - Caught exception : {}'.format(time.ctime(), error_msg))
                logger.log('PC: {} - CLIENT_request_status({}) is not executed!'.format(time.ctime(), remote_host))

            finally:
                if client_socket:
                    client_socket.close()
                
                
def send_ctrl(cmd):
    global selected_drone
    Velocity = 0.5
    x = '0'
    y = '0'
    z = '0'
    if cmd == 'w':
        x = str(Velocity)
    elif cmd == 's':
        x = str(-Velocity)
    if cmd == 'a':
        y = str(Velocity)
    elif cmd == 'd':
        y = str(-Velocity)
    if cmd == 'u':
        z = str(-Velocity)
    elif cmd == 'j':
        z = str(Velocity)

    logger.log("Selected_Drone is : {}".format(selected_drone))

    if selected_drone == 'MCU' or selected_drone == 'ALL':
        send(MCU_host, 'MCU.send_ned_velocity('+x+','+y+','+z+')')
    if selected_drone == 'CD1' or selected_drone == 'ALL':
        send(CD1_host,'CD1.send_ned_velocity('+x+','+y+','+z+')')
    if selected_drone == 'CD2' or selected_drone == 'ALL':
        send(CD2_host,'CD2.send_ned_velocity('+x+','+y+','+z+')')


    logger.log("Sending ned velocity to {}\n X={}, Y={}, Z={}".format(selected_drone,x,y,z))

            
def ctrlON(root):
    root.bind('w', lambda event: send_ctrl('w'))
    root.bind('a', lambda event: send_ctrl('a'))
    root.bind('d', lambda event: send_ctrl('d'))
    root.bind('u', lambda event: send_ctrl('u'))
    root.bind('j', lambda event: send_ctrl('j'))
    root.bind('s', lambda event: send_ctrl('s'))
    logger.log("CONTROL ON {}".format(selected_drone))

def ctrlOFF(root):
    root.unbind('w')
    root.unbind('a')
    root.unbind('d')
    root.unbind('u')
    root.unbind('j')
    root.unbind('s')
    logger.log("CONTROL OFF")

def select_drone(string):
    global selected_drone
    selected_drone = string
    logger.log(selected_drone)

def ARM(mode):
    if selected_drone == 'MCU' or selected_drone == 'ALL':
        send(MCU_host,'MCU.arm('+'"'+str(mode)+'"'+')')
    if selected_drone == 'CD1' or selected_drone == 'ALL':
        send(CD1_host,'CD1.arm(''"'+str(mode)+'"'')')
    if selected_drone == 'CD2' or selected_drone == 'ALL':
        send(CD2_host,'CD2.arm(''"'+str(mode)+'"'')')

    logger.log("Arming {} in {} mode)'".format(selected_drone,mode))


def RTL():
    if selected_drone == 'MCU' or selected_drone == 'ALL':
        send(MCU_host,'MCU.rtl()')
    if selected_drone == 'CD1' or selected_drone == 'ALL':
        send(CD1_host,'CD1.rtl()')
    if selected_drone == 'CD2' or selected_drone == 'ALL':
        send(CD2_host,'CD2.rtl()')

    logger.log("RTL to {}".format(selected_drone))

def POSHOLD():
    if selected_drone == 'MCU' or selected_drone == 'ALL':
        send(MCU_host,'MCU.poshold()')
    if selected_drone == 'CD2' or selected_drone == 'ALL':
        send(CD2_host,'CD2.poshold()')
    if selected_drone == 'CD1' or selected_drone == 'ALL':
        send(CD1_host,'CD1.poshold()')

    logger.log("POSHOLD {}".format(selected_drone))
    
def TAKEOFF():
    if selected_drone == 'MCU' or selected_drone == 'ALL':
        send(MCU_host,'MCU.takeoff()')
    if selected_drone == 'CD2' or selected_drone == 'ALL':
        send(CD2_host,'CD2.takeoff()')
    if selected_drone == 'CD1' or selected_drone == 'ALL':
        send(CD1_host,'CD1.takeoff()')

    logger.log("TakeOFF {}".format(selected_drone))

def LAND():
    if selected_drone == 'MCU' or selected_drone == 'ALL':
        send(MCU_host,'MCU.land()')
    if selected_drone == 'CD2' or selected_drone == 'ALL':
        send(CD2_host,'CD2.land()')
    if selected_drone == 'CD1' or selected_drone == 'ALL':
        send(CD1_host,'CD1.land()')

    logger.log("LANDING {}".format(selected_drone))

class Logger:
    def __init__(self):
        self.log_text = None
        self.mcu_status = False
        self.cd1_status = False
        self.cd2_status = False

    def set_log_text(self, log_text):
        self.log_text = log_text

    def log(self, message,foreground = "#5E95FF"):
        if self.log_text:
            self.log_text.configure(state="normal", font=("Montserrat Bold", 20 * -1), foreground=foreground)
            message = str(message)
            self.log_text.insert("end", message + "\n")
            self.log_text.configure(state="disabled")
            self.log_text.see("end")

    def log_server(self):

        def handle_client():
            while True:
                try:
                    client_connection, client_address = msg_socket.accept()
                    print("received log {}".format(client_address))
                    data = client_connection.recv(1024).decode()
                    data = str(data)
                    if data == 'mcu_status':
                        self.mcu_status = True
                    if data == 'cd1_status':
                        self.cd1_status = True
                    if data == 'cd2_status':
                        self.cd2_status = True
                    self.log("{} from {}".format(data, client_address))
                    client_connection.close()

                except Exception as e:
                    self.log('PC: log Error: {}'.format(e))
            

        msg_socket = socket.socket()
        msg_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        msg_socket.bind(('192.168.207.101',60123))
        msg_socket.listen(5)

        self.log('PC: {} - log_server() is started!'.format(time.ctime()))
        threading.Thread(target=handle_client).start()

logger = Logger()


