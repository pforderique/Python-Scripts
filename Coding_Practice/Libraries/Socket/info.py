'''
Socket Programming Tutorial
Tech with Tim

Piero Orderique
11 Feb 2021
'''

'''
Client Server Model

1 central processor - a server
several clients scattered all over

It would be a security risk to connect directly to another persons computer
Instead, we all connect to the Server
'''

'''
Local Area Network

internet-->Modem-->router(for wireless connections)
Modem is given a public IP address to communicate with internet
Router communicates with each device on network through local ip addresses
    Common local IP addresses: 192.168.1.xxx

So if I run server on device connected to router, only devices in LAN can connect
If its instead connected to modem, then all internet can see it 
'''