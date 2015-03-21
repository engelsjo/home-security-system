'''
This python module will be the webserver handling communication from the Arduino's
to the mobile devices.

@author: Joshua Engelsma
@date: 03/21/2015
'''

import socket

class WebServer:

	def __init__(self, ip='', port=8080):
		#set up a udp socket
		self.ip_addr = ip #IN_ADDR by default
		self.port = port
		self.socket = socket.socket(socket.AF_NET, socket.SOCK_DGRAM)
		self.socket.bind((self.ip_addr, self.port))

	def Serve():
		serving = True
		while serving:
			#handle web requests
			try:
				data, client_addr = self.socket.recfrom(self.port)
			except KeyboardInterrupt:
				running = False
				break;
			except Exception as e:
				print("Exception serving: ")
				print (e)

def __main__():
	web_server = WebServer()
	web_server.serve()



