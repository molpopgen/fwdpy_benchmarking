import fwdpy as fp
import numpy as np

def evolve(N,npops,theta,rho,seed):
    """
    This function evolves a population
    with only neutral mutations.

    The setup is "ms-like", with
    mutation and recombination occuring
    on the continuous interval from [0,1).
    """
    #A region is defined by a start, stop,
    #and a weight
    nregions=[fp.Region(0,1,1)] #Where neutral mutations occur
    rregions=nregions           #Where recombination occurs
    sregions=[]                 #No selected mutations = empty lst
    rng=fp.GSLrng(seed)         #Random number seed object

    mu_n = theta/(4.*float(N))
    mu_s = 0.
    recrate = rho/(4.*float(N))
    #"nlist" is the list of population sizes 
    #over time.
    #Here, we Evolve for 10N generations.
    #We can have any unsigned, 32-bit
    #integer in "nlist", meaning we
    #implement bottlenecks, etc.,
    #by changing what is in nlist
    nlist = np.array([N]*10*N,dtype=np.uint32) 
    pop=fp.evolve_regions(rng,npops,N,nlist,
            mu_n,mu_s,recrate,
            nregions,
            sregions,
            rregions)
