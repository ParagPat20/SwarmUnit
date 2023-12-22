import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import zmq
import json
from saves import *

# Initialize the subplots
fig, axs = plt.subplots(3, 1, figsize=(8, 12))
fig.suptitle('Error and PID Plots')

# Create lines for each subplot (Error lines in blue, PID lines in red)
line_velx, = axs[0].plot([], [], label='Error velx', color='blue')
line_pid_velx, = axs[0].plot([], [], label='PID velx', color='red')

line_vely, = axs[1].plot([], [], label='Error vely', color='blue')
line_pid_vely, = axs[1].plot([], [], label='PID vely', color='red')

line_velz, = axs[2].plot([], [], label='Error velz', color='blue')
line_pid_velz, = axs[2].plot([], [], label='PID velz', color='red')

# Add legends to each subplot
axs[0].legend()
axs[1].legend()
axs[2].legend()

def update_plot(frame):
    # Update the plot with new error data
    error_data = subscriber.recv_json()
    timestamp = error_data.get("timestamp", 0)
    error_velx = error_data.get("error_velx", 0)
    error_vely = error_data.get("error_vely", 0)
    error_velz = error_data.get("error_velz", 0)
    pid_output_velx = error_data.get("pid_output_velx", 0)
    pid_output_vely = error_data.get("pid_output_vely", 0)
    pid_output_velz = error_data.get("pid_output_velz", 0)

    x_data = line_velx.get_xdata()
    y_data_velx = line_velx.get_ydata()
    y_data_vely = line_vely.get_ydata()
    y_data_velz = line_velz.get_ydata()
    
    # PID data
    y_data_pid_velx = line_pid_velx.get_ydata()
    y_data_pid_vely = line_pid_vely.get_ydata()
    y_data_pid_velz = line_pid_velz.get_ydata()

    x_data = list(x_data) + [timestamp]
    y_data_velx = list(y_data_velx) + [error_velx]
    y_data_vely = list(y_data_vely) + [error_vely]
    y_data_velz = list(y_data_velz) + [error_velz]
    
    # PID data
    y_data_pid_velx = list(y_data_pid_velx) + [pid_output_velx]
    y_data_pid_vely = list(y_data_pid_vely) + [pid_output_vely]
    y_data_pid_velz = list(y_data_pid_velz) + [pid_output_velz]

    line_velx.set_xdata(x_data)
    line_velx.set_ydata(y_data_velx)

    line_vely.set_xdata(x_data)
    line_vely.set_ydata(y_data_vely)

    line_velz.set_xdata(x_data)
    line_velz.set_ydata(y_data_velz)
    
    # PID data
    line_pid_velx.set_xdata(x_data)
    line_pid_velx.set_ydata(y_data_pid_velx)

    line_pid_vely.set_xdata(x_data)
    line_pid_vely.set_ydata(y_data_pid_vely)

    line_pid_velz.set_xdata(x_data)
    line_pid_velz.set_ydata(y_data_pid_velz)

    axs[0].relim()
    axs[0].autoscale_view()

    axs[1].relim()
    axs[1].autoscale_view()

    axs[2].relim()
    axs[2].autoscale_view()

# Set up the PyZMQ subscriber
context = zmq.Context()
subscriber = context.socket(zmq.SUB)
subscriber.connect("tcp://{}:5555".format(CD2_host))  # Update with your PUB socket address
subscriber.setsockopt_string(zmq.SUBSCRIBE, "")  # Subscribe to all topics

# Set up animation to update the plot
ani = FuncAnimation(fig, update_plot, interval=100, cache_frame_data=False, save_count=10)  # Update every second
plt.show()
