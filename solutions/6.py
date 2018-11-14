def r(z):
 P=sorted(set(z))
 if len(P)<=1:return P
 def c(o,a,b):return(a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
 l=[]
 for p in P:
  while len(l)>1and c(l[-2],l[-1],p)<=0:
   l.pop()
  l.append(p)
 u=[]
 for p in reversed(P):
  while len(u)>1and c(u[-2],u[-1],p)<=0:
   u.pop()
  u.append(p)
 return u[:-1]+l[:-1]
for _ in range(int(input())):
 a = r(list(zip(*[iter(map(int,input().split()))] * 2)))[::-1]
 b = ''
 for i in a:
  b += str(i[0])+' '+str(i[1])+' '
 print(b.strip())