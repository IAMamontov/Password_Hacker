import socket
def submit_data(data, client, address):
    client.connect(address)
    client.send(data.encode('utf-8'))
    client.close()
