#!/usr/bin/env python

#******************************************************************************
#
#  CS 6421 - Discovery Server
#  Execution:    python DiscoveryServer.py portnum
#
#******************************************************************************

import socket
import sys

#******************************************************************************
#   Discovery Server
#******************************************************************************

class DiscoveryServer(object):

    def __init__(self):
        # Initial Server
        self.serverList = dict()
        self.unitList = dict()

    #******************************************************************************
    #   Function to process requests
    #******************************************************************************
    def processRequest(self, conn):
        # Read userInput from client
        userInput = conn.recv(BUFFER_SIZE)
        userInputs = userInput.strip().split(' ')

        command = userInputs[0].lower()
        res = ''
        if command == 'add':
            if len(userInputs) != 5:
                res = 'Failure Argument'
            else:
                res = self.addConv(userInputs[1], userInputs[2], userInputs[3], userInputs[4])
        elif command == 'remove':
            if len(userInputs) != 3:
                res = 'Failure Argument'
            else:
                res = self.removeConv(userInputs[1], userInputs[2])
        elif command == 'lookup':
            if len(userInputs) != 3:
                res = 'Failure Argument'
            else:
                res = self.lookupConv(userInputs[1], userInputs[2])
        else:
            res = 'Failure Unknown'

        print('Send Response:' + res)
        conn.send(res + '\n')
        # Close connection
        conn.close()

    def addConv(self, unit1, unit2, ip, port):
        conv1 = unit1 + ' ' + unit2
        conv2 = unit2 + ' ' + unit1
        server = ip + ' ' + port
        if server in self.serverList:
            if conv1 in self.serverList[server]:
               return 'Failure Exists'
        else:
            self.serverList[server] = set()
        self.serverList[server].add(conv1)
        self.serverList[server].add(conv2)
        if conv1 in self.unitList:
            self.unitList[conv1].append(server)
        else:
            self.unitList[conv1] = [server]
        if conv2 in self.unitList:
            self.unitList[conv2].append(server)
        else:
            self.unitList[conv2] = [server]
        return 'Success'

    def removeConv(self, ip, port):
        server = ip + ' ' + port
        if server not in self.serverList:
            return 'Failure Already Removed'
        for conv in self.serverList[server]:
            pre = self.unitList[conv]
            curr = []
            for pserver in pre:
                if pserver != server:
                    curr.append(pserver)
            if curr:
                self.unitList[conv] = curr
            else:
                del self.unitList[conv]
        del self.serverList[server]
        return 'Success'

    def lookupConv(self, unit1, unit2):
        conv = unit1 + ' ' + unit2
        if conv in self.unitList:
            return self.unitList[conv][0]
        conv = unit2 + ' ' + unit1
        if conv in self.unitList:
            return self.unitList[conv][0]
        return 'None'

#******************************************************************************
#   Main code run when program is started
#******************************************************************************
if __name__ == "__main__":
    
    BUFFER_SIZE = 1024
    interface = ""

    # If input arguments are wrong, print out usage
    if len(sys.argv) != 2:
        print >> sys.stderr, "usage: python {0} portnum\n".format(sys.argv[0])
        sys.exit(1)
    else:
        portnum = int(sys.argv[1])

    # Create socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((interface, portnum))
    s.listen(5)

    # Create Server
    server = DiscoveryServer()

    # Server should be up and running and listening to the incoming connections
    while True:
        print 'Ready to serve... Port:', portnum
        # Set up a new connection from the client
        conn, addr = s.accept()
        # If an exception occurs during the execution of try clause
        # the rest of the clause is skipped
        # If the exception type matches the word after except
        # the except clause is executed
        try:
            # Receives the request message from the client
            print 'Accepted connection from client', addr
            # Process the connection
            server.processRequest(conn)
        except KeyboardInterrupt:
            conn.close()
        except IOError:
            # Close the client connection socket
            conn.close()

    # Close the Server connection socket
    s.close()

    # Exit
    sys.exit(0)

