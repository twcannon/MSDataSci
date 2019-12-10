burst <- read.csv("/home/thomas/git/datascience/MSDataSci/MATH550/project/cat64ms.00143",header=TRUE,sep=",")
attach(burst)
total <- CHAN1+CHAN2+CHAN3+CHAN4
total
plot(total, type="l")
acf <- acf(total,plot=TRUE,lwd=2,lag.max=1000)
