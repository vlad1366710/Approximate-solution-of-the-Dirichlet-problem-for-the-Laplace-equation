import numpy




h=0.1
eps=0.00001
n=int(1/h)


def norm(x,n):
    max=0
    sum=0
    for i in range(1,n):
        for j in range(1,n):
            sum=sum+abs(x[i,j])
        if(sum > max):
            max=sum
            sum=0
    return(max)

def func(u,uh):
    for i in range(1,n):
                for j in range(1,n):
                    uh[i,j] = u[i,j]
                    uu = 0.25 * (u[i + 1,j] + u[i - 1,j] + u[i,j + 1] + u[i,j-1])
                    u[i,j] = u[i,j] + w * (uu - u[i,j])
                    uh[i,j] = u[i,j] - uh[i,j]




x=numpy.zeros((n+1))
y=numpy.zeros((n+1))
for i in range(n):
    x[i]=i*h
    y[i]=x[i]
u = numpy.zeros((n+1,n+1))
uh=numpy.zeros((n+1,n+1))
for i in range(n):
    u[i]= numpy.zeros((n+1))
    uh[i]= numpy.zeros((n+1))
for j in range(n):
    u[0,j]=50*y[j]*y[j]
    u[n,j]= 50*(1-x[j])
    uh[0,j] = 50*y[j]*y[j]
    uh[n,j] = 50*(1-x[j])
    u[j,0] = 60*x[j]*(1-x[j]*x[j])
    u[j,n] = 0
    uh[i,0] = 60*x[j]*(1-x[j]*x[j])
    uh[i,n] = 0

for i in range(1,n):
    for j in range(1,n):
        u[i,j] = i * j

k=0
uu=0

for w in numpy.arange(0.1,2,0.1):
    k = 0
    func(u,uh)
    k=k+1
    while (norm(uh, n) > eps):
        for i in range(1,n):
                for j in range(1,n):
                    uh[i,j] = u[i,j]
                    uu = 0.25 * (u[i + 1,j] + u[i - 1,j] + u[i,j + 1] + u[i,j-1])
                    u[i,j] = u[i,j] + w * (uu - u[i,j])
                    uh[i,j] = u[i,j] - uh[i,j]

        k=k+1
    print ( "w = " , round(w,3)  ," k = ", k )

print ( "matrix u:")
print(u)


