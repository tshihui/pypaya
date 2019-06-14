#########################################################
#------- Solution to identify largest binary gap -------#
#########################################################

#-----------------------------------------#
#---------- Final Version ----------------#
#-----------------------------------------#
#----- Functions -----#
def find0(binNum):
    # find first 1 
    pos1 = binNum.find('1')
    # find second 1
    pos2 = binNum.find('1', pos1+2)
    # return number of 0s
    count0  = binNum[pos1:pos2+1].count('0')
    # return cut string 
    newBinNum = binNum[pos2:len(binNum)]
    
    return(count0, newBinNum)

def binaryGap(N):    
     # Needs to be improved
     binNum = "{0:b}".format(N)
     
     count0s = []
     if binNum.count('0') > 0 and binNum.count('1') > 1:
         while(len(binNum) > 2):
             binAns = find0(binNum)
             count0s.append(binAns[0])
             binNum = binAns[1]
         return(max(count0s))
     else:
         return(0)

#----- Main function -----#
if __name__ ==  '__main__':
    print('---------- Running test cases: ')
    print('When N = 53: ')
    print(binaryGap(53))
    print('')
    
    print('When N = 1456: ')
    print(binaryGap(1456))
    print('')

    print('When N = 10555501: ')
    print(binaryGap(10555501))
    print('')

    
#-------------------------------------#
#---------- Version 2 ----------------#
#-------------------------------------#
def find0(binNum):
    # find first 1 
    pos1 = binNum.find('1')
    # find second 1
    pos2 = binNum.find('1', pos1+2)
    # return number of 0s
    count0  = binNum[pos1:pos2+1].count('0')
    # return cut string 
    newBinNum = binNum[pos2:len(binNum)]

    if count0 == 0:
        return(0)
    else:
        return(count0, newBinNum)

def binaryGap(N):    
     # Needs to be improved
     binNum = "{0:b}".format(N)
     
     count0s = []
     if binNum.count('0') > 0 and binNum.count('1') > 1:
         while(len(binNum) > 2):
             binAns = find0(binNum)
             count0s.append(binAns[0])
             binNum = binAns[1]
         return(max(count0s))
     else:
         return(0)


#-------------------------------------#
#---------- Version 1 ----------------#
#-------------------------------------#
def binaryGap(N):    
     # Needs to be improved
     binNum = "{0:b}".format(N)
     
     count0s = []
     pos1, pos2 = 0, 0
     if binNum.count('0') > 0 and binNum.count('1') > 1:
         pos1 = binNum.find('1')
         while (pos1+2) <= len(binNum):
             pos2 = binNum.find('1', pos1+2)
             count0s.append(binNum[pos1:pos2+1].count('0'))
             pos1 = pos2
         return(max(count0s))
     else:
         return(0)
