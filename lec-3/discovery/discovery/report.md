
# Server

$ python DiscoveryServer.py 8181
Ready to serve... Port: 8181
Accepted connection from client ('127.0.0.1', 56292)
Send Response:Success
Ready to serve... Port: 8181
Accepted connection from client ('127.0.0.1', 56293)
Send Response:127.0.0.1 15535
Ready to serve... Port: 8181
Accepted connection from client ('127.0.0.1', 56295)
Send Response:127.0.0.1 15535
Ready to serve... Port: 8181
Accepted connection from client ('127.0.0.1', 56296)
Send Response:Success
Ready to serve... Port: 8181
Accepted connection from client ('127.0.0.1', 56297)
Send Response:127.0.0.1 15535
Ready to serve... Port: 8181
Accepted connection from client ('127.0.0.1', 56298)
Send Response:Success
Ready to serve... Port: 8181
Accepted connection from client ('127.0.0.1', 56299)
Send Response:127.0.0.1 4553
Ready to serve... Port: 8181
Accepted connection from client ('127.0.0.1', 56300)
Send Response:Success
Ready to serve... Port: 8181
Accepted connection from client ('127.0.0.1', 56301)
Send Response:None
Ready to serve... Port: 8181

# Telnet

$ telnet localhost 8181
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
add g kg 127.0.0.1 15535
Success
Connection closed by foreign host.
$ telnet localhost 8181
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
lookup g kg
127.0.0.1 15535
Connection closed by foreign host.
$ telnet localhost 8181
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
lookup kg g
127.0.0.1 15535
Connection closed by foreign host.
$ telnet localhost 8181
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
add g kg 127.0.0.1 4553
Success
Connection closed by foreign host.
$ telnet localhost 8181
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
lookup g kg
127.0.0.1 15535
Connection closed by foreign host.
$ telnet localhost 8181
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
remove 127.0.0.1 15535
Success
Connection closed by foreign host.
$ telnet localhost 8181
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
lookup g kg
127.0.0.1 4553
Connection closed by foreign host.
$ telnet localhost 8181
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
remove 127.0.0.1 4553
Success
Connection closed by foreign host.
$ telnet localhost 8181
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
lookup kg g
None

