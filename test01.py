import serial
import time
import unicodedata

def remove_control_characters(s):
    # from https://stackoverflow.com/questions/4324790/removing-control-characters-from-a-string-in-python
    # ## Answer from Alex Quinn https://stackoverflow.com/users/500022/alex-quinn
    return "".join(ch for ch in s if unicodedata.category(ch)[0]!="C")


def serial_anticlobber(t = 0.11):
    time.sleep(t)

def append_element_to_list(inList, inElement):
    return inList + inElement

def list_to_string(inList):
    strOut = ""
    first = True
    if first:
        for items in inList:
            strOut=  strOut + str( items )
            first = False
        else:
            strOut=  strOut + str(","+  items )

    return strOut

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
        self.a_patternBuff = []
        # # # Define NDLR Data Structure
        # 
        #
        #
        #  0) NDLR Presets
        #         n  := 1 of 8 presets
        #         NN := preset banks {1 to 10}
        #       
        #     <an>
        #         PreLNN-XX,
        #
        #  1) NDLR Patterns
        #    - Dump:
        #     ``1) Read the Patterns from all 20 NDLR memory slots (21-40).
        #            The first number is the Pattern Type (20,40,60), the following
        #             16 numbers are the step values. The results are formatted the same
        #             way the Write command expects. `` -- (C) Conductive Labs (2020)
        #         XX := pattern number {21 to 40}
        #         NN := Pattern Type {20,40,60}
        #         yM := step values in midi, m := { 0 - 127 theor}  
        #      <b>
        #         <PattXX-NN, y1, y2, ... y16>
        #        
        #
        #         Patterns are stored as a py dict:
        #             val is a list with 17 entries
        #             'PattXX':[NN, y1, y2, ... y16]
        #                 pos 0 := pattern type {20,40,60}
        #                 pos 1 ... 17 := step value
        #
        self.a_patterns = {}
        
        #
        #
        #  
        #          
        #
        #
        #
        #
        #
        #
        #
        #
        #
        #
        #
        #
        #
        #
        #
        #
        #
        #



        

        
    def a_pull_patterns(self):
        #self.sIO.sIO.write(b'<b>')
        self.sIO.send(b'<b>')
        listPatterns = s.sIO._strBuff.split('\n')
        #print(len(listPatterns))
        self._patternBuff = listPatterns
        listBuff = []
        for items in self._patternBuff:
            if len(items) > 0:
                if items[0] == '<':
                    listBuff.append(items)
                    print(items)
        self._patternBuff = listBuff

    def a_parse_patterns(self):
        for line in self._patternBuff:
            line = line.replace('<','')
            line = line.replace('>','')
            line = line.replace('\r','')
            line = line.split(',')
            lkey,val0 = line[0].split('-')
            rside = [val0] + line[1:]
            print(lkey)
            #print(val0)
            print(rside)
            #val0 = line[0]
            self.a_patterns[lkey] = rside

    def a_make_pattern(self, patternNum):
        if int(patternNum) > 40 or int(patternNum) < 21:
            self.a_patterns[patternNum] = { [
                                            7, 7, 7, 7, 7, 5, 5,  7,
                                            5, 5, 5, 5, 5, 5, 5,  1    ] }

    def a_put_pattern(self, patternNum, patternType):
        strOut = "<Patt"+str( int(patternNum) )
        Rhandside = self.a_patterns['Patt'+str(patternNum)]
        strOut = strOut + list_to_string( Rhandside )
        strOut = strOut + ">"
        print(strOut)
        print( strOut[0:8]+"-")
                
            
        
                    
s = pyNuDLR()
print("_________________")
s.a_pull_patterns()
s.a_parse_patterns()
s.a_make_pattern(30)
s.a_put_pattern(30,40)
print("_________________")
#print(s.sIO._strBuff)

for items in s._patternBuff:
        if len(items) > 0:
            if items[0] == '<':
                 print(items)


