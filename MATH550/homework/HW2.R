library(Stat2Data)
library(MASS)
data(PalmBeach)
palm<-PalmBeach

palm.lm<-lm(Buchanan~Bush,data=palm)
plot(Buchanan~Bush,data=palm,col="purple",pch=19)
abline(palm.lm,lwd=2)

standres<-stdres(palm.lm)
plot(standres~palm.lm$fitted.values,pch=19,col=12)

leverage <- hatvalues(palm.lm)
leverage
plot(leverage~palm.lm$fitted.values,pch=19,col=12)

plot(palm.lm,which=c(1,2,3,4),pch=19,col=10)

palm.lm2<-lm(Buchanan~Bush,data=palm[-50])
plot(Buchanan~Bush,data=palm[-50,-13],col="purple",pch=19)
abline(palm.lm2,lwd=2)

## ignore this stuff for now
plot(palm.lm$residuals~palm.lm$fitted.values,pch=19,col=12)
abline(h=0,lwd=2)
plot(Buchanan~Bush,data=palm,col="purple",pch=19)
abline(palm.lm,lwd=2)
palm.lm2<-lm(Buchanan~Bush,data=palm[-50,-13])
abline(palm.lm2,lwd=2,lty=2)
summary(palm.lm)
summary(palm.lm2)

stu<-studres(palm.lm)

stu[50]
standres[50]
standres

