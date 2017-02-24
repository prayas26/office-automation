import socket, select
from PyQt4 import QtCore, QtGui
import RPi.GPIO as GPIO
import time
import os
import csv


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False) # disable warnings

# GPIO pins setup
GPIO.setup(21, GPIO.OUT)
GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)

def light1on():
    GPIO.output(18,GPIO.HIGH)

def light2on():
    GPIO.output(14,GPIO.HIGH)

def light3on():
    GPIO.output(15,GPIO.HIGH)

def fan1on():
    GPIO.output(23,GPIO.HIGH)

def fan2on():
    GPIO.output(24,GPIO.HIGH)

def light1off():
    GPIO.output(18,GPIO.LOW)

def light2off():
    GPIO.output(14,GPIO.LOW)

def light3off():
    GPIO.output(15,GPIO.LOW)

def fan1off():
    GPIO.output(23,GPIO.LOW)

def fan2off():
    GPIO.output(24,GPIO.LOW)

# rewrite the last_log.txt with last status as LOCK
def last_log_lock():
    l = open("last_log.txt", 'w')
    log = "LOCK"
    l.write(log)
    l.close()

# rewrite the last_log.txt with last status as UNLOCK
def last_log_unlock():
    u = open("last_log.txt", 'w')
    log = 'UNLOCK'
    u.write(log)
    u.close()

# lock the door
def doorclose():
    o = open("last_log.txt", 'rw')
    x = o.read() # reads the text file
    if x == "LOCK":
        o.close() # no action if the last status is already LOCK
    elif x == "UNLOCK":
        o.close()
        p = GPIO.PWM(21, 65) # set the pulse to 65 at pin no. 21
        p.start(7.5)
        p.ChangeDutyCycle(12.5) # set the duty cycle of servo as 12.5
        time.sleep(0.4)
        p = GPIO.PWM(21, 90) # stop the 360 degree servo
        logs = []
        if os.access("lock_log.csv", os.F_OK):
            f = open("lock_log.csv", 'a')
            localtime = time.asctime( time.localtime(time.time()) )
            log = [localtime, 'LOCK']
            logs.append(log) # add the log entry into csv file
            for items in logs:
                    csv.writer(f).writerow(items)
            f.close()
        last_log_lock()
    else:
        o.close()

def dooropen():
    o = open("last_log.txt", 'rw')
    x = o.read() # reads the txt file
    if x == "UNLOCK":
        o.close() # no action if last status is already UNLOCK
    elif x == "LOCK":
        o.close()
        p = GPIO.PWM(21, 165) # set the pulse to 165 at pin no. 21
        p.start(7.5)
        p.ChangeDutyCycle(12.5) # set the duty cycle of servo as 12.5
        time.sleep(0.4)
        p = GPIO.PWM(21, 90) # stop the 360 degree serco
        logs = []
        if os.access("lock_log.csv", os.F_OK):
            f = open("lock_log.csv", 'a')
            localtime = time.asctime( time.localtime(time.time()) )
            log = [localtime, 'UNLOCK']
            logs.append(log) # add the log entry into the csv file
            for items in logs:
                csv.writer(f).writerow(items)
            f.close()
        last_log_unlock()
    else:
        o.close()


  
if __name__ == "__main__":
    
    CONNECTION_LIST = []    # list of socket clients
    RECV_BUFFER = 4096 # Advisable to keep it as an exponent of 2
    PORT = 1234 # empty port no. to allow connections
         
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(("192.168.0.2", PORT))
    server_socket.listen(10)
 
    CONNECTION_LIST.append(server_socket)
    data = '1'
    while True:
        while data !='':
            read_sockets,write_sockets,error_sockets = select.select(CONNECTION_LIST,[],[])
            for sock in read_sockets:
                if sock == server_socket:
                    sockfd, addr = server_socket.accept()
                    CONNECTION_LIST.append(sockfd)
                     
                else:
                    data = sock.recv(RECV_BUFFER) # recieve data
                    print str(data)
                    
                    if data == '1':
                        light1on()
                    elif data == '2':
                        light1off()
                    elif data == '3':
                        light2on()
                    elif data == '4':
                        light2off()
                    elif data == '5':
                        light3on()
                    elif data == '6':
                        light3off()
                    elif data == '7':
                        fan1on()
                    elif data == '8':
                        fan1off()
                    elif data == '9':
                        fan2on()
                    elif data == '0':
                        fan2off()
                    elif data == 'l':
                        doorclose()
                    elif data == 'u':
                        dooropen()
                    else:
                        pass
                        
                    
                    CONNECTION_LIST.remove(sock)
                break
    server_socket.close() # close socket connection
