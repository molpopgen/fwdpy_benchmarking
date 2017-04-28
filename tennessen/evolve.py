import fwdpy11 as fp11
import fwdpy11.wright_fisher as wf
import numpy as np
import math

def exponential_size_change(Nstart,Nstop,time):
    """
    Generate a list of population sizes according to exponential size_change model

    :param Nstart: population size at onset of size change
    :param Nstop: Population size to reach at end of size change
    :param time: Time (in generations) to get from Nstart to Nstop

    :return: A list of integers representing population size over time.
    """
    if time < 1:
        raise RuntimeError("time must be >= 1")
    if Nstart < 1 or Nstop < 1:
        raise RuntimeError("Nstart and Nstop must both be >= 1")
    G = math.exp((math.log(Nstop) - math.log(Nstart))/time)
    rv=[]
    for i in range(time):
        rv.append(round(Nstart*pow(G,i+1)))
    return rv

def tennessen_popsizes():
    """
    Generates a numpy array of the canges in N over time
    There are 5 epochs, with t=0 being the present.
    
    E1: Ne= 7,310  from t=start(8N?) to t = - 5920 generation (Ancestral sizes until 5920 generations ago)
    
    E2: Ne =14,474 from t = -5920 to t = -2040 (Ancient growth at 5920 g ago)
    
    E3: Ne =1,861 from t= -2040 to t= -920 (OOA, first bottle neck 2040 g ago)
    
    E4: Ne = 1,032 to Ne = 9,300 during t = -920 to t = -205 ( second bottle neck and onset of 715 g of exponential growth at rate 0.31% per gen )  
    
    E5: Ne = 9,300 to Ne = 512,000 during t = -205 to t = -0 ( 205 g of exponential growth at rate 1.95% per gen )  
    """
    n=[7310]*(10*7310) #E1: evolve ancestral size to mutation/selection/drift equilibrium
    n.extend([14474]*(5920-2040)) #E2
    n.extend([1861]*(2040-920)) #E3
    n.extend(exponential_size_change(1032,9300,920-205)) #E4
    n.extend(exponential_size_change(9300,512000,205)) #E5
    return np.array(n,dtype=np.uint32)


def evolve(args):
    """
    This function evolves a population
    with only neutral mutations.

    The setup is "ms-like", with
    mutation and recombination occuring
    on the continuous interval from [0,1).
    """
    N,npops,theta,rho,seed=args
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
    #Here, we use the Tennessen et al.
    #model for European demography,
    #which is defined in the preceding
    #function.
    nlist = tennessen_popsizes() 
    pop = fp11.Spop(N)
    wf.evolve_regions(rng,pop,nlist,
            mu_n,mu_s,recrate,
            nregions,
            sregions,
            rregions)
