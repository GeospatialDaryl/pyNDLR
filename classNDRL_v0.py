import serial
import time
import unicodedata

def remove_control_characters(s):
    # from https://stackoverflow.com/questions/4324790/removing-control-characters-from-a-string-in-python
    # ## Answer from Alex Quinn https://stackoverflow.com/users/500022/alex-quinn
    return "".join(ch for ch in s if unicodedata.category(ch)[0]!="C")


def serial_anticlobber(t = 0.11):
    time.sleep(t)


class sIO:

    outie = b'xx'
    
    def __init__(self,
                 strCOM = 'COM3',#):   # open sIO method
                 timeout = 0.01 ):
        
        self.sIO = serial.Serial(strCOM, timeout)
        print(self.sIO.name)

        # # #
        # local variables

        self._strBuff = []        #  buffer for string ops
        #
        # # #

        # init reporting
        self._ser_write(b'a')
        serial_anticlobber()
        self._ser_read()
        serial_anticlobber()
        
    def __enter__(self):
        return self

    # #
    
   
    # # 
    def _ser_read(self):
        self.waiting = self.sIO.in_waiting
        readBuf = self.sIO.read(self.waiting)
        print(type(readBuf))
        self._strBuff = readBuf.decode()
        #print(self._strBuff)
        print( readBuf.decode() )

    def _ser_write(self, strIn, fByte = True):
        # TODO fix the byte testing
        if fByte:
            self.sIO.write(strIn)
        else:
            self.sIO.write(byte( strIn) )
    

    # #  User methods
    def send(self, strIn):
        self._ser_read()
        serial_anticlobber()
        self._ser_write( strIn, fByte = True)
        serial_anticlobber()
        self._ser_read()

    def close(self):
        self.sIO.close()

    def __exit__(self):
        self.sIO.close()


def boolNDLRrecord(lineRecord):
    pass

class pyNuDLR:
    
    def __init__(self):
        self.sIO = sIO()
        self._listBuffer = []

    def a_pull_patterns(self):
        #self.sIO.sIO.write(b'<b>')
        self.sIO.send(b'<b>')
        self._listBuffer = []
        
        listPatterns = s.sIO._strBuff.split('\n')
        #print(type(listPatterns))
        
        for items in listPatterns:
            #print(len(items[0]))
            #print(items)
            try:
                if items[0] != '<':
                    pass
                else:
                    print(items)
                    self._listBuffer.append(items)
            except: pass
            #if items[0] == '<':
            #    print(items)
        #
#read(self.waiting)
    
s = pyNuDLR()
s.a_pull_patterns()
print("_________________")
#print(s.sIO._strBuff)
print( s._listBuffer)




#s = sIO()

#s._ser_write(b'a')
#s._ser_read()

