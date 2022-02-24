def input():
    with open("a_an_example.in.txt", "r") as file:
        data = file.readlines()
        x=0
        c,p = data[x].split()
        x+=1;
        c=int(c);p=int(p);
        contributors = []
        for i in range(c):
            name,skills = data[x].split()
            contributors.append(dict([name,-1]))
            for i in range(skills):
                
                
                
            
    
    
def main():
    input()
    return 0

if __name__=='__main__':
    main()