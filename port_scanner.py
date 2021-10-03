import sys
import socket
import logging


ipInput = input("Please insert Ip address:  ")
print("Ip recived %s , is this correct? press Y/N " %ipInput)
correct = input()

if correct.upper() == 'N':
    while correct.upper() == "N":
        ipInput = input("Please insert Ip address:  ")
        print("Ip recived %s , is this correct? press Y/N " %ipInput)
        correct = input()

if correct.upper() == 'Y':
    # creating a file to be filled with open ports
    with open('openPort.txt', 'w') as oPf:
        # creating a log file to be filled with errors
        #with open('errLog.txt', 'w')  as errLog:
            # Create and configure logger
            logging.basicConfig(filename="Error.log",
                                format='%(asctime)s %(message)s',
                                filemode='w')

            # Creating a logger object
            elog = logging.getLogger()

            # Setting the threshold of logger to ERROR
            elog.setLevel(logging.ERROR)

            try:
                #getting ip address ipv4 from string that represents ip.
                machineIp = socket.gethostbyname(ipInput)
                #check ports 1-65535
                for port in range(1, 65535):
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    result = sock.connect_ex((machineIp, port))
                    if result == 0:
                         print(("Port {}: 	 Open".format(port)))
                         oPf.write("Port {}: 	 Open \n".format(port))

                sock.close()


            #Exit the program option
            except KeyboardInterrupt:
                print("You pressed Ctrl+C")
                sys.exit()
            # Error handling
            except socket.gaierror as eg:
                sys.stdout.write("Error number: [%s] %s\n" %(eg.errno,eg.strerror))
                #logger Test messages
                elog.error("Error number: [%s] %s\n" %(eg.errno,eg.strerror))



            except socket.error as er:
                errLog.write("Error number: [%s]  %s\n" % (er.errno, er.strerror))
                sys.stdout.write("Error number: [%s] %s\n" % (er.errno, er.strerror))
                #logger Test messages
                elog.error("Error number: [%s] %s\n" % (er.errno, er.strerror))


else:
    print("Wrong input")
    sys.exit()



