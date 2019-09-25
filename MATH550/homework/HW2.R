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
par(mfrow = c(2,2))
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

#Part D
#95% confidence intervals on page 24
round(confint(modelA,level=0.95),3)

newdata = data.frame(ChestGirth=38)
predict(modelA,newdata,interval="predict")








#Question 3

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

plot(palm.lm)


palm.removed <- palm[- c(13,50),]

log.Buchanan <- log(palm.removed$Buchanan)
log.Bush <- log(palm.removed$Bush)
plot(log.Buchanan~log.Bush,col="purple",pch=19)
abline(palm.lm2,lwd=2)


palm.lm2<-lm(log.Buchanan~log.Bush)
plot(palm.lm2)
log(palm$Bush[50])
round(confint(palm.lm2,level=0.95),3)
log_test_bush <- log(palm$Bush[50])
newdata <- data.frame(Bush=log_test_bush)
predict(palm.lm2,newdata,interval="predict")
newdata <- data.frame(Bush=log(palm$Bush[13]))
predict(palm.lm2,newdata,interval="predict")


