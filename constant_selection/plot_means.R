library(ggplot2)
x = read.table("data.txt",header=T)

plot_labeller <- function(variable,value){
  if (variable=='s') {
      return(paste("s = ",value,sep=""))
  } else {
      return(paste("h = ",value,sep=""))
  } 
}
p = ggplot(x,aes(x=factor(pneut),times,color=Simulation)) +  #+ geom_boxplot(aes(color=sim,position="dodge")) + 
    facet_grid(h~s,scales="free_y",labeller=plot_labeller) + 
    geom_point(position = position_jitter(width = 0.2)) + theme_bw()  +
    xlab("Proportion of new mutations that are neutral.") + ylab("Run time (hours)")

ggsave("test.png",p)
