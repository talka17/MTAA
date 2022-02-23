import sipfullproxy

if __name__ == "__main__":    
    #logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s',filename='proxy.log',level=logging.INFO,datefmt='%H:%M:%S')
    #logging.info(time.strftime("%a, %d %b %Y %H:%M:%S ", time.localtime()))
    hostname = sipfullproxy.socket.gethostname()
    #logging.info(hostname)
    ipaddress = sipfullproxy.socket.gethostbyname(hostname)
    if ipaddress == "127.0.0.1":
        ipaddress = sipfullproxy.sys.argv[1]
    sipfullproxy.logging.info(ipaddress)
    sipfullproxy.recordroute = "Record-Route: <sip:%s:%d;lr>" % (ipaddress,sipfullproxy.PORT)
    sipfullproxy.topvia = "Via: SIP/2.0/UDP %s:%d" % (ipaddress,sipfullproxy.PORT)
    server = sipfullproxy.socketserver.UDPServer((sipfullproxy.HOST, sipfullproxy.PORT), sipfullproxy.UDPHandler)
    print("Proxy is active")
    server.serve_forever()
