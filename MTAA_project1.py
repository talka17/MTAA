import sipfullproxy

if __name__ == "__main__":    
    sipfullproxy.logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s',filename='proxy.log',level=sipfullproxy.logging.INFO,datefmt='%H:%M:%S')
    sipfullproxy.logging.info(sipfullproxy.time.strftime("%a, %d %b %Y %H:%M:%S ", sipfullproxy.time.localtime()))
    my_hostname = sipfullproxy.socket.gethostname()
    sipfullproxy.logging.info(my_hostname)
    my_ip_add = sipfullproxy.socket.gethostbyname(sipfullproxy.socket.gethostname())
    print(my_ip_add)
    #ipaddress = "192.168.56.1" #sipfullproxy.socket.gethostbyname(hostname)
    #if ipaddress == "127.0.0.1":
    #    ipaddress = sipfullproxy.sys.argv[1]
    sipfullproxy.logging.info(my_ip_add)
    sipfullproxy.recordroute = "Record-Route: <sip:%s:%d;lr>" % (my_ip_add,sipfullproxy.PORT)
    sipfullproxy.topvia = "Via: SIP/2.0/UDP %s:%d" % (my_ip_add,sipfullproxy.PORT)
    my_server = sipfullproxy.socketserver.UDPServer((sipfullproxy.HOST, sipfullproxy.PORT), sipfullproxy.UDPHandler)
    print("Proxy is active")
    my_server.serve_forever()
    