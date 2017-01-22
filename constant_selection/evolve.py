import fwdpy as fp
import fwdpy.fitness as fpw
import numpy as np

def evolve(N,npops,theta,rho,pneutral,s,h,seed):
    """
    This function evolves a population
    with only neutral mutations.

    The setup is "ms-like", with
    mutation and recombination occuring
    on the continuous interval from [0,1).
    """
    #A region is defined by a start, stop,
    #and a weight
    nregions=[fp.Region(0,1,1)]        #Where neutral mutations occur
    rregions=nregions                  #Where recombination occurs
    sregions=[fp.ConstantS(0,1,1,s,h)] #Where selected mutations occur 
    rng=fp.GSLrng(seed)                #Random number seed object

    mu_n = pneutral*theta/(4.*float(N))
    mu_s = (1.-pneutral)*theta/(4.*float(N))
    recrate = rho/(4.*float(N))
    #"nlist" is the list of population sizes 
    #over time.
    #Here, we Evolve for 10N generations.
    #We can have any unsigned, 32-bit
    #integer in "nlist", meaning we
    #implement bottlenecks, etc.,
    #by changing what is in nlist
    nlist = np.array([N]*10*N,dtype=np.uint32) 
    fitness=fpw.SpopAdditive(1) #Scaling of 1 makes model identical to SLiM
    sampler=fp.NothingSampler(1)
    pops=fp.SpopVec(1,N)
    pop=fp.evolve_regions_sampler_fitness(rng,pops,sampler,fitness,nlist,
            mu_n,mu_s,recrate,
            nregions,
            sregions,
            rregions,0)
