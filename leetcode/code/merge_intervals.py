

# interval_len = len(intervals)
# print(interval_len)


def merge(intervals):
    
    print(intervals)
    intervals.sort(key=lambda x: x[0])
    print(intervals)
    
    merged = []
    for interval in intervals:
        
        print(interval)
        print(interval[0])
        
        # if the list of merged intervals is empty or if the current 
        # interval does not overlap with the previous, simply append it.
        
        if len(merged) == 0 or merged[-1][1] < interval[0]:
            merged.append(interval)
            
        # otherwise, there is overlap, so we merge the current and previous
        # intervals.
        
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged

if __name__ == "__main__":
    
    intervals = [[1,3], [2,6], [8,10], [15,18]]
    
    output = merge(intervals)
    print(output)
    
    


# idx = 0
# output = []
# for i in range(interval_len):
#     print(i)
    
#     current_left, current_right = intervals[idx][0], intervals[idx][1]
#     next_left, next_right = intervals[idx+1][0], intervals[idx+1][1]
    
#     if next_right < current_left and current_left < next_right:
#         output.append([current_left, next_right])
        
#     if current_right < next_left:
#         output.append([curre])

#     print(current_left, current_right, next_left, next_right)
#     quit()