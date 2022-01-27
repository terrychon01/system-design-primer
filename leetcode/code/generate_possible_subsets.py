



def generate_subsets(numbers):
    
    
    len_numbers = len(numbers)
    print(len_numbers)
    
    subsets = [[]]

    for i in range(len_numbers):
        print('i', i)
        print([i])
        subsets += [x + [i] for x in subsets]
        
        for x in subsets:
            print('x', x)
    
    return subsets





if __name__ == "__main__":
    
    numbers = [1, 2, 3, 6, 8, 9]
    output = generate_subsets(numbers)
    
    print(output)
    
    print('todo')