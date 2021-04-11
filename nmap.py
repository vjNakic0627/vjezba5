'''import socket

target = input('Enter the host to be scanned: ')
t_IP = socket.gethostbyname(target)
print ('Starting scan on host: ', t_IP)
   
for i in range(1500, 15000):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      
    conn = s.connect((t_IP, i))
    if(conn == 0) :
        print ('Port open ', i)
    else:
        print('Port closed ', i)
    s.close()'''


import socket

t_host = input('Enter the host to be scanned: ')
t_ip = socket.gethostbyname(t_host)

print (t_ip)

while 1:
	t_port = input('Enter the port: ')
	
	try:
		sock = socket.socket()			
		res = sock.connect((t_ip, t_port))
		print ("port oopen ", t_port)
		sock.close()
	except:
		print ("port closed ", t_port)
	
print ("Port Scanning complete")