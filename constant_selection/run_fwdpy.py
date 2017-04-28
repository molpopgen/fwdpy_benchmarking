import sys
import evolve

if __name__ == "__main__":
    theta=float(sys.argv[1])
    rho=float(sys.argv[2])
    seed=int(sys.argv[3])
    pneutral=float(sys.argv[4])
    s=float(sys.argv[5])
    h=float(sys.argv[6])
    evolve.evolve((10000,theta,rho,pneutral,s,h,seed))
