i=0;j=0
for f in range(1,6):
    try: j=list(map(int, input().split())).index(1)+1;i=f 
    except ValueError:pass
print( 0 if(i==3 and j==3) else abs(3-i)+abs(3-j))



#mas optimo:
# l=[2,1,0,1,2]
# for i in l:
#  s=input()
#  if"1"in s:print(i+l[s.find("1")//2])

