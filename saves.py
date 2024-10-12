import zmq
import time
import threading
import tkintermapview
import tkinter
import logging


MCU_host = '192.168.207.122'
CD1_host = '192.168.207.43'
CD2_host = '192.168.207.225'
CD3_host = CD2_host

cmd_port = 12345
ctrl_port = 54321
selected_drone = None
context = zmq.Context()  # Create a ZeroMQ context
poller = zmq.Poller
connected_hosts = set()
clients = {}
pc = '192.168.207.101'
coordslat = 22.2868240
coordslon = 73.3639982
cap = None
import random

def send(host, immediate_command_str):
    global connected_hosts
    global clients

    try:
        if host not in connected_hosts:
            connect_and_register_socket(host)

            immediate_command_str = str(immediate_command_str)

        clients[host].send(immediate_command_str.encode(), zmq.NOBLOCK)  # Non-blocking send
        logger.log("Command sent successfully to {}".format(host))

    except zmq.error.Again:  # Handle non-blocking send errors
        poller.register(clients[host], zmq.POLLOUT)  # Wait for socket readiness
        socks = dict(poller.poll(1000))
        if clients[host] in socks and socks[clients[host]] == zmq.POLLOUT:
            clients[host].send_string(immediate_command_str)  # Retry sending
        else:
            logger.log("Socket not ready for {}, reconnecting...".format(host))
            reconnect_socket(host)

    except zmq.error.ZMQError as e:
        logger.log("PC Host {host}: {}".format(e))
        reconnect_socket(host)  # Attempt reconnection

def connect_and_register_socket(host):
    socket = context.socket(zmq.PUSH)
    socket.setsockopt(zmq.SNDHWM, 1000)  # Allow up to 1000 queued messages
    socket.connect(f"tcp://{host}:12345")
    clients[host] = socket
    connected_hosts.add(host)
    logger.log("Clients: {}".format(clients))

def reconnect_socket(host):
    socket = clients[host]
    socket.close()
    socket = context.socket(zmq.PUSH)
    socket.connect(f"tcp://{host}:12345")
    clients[host] = socket
    socks = dict(poller.poll(1000))  # Wait for write events with timeout


def recv_status(remote_host,status_port, param=None):
    logger.log("just chilling")
                
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
        z = str(-0.2)
    elif cmd == 'j':
        z = str(0.2)

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

def servo_set(cmd):
    global selected_drone
    if selected_drone == 'MCU':
        send(MCU_host,'MCU.servo('+'"'+str(cmd)+'"'+')')
    if selected_drone == 'CD1':
        send(CD1_host,'CD1.servo('+'"'+str(cmd)+'"'+')')
    if selected_drone == 'CD2':
        send(CD2_host,'CD2.servo('+'"'+str(cmd)+'"'+')')
    logger.log("Sending Servo condition {} to {}".format(selected_drone,cmd))

def ARM(mode):
    if selected_drone == 'MCU' or selected_drone == 'ALL':
        send(MCU_host,'MCU.arm('+'"'+str(mode)+'"'+')')
    if selected_drone == 'CD1' or selected_drone == 'ALL':
        send(CD1_host,'CD1.arm(''"'+str(mode)+'"'')')
    if selected_drone == 'CD2' or selected_drone == 'ALL':
        send(CD2_host,'CD2.arm(''"'+str(mode)+'"'')')

    logger.log("Arming {} in {} mode".format(selected_drone,mode))


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
        self.log_text_sec = None
        self.mcu_status = False
        self.cd1_status = False
        self.cd2_status = False
        self.log_thread = None
        self.context = zmq.Context()
        self.router_socket = self.context.socket(zmq.ROUTER)

    def set_log_text(self, log_text):
        self.log_text = log_text

    def log(self, message):
        if self.log_text:
            self.log_text.configure(state="normal", font=("Montserrat Bold", 15 * -1), foreground="#5E95FF")
            message = str(message)
            self.log_text.insert("end", message + "\n")
            self.log_text.configure(state="disabled")
            self.log_text.see("end")

    def set_log_text_sec(self, log_text):
        self.log_text_sec = log_text

    def log_sec(self, message):
        if self.log_text_sec:
            self.log_text_sec.configure(state="normal", font=("Montserrat Bold", 15 * -1), foreground="#FF0000")
            message = str(message)
            self.log_text_sec.insert("end", message + "\n")
            self.log_text_sec.configure(state="disabled")
            self.log_text_sec.see("end")

    def start_logging(self):
        try:
            self.log("LOGGING SERVER STARTED!")
            self.log_sec("WAITING FOR SECURITY PARAMS!!!")
            self.log_thread = threading.Thread(target=self.handle_messages)
            self.log_thread.start()
            self.router_socket.bind("tcp://*:5556")
            socket = context.socket(zmq.REP)  # REP socket for responding to clients
            socket.bind("tcp://*:8888")  # Bind to port 8888 (matching client configuration)
            while True:
                message = socket.recv()  # Receive request from client
                try:
                    socket.send_string("Connected")  # Send response to client
                except Exception as e:
                    print(f"Error checking Wi-Fi: {e}")
                    socket.send_string("Error")  # Notify client of an error
        except zmq.ZMQError as e:
            logging.error("Error connecting to server: %s", e)

    def handle_messages(self):
        while True:
            try:
                message = self.router_socket.recv_multipart()
                message = message[1].decode()
                message = str(message)
                try:
                    # Process messages appropriately
                    if message.startswith("sec "):
                        self.log_sec(message[4:])
                    elif message.startswith("lat "):
                        coordslat = float(message[4:])
                        self.log_sec(coordslat)
                    elif message.startswith("lon "):
                        coordslon = float(message[4:])
                        self.log_sec(coordslon)
                    else:
                        self.log(message)
                except Exception as e:
                    logging.error("Error processing message: %s", e)
            except zmq.ZMQError as e:
                if e.errno != zmq.ETERM:
                    logging.error("Error receiving message: %s", e)

  
logger = Logger()
def start_logging_in_background():
    logger.start_logging()


class MapApplication():
    def __init__(self, root):
        #self.root = root
        global coordslat
        global coordslon
    
        self.map_widget = tkintermapview.TkinterMapView(root)
        self.map_widget.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        self.coords = (coordslat,coordslon)
        logger.log_sec(str(self.coords))
        self.map_widget.set_position(self.coords[0], self.coords[1])
        self.map_widget.set_zoom(15)
        
        given_coordinates = [
        {"coords": self.coords, "label": "Drone 1"}
        ]

        # Function to add marker to the map at given coordinates with labels
        def add_given_markers():
            for data in given_coordinates:
                coords = data["coords"]
                label = data["label"]
                self.map_widget.set_marker(coords[0], coords[1], text=label)
                print(coords)

        # Adding right-click event to the map
        self.map_widget.add_right_click_menu_command(label="Add Given Markers",
                                        command=add_given_markers)



        #clear_button = tkinter.Button(root, text="Clear Markers", command=self.clear_markers)
        #clear_button.pack()
