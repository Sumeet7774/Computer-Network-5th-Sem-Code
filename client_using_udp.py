import socket

def start_udp_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = (socket.gethostname(), 4000)
    
    while True:
        # Take two numbers as input from the user
        num1 = input("Enter the first number: ")
        num2 = input("Enter the second number: ")
        
        if not num1 or not num2:
            break
        
        # Send the numbers to the server
        message = f"{num1},{num2}"
        client.sendto(message.encode('utf-8'), server_address)
        
        # Receive the result from the server
        result, _ = client.recvfrom(1024)
        print(f"Server result: {result.decode('utf-8')}")
    
    client.close()

if __name__ == '__main__':
    start_udp_client()