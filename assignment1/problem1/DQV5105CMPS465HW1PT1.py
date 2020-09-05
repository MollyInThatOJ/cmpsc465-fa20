
line1 = [int(i) for i in input().split()]
line2 = [int(i) for i in input().split()]


n1 = line1[0]
n2 = line2[0]
sortedboth = [None]*(n1+n2+1)
sortedboth[0]=(n1+n2)

i = 1
j = 1
k = 1

while i <= n1 and j <= n2:
    if line1[i] < line2[j]:
        sortedboth[k] = line1[i]
        i+=1
        k+=1
    else:
        sortedboth[k] = line2[j]
        j+=1
        k+=1
        
while i < n1 or i == n1:
    sortedboth[k]=line1[i]
    i+=1
    k+=1
    
while j < n2 or j == n2:
    sortedboth[k]=line2[j]
    j+=1
    k+=1
    
out = ''+str(sortedboth[0])
for i in sortedboth[1:]:
    out+=' '+str(i)
    
print(out)