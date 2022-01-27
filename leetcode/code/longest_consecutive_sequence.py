def longestConsecutive(nums):
    
    nums.sort()
    print(nums)
 
    longest = 0
    cur_longest = min(1, len(nums))
 
    for i in range(1, len(nums)):
        
        print('nums[i]', nums[i])
        print('nums[i-1]', nums[i-1])
        
        print(i)
        if nums[i] == nums[i-1]:
            continue
        if nums[i] == nums[i-1]+1: 
            print('here')
            cur_longest += 1
        else: 
            longest = max(longest, cur_longest)
            print('longest', longest)
            cur_longest = 1
            
    return max(longest, cur_longest)

if __name__ == "__main__":
    
    nums = [100, 4, 200, 1, 3, 2]
    
    out = longestConsecutive(nums)