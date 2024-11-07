import zmq
import time

# Initialize a ZeroMQ context
context = zmq.Context()

# Create a request socket
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")  # Connect to the receiver's address

# Message to send
message = "This is a message from CS361"
print(f"Sending message: {message}")

# Send the message
socket.send_string(message)

# Wait for the response
response = socket.recv_string()
print(f"Received response: {response}")

# Clean up
socket.close()
context.term()

