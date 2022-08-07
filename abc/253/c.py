#heapq と defaultdict を使う
import heapq
from collections import defaultdict
 
mx=[]
mn=[]
cnt=defaultdict(int)
 
q=int(input())
for _ in range(q):
  query=list(map(int,input().split()))
  if query[0]==1:
    x=query[1]
    #これで数と個数を管理できる
    cnt[x]+=1
    #小さい値であれば0に来る
    #maxは対応していないので、予め-倍する
    heapq.heappush(mx,-x)
    heapq.heappush(mn,x)
 
  if query[0]==2:
    x,c=query[1:]
    #defaultdict の要素からマイナスする
    cnt[x]=max(0,cnt[x]-c)
 
  if query[0]==3:
    #最大要素の数を確認、0ならpopしてなくす
    while cnt[-mx[0]]==0:
      heapq.heappop(mx)
      #最小要素の確認、0ならpopしてなくす
    while cnt[mn[0]]==0:
      heapq.heappop(mn)
    print(-mx[0]-mn[0])