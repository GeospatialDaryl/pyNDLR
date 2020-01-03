class sIO:

    outie = b'xx'
    
    def __init__(self,
                 strCOM = 'COM3',):   # open sIO method
                 #timeout = 0.5 ):
        
        self.sIO = serial.Serial(strCOM)#, timeout)
        print(self.sIO.name)
        #self.cmd('a')

    def raw_poll(self, strPoll):
        s


    def cmd(self, inStr):
        flagOut = b'xx'
        inStr = str.encode(inStr)
        self.sIO.write(inStr)
        while flagOut != b'':
            self.outie = self.sIO.readline()
            print(self.outie)
        print("done")
        flagOut = b'xx'


#tio = sIO()
#tio.cmd("b")


#class NDLR:
 #   def __init__(
         


