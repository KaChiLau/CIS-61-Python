def sum(n):
    if  n == 1:
        return 1
    return n ** 3 + sum(n - 1) 

def memo(f):
    cache = {}
    def memoized(n):
        if n not in cache:
            cache[n] = f(n)
            return cache[n]
    return memoized
    
sum = memo(sum)

print(sum(13))

