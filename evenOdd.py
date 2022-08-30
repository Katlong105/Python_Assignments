def evenOdd(*args):
    
    evenList = [n for n in args if n%2==0]
    oddList = [n for n in args if n%2==1]
    
    return f'EvenNumbers: {evenList}\nOddNumbers: {oddList}'

inputValue = evenOdd(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
print(inputValue)