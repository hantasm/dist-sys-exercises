#!/usr/bin/env python

#******************************************************************************
#
#  CS 6421 - Simple Conversation
#  Execution:    python convServer.py portnum
#
#******************************************************************************

import socket
import sys

## Function to process requests
def process(conn):
    #conn.send("Welcome to banana's potassium calculater. Please send the number of bananas.\n")

    # read userInput from client
    userInput = conn.recv(BUFFER_SIZE)

    response = ''
    if not userInput:
        print "Error reading message"
        return

    userInputs = userInput.split(' ')

    if len(userInputs) != 3:
	response = "Invalid Data"
    else:
        inputNum = userInputs[2]
        if not inputNum.isdigit():
	    response = "Invalid Number"
        else:
    	    num = int(inputNum)
	    response = str(0.442 * num)

    conn.send(response)

    conn.close()


### Main code run when program is started
BUFFER_SIZE = 1024
interface = ""

# if input arguments are wrong, print out usage
if len(sys.argv) != 2:
    print >> sys.stderr, "usage: python {0} portnum\n".format(sys.argv[0])
    sys.exit(1)

portnum = int(sys.argv[1])

# create socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((interface, portnum))
s.listen(5)

while True:
    # accept connection and print out info of client
    conn, addr = s.accept()
    print 'Accepted connection from client', addr
    process(conn)
s.close()
