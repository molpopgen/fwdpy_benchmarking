#This is a growth epoch
#in the Tennsessen model
N=1032
t = 920-205
G = exp((log(9300)-log(N))/(t))
print(G)
#This is how SLiM2 wants you to do it
#This undershoots the final N
for (i in 1:t)
{
    N=as.integer((N*G))
}
print(N)

#This is how fwdpy/KRT 
#tends to do it, and it
#gets the correct final N
N0=1032
for (i in 1:t)
{
    N=as.integer(round(N0*(G^i)))
}
print(N)

#Refactoring how to do it in slim2,
#which has now pow() function
N0=1032
for (i in 1:715)
{
    N=as.integer(round(N0*exp(i*log(G))))
}

print(N)
