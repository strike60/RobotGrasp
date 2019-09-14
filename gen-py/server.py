# coding: utf-8
"""
thrift_client.py
"""
import socket
import sys
from inference import Inference
from inference.ttypes import *

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer


class InferenceHandler:
    def sendPhoto(self, picture):
        ret = [0., 0., 0., 0., 0., 0.]
        return ret


handler = InferenceHandler()
processor = Inference.Processor(handler)
transport = TSocket.TServerSocket("localhost", 9090)
tfactory = TTransport.TBufferedTransportFactory()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

print ("Starting thrift server in python...")
server.serve()
print ("done!")
