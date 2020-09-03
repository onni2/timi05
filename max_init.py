n = int(input("Enter the length of the sequence: ")) # Do not change this line
Sum = 1
for i in range(1, n+1):
        print(Sum)
        Sum = ((n)*(2*1 + (n -1) * 1) / 2+2 * (pow(2,n) - 1)/ (2 -1))