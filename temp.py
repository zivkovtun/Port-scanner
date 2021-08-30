import sys
import socket

ipInput = input("Please insert Ip address:  ")
print("Ip recived %s , is this correct? press Y/N " %ipInput)
correct = input()

if correct.upper() == 'N':
    while correct.upper() == "N":
        ipInput = input("Please insert Ip address:  ")
        print("Ip recived %s , is this correct? press Y/N " %ipInput)
        correct = input()
if correct.upper() == 'Y':
    machineIp = socket.gethostbyname(ipInput)

    # creating an open port file to fill
    with open('openPort.txt', 'w') as oPf:
        with open('errLog.txt', 'w')  as errLog:
            try:
            #check ports 1-65535
                for port in range(1, 1000):
                 sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                 result = sock.connect_ex((machineIp, port))
                 if result == 0:
                    print(("Port {}: 	 Open".format(port)))
                    oPf.write("Port {}: 	 Open \n".format(port))
                 sock.close()

            except KeyboardInterrupt:
                print("You pressed Ctrl+C")
                sys.exit()

            except socket.gaierror:
                errLog.write("%d , %s",socket.gaierror)
                #print('Hostname could not be resolved. Exiting')
                #sys.exit()

            except socket.error:
                 errLog.write("%d , %s", socket.error)
                 #print("Couldn't connect to server")
                 #sys.exit()


else:
    print("Wrong input")
    sys.exit()



