from collections import deque


def letterCombinations(digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    interpret_digit = {
        '1': '',
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
        '0': ' '}
    all_combinations = [''] if digits else []
    
    print(all_combinations)
    
    for digit in digits:
        current_combinations = list()
        for letter in interpret_digit[digit]:
            print('letter', letter)
            for combination in all_combinations:
                # print('combo', combination)
                current_combinations.append(combination + letter)
        all_combinations = current_combinations
        print(all_combinations)
    return all_combinations

if __name__ == '__main__':
    
    digits = "234"
    out = letterCombinations(digits)
    print(out)