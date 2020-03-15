
# coding: utf-8

# In[28]:


f=open("input.txt","r")
lines=f.readlines()
a=list(map(int,lines[0].split()))
b=list(map(int,lines[1].split()))
a=sorted(a)
b=sorted(b)
a.append(0)
print(a,b)
flag=0
for i in range(len(b)-1,-1,-1):
    j=len(a)-2
    while(j>=0):
        if(a[j]<=b[i]):
            break
        else:
            flag+=1
            a[j+1]=a[j]
        j-=1
    if(flag):
        a[j+1]=b[i]
        b[i]=a[-1]
a.pop()
print(a,b)


# In[20]:




