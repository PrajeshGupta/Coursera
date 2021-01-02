def problem2_8(temp_list):
    if len(temp_list)>0:    
        sum_ = 0
        for i in range(0,len(temp_list)) :
            sum_ = sum_ + temp_list[i]
        average = sum_/len(temp_list)
        print("Average:",float(average))
        print("High:",float(max(temp_list)))
        print("Low:",float(min(temp_list)))
        
        


