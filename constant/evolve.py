import fwdpy11 as fp11
import fwdpy11.wright_fisher as wf
import numpy as np

def evolve(args):
    """
    This function evolves a population
    with only neutral mutations.

    The setup is "ms-like", with
    mutation and recombination occuring
    on the continuous interval from [0,1).
    """
    N,theta,rho,seed=args
    #A region is defined by a start, stop,
    #and a weight
    nregions=[fp11.Region(0,1,1)] #Where neutral mutations occur
    rregions=nregions           #Where recombination occurs
    sregions=[]                 #No selected mutations = empty lst
    rng=fp11.GSLrng(seed)         #Random number seed object

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
    pop=fp11.Spop(N)
    wf.evolve_regions(rng,pop,nlist,
            mu_n,mu_s,recrate,
            nregions,
            sregions,
            rregions)
