def myzip(*args):
    iters = list(map(iter,args))
    print(iters is False)
    while iters: 
        res = [next(i) for i in iters]
        print(iters,iters==True)
        yield tuple(res)


print(list(myzip()))


