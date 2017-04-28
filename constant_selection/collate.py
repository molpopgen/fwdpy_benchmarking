import glob
import pandas as pd

#collation here is nastier, so let's brute-force a few things
#1. there are 8 conditions that we're testing, varying fraction
#of selected mutations, s, and h
#2. N=1e4 for all cases
#3. The TOTAL 4Nu and 4Nr are 1e3 for all cases 
pneutral = pd.Series([0.99]*2 + [0.9]*2 + [0.99]*2 + [0.9]*2)
h = pd.Series([0.0,0.5,0.0,0.5,0.0,0.5,0.0,0.5])
s = pd.Series([-1e-3]*4 + [0.05]*4) 
case = pd.Series(list(range(1,9)))
params = pd.DataFrame({'pneut':pneutral,'h':h,'s':s,'case':case})

sims = ['fwdpy','slim']

simnames = []
cases = []
times = []
mem = []
for i in case: 
    for sim in sims:
        b = sim + str(i) + '.*.time.txt'
        g = glob.glob(b)
        for gi in g:
            data = pd.read_csv(gi,sep=' ',header=None)
            simnames.append(sim)
            cases.append(i)
            times.append(data[0][0])
            mem.append(data[1][0])

data = pd.DataFrame({'sim':simnames,'case':cases,'times':times,'mem':mem})

data['times'] /= (60.*60.)

means = data.groupby(['case','sim']).mean().reset_index()

final = means.set_index('case').join(params.set_index('case'))

final.to_csv('means.txt',sep='\t',header=True,index=False)
