
def concat(reads):
    max_val = -1
    best_read = ""
    best_ps = ""
    big_read = ""
    list_of_concats = []
    for i in range(0,len(reads)):
        big_read = ""
        curr_read = reads[i] #the current read that we are on 
        #matches_arr = AssemblyAlgorithm()#array where each index contains a tuple of the read that matches,
                                          #if it is a prefix or suffix and the number of nucleotides that matches
        matches_arr = [["ATGCTACC","s",3],["ATGCTAC","s",2]]
        for j in range(0,len(matches_arr)):
            if(matches_arr[j][2]>max_val and matches_arr[j][2]>20):
                max_val = matches_arr[j][2]
                best_read = matches_arr[j][0]
                best_ps = matches_arr[j][1]
        if(best_ps=="p"):
            big_read += curr_read + best_read[max_val:]
            
            
        elif(best_ps=="s"):
            big_read += best_read + curr_read[max_val:]
            
        list_of_concats.append(big_read)
        
    return list_of_concats
readz = ["ACCTTACT"]
print(concat(readz))
            
    
