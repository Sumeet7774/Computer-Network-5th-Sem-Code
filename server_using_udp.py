import socket

def start_udp_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind((socket.gethostname(), 4000))
    print("UDP Server started and listening...")
    
    while True:
        # Receive the numbers from the client
        data, addr = server.recvfrom(1024)
        if not data:
            break
        
        # Decode and split the numbers
        numbers = data.decode('utf-8').split(',')
        num1, num2 = int(numbers[0]), int(numbers[1])
        
        # Perform the addition
        result = num1 + num2
        print(f"Received numbers {num1} and {num2} from {addr}, sending back result {result}")
        
        # Send the result back to the client
        server.sendto(str(result).encode('utf-8'), addr)

if __name__ == '__main__':
    start_udp_server()