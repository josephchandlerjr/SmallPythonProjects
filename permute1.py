
def log(i,*args):
    print(' '*i,*args)

def permute1(seq,indent=2):
    log(indent,'seq is ',seq)
    if not seq:
        log(indent,'returning [{}]'.format(seq)) 
        return [seq]
    else:
        res = []
        for i in range(len(seq)):
            rest = seq[:i] + seq[i+1:]
            log(indent,'rest is',rest)
            for x in permute1(rest,indent+4):
                log(indent,'inside inner loop for ',seq)
                log(indent,'seq slice is',seq[i:i+1])
                log(indent,'x is ',x)
                log(indent, 'append', seq[i:i+1]+x, 'to',res)
                res.append(seq[i:i+1] + x)
        log(indent,'returning [{}]'.format(seq))
        return res



if __name__ == '__main__':
    print(permute1((1,2)))
