def input():
    with open("C:/Users/Geoffrey/Documents/PROGRAMS/HASHCODE/a_an_example.in.txt", "r") as file:
        data = file.readlines()
        x=0
        c,p = data[x].split()
        x+=1;
        c=int(c);p=int(p);
        contributors = []
        for i in range(c):
            name,skills = data[x].split()
            x+=1;
            contributors.append({name:[]})
            for k in range(int(skills)):
                skillname,skillpts = data[x].split()
                contributors[i][name].append([skillname,int(skillpts)])
                x+=1;
        # print(contributors)
        
                
                
                
                
                
            
    
    
def main():
    input()
    return 0

if __name__=='__main__':
    main()