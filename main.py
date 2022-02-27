import sipfullproxy

if __name__ == "__main__":    
    #sipfullproxy.logging.info(sipfullproxy.time.strftime("%a, %d %b %Y %H:%M:%S ", sipfullproxy.time.localtime()))
    #my_hostname = sipfullproxy.socket.gethostname()
    #sipfullproxy.logging.info(my_hostname)
    my_ip_add = sipfullproxy.socket.gethostbyname(sipfullproxy.socket.gethostname())
    #print(my_ip_add)
    #ipaddress = "192.168.56.1" #sipfullproxy.socket.gethostbyname(hostname)
    if my_ip_add == "127.0.0.1":
        my_ip_add = sipfullproxy.sys.argv[1]
    #sipfullproxy.logging.info(my_ip_add)
    sipfullproxy.recordroute = "Record-Route: <sip:%s:%d;lr>" % (my_ip_add,sipfullproxy.PORT)
    sipfullproxy.topvia = "Via: SIP/2.0/UDP %s:%d" % (my_ip_add,sipfullproxy.PORT)
    my_server = sipfullproxy.socketserver.UDPServer((sipfullproxy.HOST, sipfullproxy.PORT), sipfullproxy.UDPHandler)
    print("SIP Proxy is active")
    print("When you want to stop SIP Proxy, press Ctrl + C ")
    my_server.serve_forever()
    
    
#if __name__ == "__main__":    
#    logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s',filename='proxy.log',level=logging.INFO,datefmt='%H:%M:%S')
#    logging.info(time.strftime("%a, %d %b %Y %H:%M:%S ", time.localtime()))
#    hostname = socket.gethostname()
#    logging.info(hostname)
#    ipaddress = socket.gethostbyname(hostname)
#    if ipaddress == "127.0.0.1":
#        ipaddress = sys.argv[1]
#    logging.info(ipaddress)
#    recordroute = "Record-Route: <sip:%s:%d;lr>" % (ipaddress,PORT)
#    topvia = "Via: SIP/2.0/UDP %s:%d" % (ipaddress,PORT)
#    server = socketserver.UDPServer((HOST, PORT), UDPHandler)
#    server.serve_forever()