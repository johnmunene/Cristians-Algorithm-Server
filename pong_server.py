import socket

def sendPong():
  s=socket.socket() #create socket
  print("Socket succcesfully created")

  #Server port
  port = 7000
  s.bind(('',port))

  #Start listening to requests
  s.listen(5)
  print("Socket is listening....")

  # Pong server running forever
  while True:
    #Establish connection with client
    connection, address=s.accept()
    print('Socket connected to ', address)

    # receive message sent by client
    message =connection.recv(1024).decode()
    print(message)
    
    # check if message sent is 'ping' or not
    if message =='ping':
    # respond to the client with Pong if true
     connection.send(str('Pong').encode())
    # close connection with client
     connection.close()
     
    # if message is not 'ping' close the connection of the client
    else:
     connection.close()
# driver function
if __name__ == '__main__':

  # trigger server
  sendPong()
