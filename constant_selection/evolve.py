import fwdpy11 as fp11
import fwdpy11.fitness as fp11w
import fwdpy11.temporal_samplers as tp
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
    N,theta,rho,pneutral,s,h,seed = args
    #A region is defined by a start, stop,
    #and a weight
    nregions=[fp11.Region(0,1,1)]        #Where neutral mutations occur
    rregions=nregions                  #Where recombination occurs
    sregions=[fp11.ConstantS(0,1,1,s,h)] #Where selected mutations occur 
    rng=fp11.GSLrng(seed)                #Random number seed object

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
    fitness=fp11w.SpopAdditive(1) #Scaling of 1 makes model identical to SLiM
    sampler=tp.RecordNothing()
    pop=fp11.Spop(N)
    wf.evolve_regions_sampler_fitness(rng,pop,nlist,
            mu_n,mu_s,recrate,
            nregions,
            sregions,
            rregions,
            fitness,sampler,0)
