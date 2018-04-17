class Packet:

    def __init__(self, time_stamp, source, destination):
        self.__time_stamp = time_stamp
        self.__source = source
        self.__destination = destination

    def getTimeStamp(self):
        # get packet time stamp
        return self.__time_stamp

    def getSource(self):
        # get packet source
        return self.__source

    def getDestination(self):
        # get packet destination
        return self.__destination

class RouteRequest(Packet):
    
    def __init__(self, time_stamp, source, destination):
        Packet.__init__(self, time_stamp, source, destination)
        self.__type = 'RouteRequest'
        self.__path = []

    def getType(self):
        return self.__type
    
    def addToPath(self, node):
        self.__path.append(node)
        
    def getPath(self):
        return self.__path
        
class RouteReply(Packet):
    
    def __init__(self, time_stamp, source, destination, path):
        Packet.__init__(self, time_stamp, source, destination)
        self.__type = 'RouteReply'
        self.__path = path
        self.__retransmits = 0 # number of times this packet has been retransmitted

    def getType(self):
        return self.__type
    
    def setPath(self, path):
        self.__path = path
        
    def getPath(self):
        return self.__path
    
    def returnRetransmits(self):
        return self.__retransmits