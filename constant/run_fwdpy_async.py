import multiprocessing as mp
import numpy as np
import sys
import evolve

if __name__ == "__main__":
    theta=float(sys.argv[1])
    rho=float(sys.argv[2])
    nprocs=int(sys.argv[3])
    seed=int(sys.argv[4])
    P=mp.Pool(nprocs)
    np.random.seed(seed)
    args=[(10000,1,theta,rho,procseed) for procseed in np.random.randint(0,42000000,nprocs)]
    P.imap_unordered(evolve.evolve,args)
    P.close()
    P.join()
