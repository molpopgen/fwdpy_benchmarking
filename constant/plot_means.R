library(tidyverse)
library(ggplot2)

fwdpy1000=read.table("fwdpy11_results.1000.txt",header=T)
fwdpy10000=read.table("fwdpy11_results.10000.txt",header=T)
slim1000=read.table("slim.1000.txt",header=T)
slim10000=read.table("slim.10000.txt",header=T)

fwdpy1000$Simulation = rep("fwdpy11",nrow(fwdpy1000))
fwdpy10000$Simulation = rep("fwdpy11",nrow(fwdpy10000))
fwdpy1000$theta = rep(1000,nrow(fwdpy1000))
fwdpy10000$theta = rep(10000,nrow(fwdpy10000))

slim1000$Simulation = rep("slim",nrow(slim1000))
slim10000$Simulation = rep("slim",nrow(slim10000))
slim1000$theta = rep(1000,nrow(slim1000))
slim10000$theta = rep(10000,nrow(slim10000))

x = as_tibble(rbind(fwdpy1000,fwdpy10000,slim10000,slim1000))

x$time = log10(x$time/(60^2))
p = ggplot(x,aes(x=factor(theta),time)) +  
    geom_point(position = position_jitter(width = 0.2),aes(color=Simulation),size=2) + 
    xlab(expression(paste(theta,"=",rho))) + ylab("Run time in hours (log10 scale)") +
    theme_bw()

ggsave("test.png",p)
