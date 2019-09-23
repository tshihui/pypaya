#-----------------------------------------------------#
#------ Simple function to return reverse array ------#
#-----------------------------------------------------#

def rev(ar):
    la = len(arr)
    rarr = []
    for i in range(la-1, -1, -1):
        rarr.append(ar[i])
        
    return(rarr)
    
    
