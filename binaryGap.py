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