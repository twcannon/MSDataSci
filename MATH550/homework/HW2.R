library(Stat2Data)
library(MASS)

#Question 2
bears <- read.table("/home/thomas/git/datascience/MSDataSci/MATH550/data/Bears.csv",header=TRUE,sep=",")
attach(bears)

#Part A
plot(ChestGirth, Weight, pch = 16, cex = 1.3, col = "blue", main = "Weight plotted against Chest Girth", xlab = "Chest Girth (inches)", ylab = "Weight (pounds)")
lm(Weight ~ ChestGirth)
abline(lm(Weight ~ ChestGirth))
modelA <- lm(Weight ~ ChestGirth)
par(mfrow = c(2,2))
plot(modelA)

#Part B
ChestGirth2 <- ChestGirth^2

plot(ChestGirth2, Weight, pch = 16, cex = 1.3, col = "blue", main = "Weight plotted against Chest Girth^2", xlab = "Chest Girth^2 (inches^2)", ylab = "Weight (pounds)")
lm(Weight ~ ChestGirth2)
abline(lm(Weight ~ ChestGirth2))
modelB <- lm(Weight ~ ChestGirth2)
plot(modelB)

#Part C
logChestGirth <- log(ChestGirth)
logWeight <- log(Weight)

plot(logChestGirth, logWeight, pch = 16, cex = 1.3, col = "blue", main = "log(Weight) plotted against log(Chest Girth)", xlab = "Chest Girth (inches)", ylab = "Weight (pounds)")
lm(logWeight ~ logChestGirth)
abline(lm(logWeight ~ logChestGirth))
modelC <- lm(logWeight ~ logChestGirth)
par(mfrow = c(2,2))
plot(modelC)
plot(modelC,pch=19,col=10,which=c(1,2,3,4))
standres<-stdres(modelC)
plot(standres~modelC$fitted.values,pch=19,col=12)

#Part D
#95% confidence intervals on page 24
round(confint(modelC,level=0.95),3)

results <- predict(modelC,newdata=data.frame(logChestGirth=c(log(38))),interval="prediction",level=0.95)
exp(results)







#Question 3
#Part A
data(PalmBeach)
palm<-PalmBeach

palm.lm<-lm(Buchanan~Bush,data=palm)
plot(Buchanan~Bush,data=palm,col="purple",pch=19)
abline(palm.lm,lwd=2)

standres<-stdres(palm.lm)
plot(standres~palm.lm$fitted.values,pch=19,col=12)

leverage <- hatvalues(palm.lm)
leverage
plot(leverage,pch=19,col=12)

#Part B
plot(palm.lm)


#Part C
palm.removed <- palm[- c(13,50),]

log.Buchanan <- log(palm.removed$Buchanan)
log.Bush <- log(palm.removed$Bush)
plot(log.Buchanan~log.Bush,col="purple",pch=19)
palm.lm2<-lm(log.Buchanan~log.Bush)
abline(palm.lm2,lwd=2)

#Part C
plot(palm.lm2)

#Part D
round(confint(palm.lm2,level=0.95),3)

palm$Buchanan[50]
palm$Buchanan[13]

results.50 <- predict(palm.lm2,newdata=data.frame(log.Bush=c(log(palm$Bush[50]))),interval="prediction",level=0.95)
exp(results.50)
results.13 <- predict(palm.lm2,newdata=data.frame(log.Bush=c(log(palm$Bush[13]))),interval="prediction",level=0.95)
exp(results.13)
exp(results.50[1])
exp(results.13[1])
palm$Buchanan[50] <- exp(results.50[1])
palm$Buchanan[13] <- exp(results.13[1])

plot(Buchanan~Bush,data=palm,col="purple",pch=19)
