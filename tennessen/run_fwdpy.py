import sys
import evolve

if __name__ == "__main__":
    theta=float(sys.argv[1])
    rho=float(sys.argv[2])
    seed=int(sys.argv[3])
    evolve.evolve((7310,1,theta,rho,seed))
