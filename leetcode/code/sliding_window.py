


def sliding_window(numbers, 
                   k):
    
    len_number = len(numbers)
    
    # boundary cases #0
    if len_number * k == 0:
        return []
    
    # boundary case #1 
    if k == 1:
        return numbers
    
    left = [0] * len_number 
    left[0] = numbers[0]
    
    right = [0] * len_number 
    right[len_number - 1] = numbers[len_number - 1]
    
    for i in range(1, len_number):
        
        # from left to right
        if i % k == 0:
            # block start
            left[i] = numbers[i]
        else:
            left[i] = max(left[i - 1], numbers[i])
            
        # from right to left
        j = len_number - i - 1
        if (j + 1) % k == 0:
            # block end
            right[j] = numbers[j]
        else:
            right[j] = max(right[j + 1], numbers[j])
    
    output = []
    for i in range(len_number - k + 1):
        output.append(max(left[i + k - 1], right[i]))
        
    return output

if __name__ == "__main__":
    
    numbers = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    
    output = sliding_window(numbers, k)
    print(output)
    
    
    