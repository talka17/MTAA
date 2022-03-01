import sipfullproxy
import time

def start_proxy():
    #get my ip address of proxy
    my_ip_add = sipfullproxy.socket.gethostbyname(sipfullproxy.socket.gethostname())
    #initialization of variables from library
    sipfullproxy.recordroute = "Record-Route: <sip:%s:%d;lr>" % (my_ip_add,sipfullproxy.PORT)
    sipfullproxy.topvia = "Via: SIP/2.0/UDP %s:%d" % (my_ip_add,sipfullproxy.PORT)
    #starting SIP proxy
    my_server = sipfullproxy.socketserver.UDPServer((sipfullproxy.HOST, sipfullproxy.PORT), sipfullproxy.UDPHandler)
    print("SIP Proxy is active. IP address:", my_ip_add)
    print("When you want to stop SIP Proxy, press Ctrl + C ")
    my_server.serve_forever()

if __name__ == "__main__":
    print("Proxy is starting...")
    time.sleep(2)
    start_proxy()
    