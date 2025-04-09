def haslo():
    import random

    p=['1','2','3','4','5','6','7','8','9','0',"q","w","e","r","t",'y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','!','@','%','^','&','*','#','$','(',')','?']
    a=[]
    for i in range(8):
        q=random.randint(0,len(p)-1)
        a.append(p[q])
    print(''.join(a))
