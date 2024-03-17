def Dict(k,v):
    global d
    d = {}
    for i in range(len(k)):
        d[k[i]]=v[i]
    print(d)

k=[1001,1002,1003,1004,1005]
v=["USA","Canada","China","Japan","UK"]
Dict(k,v)
print(d)