afactaral = lambda n:(n>0 and ((n==0 and 1)+n)*afactaral(n-1))+(n==0 and 1)


#def e_fe(n):
    #exec("n * (e_fe(n-1) if n>1 else 1)")

print(afactaral(3))