import sys, time

try:
    timer = time.perf_counter
except AttributeError:
    timer = time.time if sys.platform[:3] != 'win' else time.clock


def total_time(func, *args, _reps=10, **kwargs):
    name = func.__name__
    reps = list(range(_reps))
    t1 = timer()
    for _ in range(reps):
        result = func(*args,**kwargs)
    t2 = timer()
    total_time = t2-t1
    return '{0} found: {1} \n total time: {2:.5f} seconds'.format(name,result,total_time)


def best_time(func, *args, _reps=10, **kwargs):
    best_time = 2**32 
    name = func.__name__
    for _ in range(_reps):
        t1 = timer()
        result = func(*args,**kwargs)
        t2 = timer()
        if t2-t1 < best_time:
            best_time = t2-t1
    return '{0} found: {1} \n best time: {2:.5f} seconds'.format(name,result,best_time)


