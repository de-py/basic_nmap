import socket
import ipaddress

start = input("Enter beginning of IP range: ")
end = input("Enter end of IP range: ")

start_ip = ipaddress.ip_address(start)
end_ip = ipaddress.ip_address(end)

start_port = int(input("Enter the beginning Port: "))
end_port = int(input("Enter the ending Port: "))
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

i = int(start_ip)
while i < int(end_ip):
    ip = str(ipaddress.ip_address(i))
    print(ip)
    for port in range(start_port, end_port + 1):
        print(port)
        # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if s.connect_ex((ip, port)):
            print(ip + ": Port " + str(port) + " closed")
        else:
             print(ip + ": Port" + str(port) + " open")
    i+=1