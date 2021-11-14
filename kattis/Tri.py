def check(q,w,e):
    if q+w==e:
        return(f"{q}+{w}={e}")
    elif q-w==e:
        return(f"{q}-{w}={e}")
    elif q*w==e:
        return(f"{q}*{w}={e}")
    elif q/w==e:
        return(f"{q}/{w}={e}")
    elif q==w+e:
        return(f"{q}={w}+{e}")
    elif q==w-e:
        return(f"{q}={w}-{e}")
    elif q==w*e:
        return(f"{q}={w}*{e}")
    elif q==w/e:
        return(f"{q}={w}/{e}")
a,b,c=list(map(int,input().split()))
print(check(a,b,c))
