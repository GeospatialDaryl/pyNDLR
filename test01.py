import serial
import unicodedata

def remove_control_characters(s):
    # from https://stackoverflow.com/questions/4324790/removing-control-characters-from-a-string-in-python
    # ## Answer from Alex Quinn https://stackoverflow.com/users/500022/alex-quinn
    return "".join(ch for ch in s if unicodedata.category(ch)[0]!="C")


#s = serial.Serial('COM3', timeout = 0)#.001 )  # open serial port
#print(s.name)         # check which port was really used
#outie = b'xx'

#s.write(b'a')

#while outie != b'':
 #   outie = s.readline()
#    print(outie)

stateOBJ = {}



class sIO:

    outie = b'xx'
    
    def __init__(self,
                 strCOM = 'COM3',#):   # open sIO method
                 timeout = 0.01 ):
        
        self.sIO = serial.Serial(strCOM, timeout)
        print(self.sIO.name)
        #self.cmd('a')

    def __enter__(self):
        return self

    def raw_poll(self, strPoll):
        pass


    def cmd(self, inStr):
        flagOut = b'xx'
        inStr = str.encode(inStr)
        self.sIO.write(inStr)
        while flagOut != b'':
            self.outie = self.sIO.readline()
            print(self.outie)
        print("done")
        flagOut = b'xx'

    def close(self):
        self.sIO.close()

    def __exit__(self):
        self.sIO.close()

    def ser_read(self):
        self.waiting = self.sIO.in_waiting
        print( self.sIO.read(self.waiting) )
        
    def ser_reader(self):
        outie = b'xx'
        while outie != b'':
            outie = s.readline()
            print(outie )


s = sIO()
s.sIO.write(b'a')
s.ser_read()



def ser_read(self):
    self.waiting = self.sIO.in_waiting
    while self.waiting > 0:
        print( self.sIO.readline() )


def send_cmd(objS, cmd, stateOBJ):
    
    outie = b'xx'
    #print(outie)
    objS.write(cmd)
    ser_reader(objS)

#send_cmd(s, b'b', {})

#send_cmd(s, b'a', {})

#cmd1 = send_cmd(s, b'a', {})


#def ser_reader(self):
#    outie = b'xx'
#  while outie != b'':
 #       outie = s.readline()
  #      print(outie )

















def poller(objS, cmd):
    #if objS.in_waiting == 0:
        
    objS.write(cmd)
    bW = objS.in_waiting
    print(bW)
    strOut = objS.read(bW)
    print(strOut)


def sWrapUp(inS):
    if inS.in_waiting > 0:
        bW = inS.in_waiting
        strOut = inS.read(bW)
        print(strOut)
    else:
        pass
            
def sTest(inS):
    inS.write(b'a')
    sWrapUp(inS)

#def s_reader(inS):
#    inw = s.in_waiting
#    res = s.read(inw)
#    print(res)


#print(res)
#s.write(b'a')
#s_reader(s)
#ser.close()             # close port
