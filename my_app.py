import sys

def twosum(a, b):
    result = int(a) + int(b)
    print(f'Сумма {a} и {b} = {result}')

if __name__ == '__main__':
    a = sys.argv[1]
    b = sys.argv[2]
    twosum(a, b)
	
