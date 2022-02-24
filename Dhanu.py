data={}
pro = {}
ans={}
checking = {}
def prob(d):
    global checking
    checking = {}
    sidelan=[]
    for j in d:
        for k in data:
            if j in data[k] and data[k][j]>=d[j]:
                checking[k]=j
                break
        
        else:
            return False
    return True
                    
def update(a):
    for i in a:
        for j in data:
            if i==j:
                data[i][a[i]]=str(int(data[i][a[i]])+1)
                break
    
with open("C:/Users/Geoffrey/Documents/PROGRAMS/HASHCODE/a_an_example.in.txt", "r") as file:
    file_list = file.readlines()
    x=0;
    a=list(map(int,file_list[x].split()))
    x+=1;
    for _ in range(a[0]):
        i=file_list[x].split()
        data[i[0]]={}
        x+=1
        for _ in range(int(i[1])):
            d=file_list[x].split()
            data[i[0]][d[0]]=d[1]
            x+=1
    for _ in range(a[1]):
        a=file_list[x].split()
        pro[a[0]]={}
        x+=1
        for i in range(int(a[-1])):
            d=file_list[x].split()
            pro[a[0]][d[0]]=d[1]
            x+=1

while len(ans)!=len(pro):
    for i in pro:
        if prob(pro[i]):
            ans[i]=checking
            update(checking)
            break
output_path = "C:/Users/Geoffrey/Documents/PROGRAMS/HASHCODE/output/a_an_example.in.txt"

with open(output_path, "w") as file:
    file.write(str(len(ans))+"\n")
    for i in ans:
        file.write(i+"\n")
        for j in ans[i]:
            file.write(j+" ")
        file.writelines("\n")