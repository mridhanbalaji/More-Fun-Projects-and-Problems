def pythagreon(n):
    #Creating a lisn of all values until input
    #Then creating a list to append all the squared values
    lista = list(range(1,n + 1))
    newlista = []
    
    listb = list(range(1,n +1))
    newlistb = []
    
    listc = list(range(1,n + 1))
    newlistc = []
   
    j = []
    filter_j = []
    
    f = []
    filter_f = []
    
    nestedlist =  []
    
    # 
    for i in lista: 
        a = i ** 2
        newlista.append(a)
        newlista = newlistc = newlistb
    
    for i in listb: 
        b = i ** 2
        newlistb.append(b)
        newlista = newlistc = newlistb
    
    for i in listc: 
        c = i ** 2
        newlistc.append(c)

    for i in newlista:
        d = i

    # for i in newlistb:
    #     e = i
    
    for i in newlistc:
        for z in newlistb:
            for x in newlista:
                if z + x == i:
                    k = (z, x, i)
                    j.append(k)
                elif z + x != i:
                    d = (z, x, i)
                    f.append(d)
    for i in j:
        if i not in filter_j:
            filter_j.append(i)
    
    for i in f:
        if i not in filter_f:
            filter_f.append(i)
    
    
    return str(filter_j) + "True" 
    # and str(filter_f) + "False"
    
     


    
    if d + e == f:
        print( "(" + str(d) + "," + str(e) + "," + str(f) + ")" + "True")
        
    for i in listc:
        c = i ** 2
        listc.remove(i)
        listc.append(a)

    nestedlist.append([newlista, newlistb, newlistc])

    for nestlist in nestedlist:
        if nestlist[0] + nestlist[1] == nestlist[2]:
            print(str(nestlist[0], nestlist[1], nestlist[2]) + "True")
        else:  
            print(nestlist[0])
    

pythagreon(100)