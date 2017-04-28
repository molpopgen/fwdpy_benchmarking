library(tidyverse)
fwdpy1000=read.table("fwdpy11_results.1000.txt",header=T)
fwdpy10000=read.table("fwdpy11_results.10000.txt",header=T)
slim1000=read.table("slim.1000.txt",header=T)
slim10000=read.table("slim.10000.txt",header=T)
runtime = c(mean(fwdpy1000$time)/(60^2),mean(fwdpy10000$time)/(60^2),mean(slim1000$time)/60^2,mean(slim10000$time)/(60^2))
print(runtime)

means = tibble(
    program=c('fwdpy11','fwdpy11','slim2','slim2'),
    N = c(1e3,1e4,1e3,1e4),
    theta = rep(1e4,4),
    rho = theta,
    ngens_sim = 10*N,
    runtime = c(mean(fwdpy1000$time)/(60^2),mean(fwdpy10000$time)/(60^2),mean(slim1000$time)/60^2,mean(slim10000$time)/(60^2)),
    mem = c(mean(fwdpy1000$mem),mean(fwdpy10000$mem),mean(slim1000$mem),mean(slim10000$mem))
    )

print(means)


