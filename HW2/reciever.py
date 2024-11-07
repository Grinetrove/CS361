import zmq

# Initialize a ZeroMQ context
context = zmq.Context()

# Create a reply socket
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")  # Bind to a port to receive messages

print("Waiting for message...")

# Receive the message
message = socket.recv_string()
print(f"Received message: {message}")

# Send a response back
response = "Message received"
socket.send_string(response)

# Clean up
socket.close()
context.term()