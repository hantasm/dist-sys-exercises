
# Add

Request:
ADD UNIT1 UNIT2 IP_ADDRESS PORT_NO\n

Response:
SUCCESS\n
FAILURE [REASON]\n -> FAILURE\n
Ex:
FAILURE EXISTS

-------------------------------

# Remove

Request:
REMOVE IP_ADDRESS PORT_NO\n
Remove all entries with IP:PORT

Response:
SUCCESS\n
FAILURE [REASON]\n -> FAILURE\n

-------------------------------

# Lookup

Request:
LOOKUP UNIT1 UNIT2\n

Response:
in case of Success:
IP_ADDRESS PORT_NO\n
-> none\n
failure:
FAILURE

-------------------------------

# Clarify
All request and responses are case-insensitive.

