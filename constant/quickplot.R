x=read.table("foo")
y=read.table("foo2")

xl=c(min(x$V1,y$V1),max(x$V1,y$V1))

pdf("performance1.pdf")

plot(ecdf(x$V1),xlim=xl,xlab="Run time (seconds)",ylab="Cumulative density")
lines(ecdf(y$V1),col="red")
dev.off()
