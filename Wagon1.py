N = int(input())
lst = ["W","M", "A", "A" , "M", "W"]

opposite_seat = N+1 if N%2==1 else N-1
if N < 49:
    line = ((N % 48)-1)//8
    ranje = line % 2
else:
    line = ((N % 54)-1)//9
    ranje = line % 2
print(opposite_seat, lst[line])