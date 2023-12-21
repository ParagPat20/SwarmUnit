import zmq
import time
import threading
import tkintermapview
import tkinter

MCU_host = '192.168.207.122'
CD1_host = '192.168.207.43'
CD2_host = '192.168.207.225'
cmd_port = 12345
ctrl_port = 54321
selected_drone = None
context = zmq.Context()  # Create a ZeroMQ context

connected_hosts = set()
clients = {}
pc = '192.168.207.101'
coordslat = 0.0
coordslon = 0.0
import random

def send(host, immediate_command_str):
    global connected_hosts
    global clients
    global context  # Use the global context
    try:
        if host not in connected_hosts:
            logger.log('New Host')
            # Remove the local redefinition of context
            socket1 = context.socket(zmq.PUSH)
            socket1.connect(f"tcp://{host}:12345")
            socket2 = context.socket(zmq.PUSH)
            socket2.connect(f"tcp://{host}:12345")
            socket3 = context.socket(zmq.PUSH)
            socket3.connect(f"tcp://{host}:12345")
            socket4 = context.socket(zmq.PUSH)
            socket4.connect(f"tcp://{host}:12345")
            socket5 = context.socket(zmq.PUSH)
            socket5.connect(f"tcp://{host}:12345")
            socket6 = context.socket(zmq.PUSH)
            socket6.connect(f"tcp://{host}:12345")
            clients[host] = [socket1, socket2, socket3, socket4, socket5, socket6]
            connected_hosts.add(host)
            logger.log("Clients {} ".format(clients))
        immediate_command_str = str(immediate_command_str)
        random_socket = random.choice(clients[host])
        random_socket.send_string(immediate_command_str)
        logger.log("Command sent successfuly")
    except Exception as e:
        logger.log(f"PC Host: {e}")

# def recv_status(remote_host, status_port, param=None):
#     client_socket = context.socket(zmq.REQ)  # Use REQ pattern for receiving status
#     client_socket.connect(f"tcp://{remote_host}:{status_port}")

#     try:
#         status_msg_str = client_socket.recv_string()
#         battery, gs, lat, lon, alt, heading = status_msg_str.split(',')
#         gs = gs[:6]

#         if param == 'battery':
#             return battery
#         elif param == 'gs':
#             return gs
#         else:
#             return status_msg_str
    
#     except zmq.error.ZMQError as error_msg:
#         logger.log(f'PC: {time.ctime()} - Caught exception : {error_msg}')
#         logger.log(f'PC: {time.ctime()} - CLIENT_request_status({remote_host}) is not executed!')
    

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

    def logger_server(self):
        context = zmq.Context()
        socket = context.socket(zmq.PULL)
        socket.bind("tcp://*:5556")  # The server binds to a specific address and port
        logger.log("Server Started")
        logger.log_sec("Security Server going ON!")
        def wifi_status_server():
            context = zmq.Context()
            server = context.socket(zmq.REP)
            server.bind('tcp://*:8888')

            while True:
                message = server.recv_string()
                response = "Connected"
                server.send_string(response)
        threading.Thread(target=wifi_status_server).start()
        try:
            while True:
                message = socket.recv_string()
                if message.startswith("sec "):
                    logger.log_sec(message[4:])
                elif message.startswith("lat "):
                    coordslat = message[4:]
                    coordslat = float(coordslat)
                    logger.log_sec(coordslat)
                elif message.startswith("lon "):
                    coordslon = float(message[4:])
                    logger.log_sec(coordslon)
                else:
                    logger.log(message)
        except KeyboardInterrupt:
            pass
        finally:
            socket.close()
            context.term()


logger = Logger()
class MapApplication():
    def __init__(self, root):
        #self.root = root
        global coordslat
        global coordslon
    
        self.map_widget = tkintermapview.TkinterMapView(root)
        self.map_widget.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        self.coords = (coordslat,coordslon)
        print(coordslat)
        print(coordslon)
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