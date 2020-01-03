import serial
import time
import unicodedata

def remove_control_characters(s):
    # from https://stackoverflow.com/questions/4324790/removing-control-characters-from-a-string-in-python
    # ## Answer from Alex Quinn https://stackoverflow.com/users/500022/alex-quinn
    return "".join(ch for ch in s if unicodedata.category(ch)[0]!="C")



class sIO:

    outie = b'xx'
    
    def __init__(self,
                 strCOM = 'COM3',#):   # open sIO method
                 timeout = 0.01 ):
        
        self.sIO = serial.Serial(strCOM, timeout)
        print(self.sIO.name)
        self._ser_write(b'a')
        time.sleep(0.01)
        self._ser_read()
        time.sleep(0.01)
        #self.cmd('a')
        
    def __enter__(self):
        return self

    # #
    def _ser_read(self):
        self.waiting = self.sIO.in_waiting
        print( self.sIO.read(self.waiting) )

    def _ser_write(self, strIn, fByte = True):
        if fByte:
            self.sIO.write(strIn)
        else:
            self.sIO.write(byte( strIn) )
    

    # #  User methods
    def make_action(self, strIn):
        self._ser_read()
        time.sleep(0.01)
        self._ser_write( strIn, fByte = True)
        time.sleep(0.01)
        self._ser_read()



    def close(self):
        self.sIO.close()

    def __exit__(self):
        self.sIO.close()


s = sIO()

s._ser_write(b'a')
s._ser_read()

