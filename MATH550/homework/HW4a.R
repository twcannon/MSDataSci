bodyfat <- read.csv("/home/thomas/git/datascience/MSDataSci/MATH550/data/bodyfat.csv", header=TRUE)
attach(bodyfat)
head(bodyfat)

#1
c <- cor(bodyfat)
round(c,3)
pairs(bodyfat$bodyfat~age+weight+height+neck+chest+abdomen+hip+thigh+knee+ankle+biceps+forearm+wrist)

#Discussion
#

#2
model <- lm(bodyfat ~., data=bodyfat)
summary(model)
#Discussion


#3
#optional?

#4 For your chosen model, show Residual plots versus each predictor and versus fits.

#Residual Plots vs Predictior
summary(model)
StanRes1 <- rstandard(model)
par(mfrow=c(2,2))
plot(age,StanRes1, ylab="Standardized Residuals",pch=19,col=10)
abline(h=0,lwd=2)
plot(weight,StanRes1, ylab="Standardized Residuals",pch=19,col=10)
abline(h=0,lwd=2)
plot(height,StanRes1, ylab="Standardized Residuals",pch=19,col=10)
abline(h=0,lwd=2)
plot(neck,StanRes1, ylab="Standardized Residuals",pch=19,col=10)
abline(h=0,lwd=2)
par(mfrow=c(2,2))
plot(chest,StanRes1, ylab="Standardized Residuals",pch=19,col=10)
abline(h=0,lwd=2)
plot(abdomen,StanRes1, ylab="Standardized Residuals",pch=19,col=10)
abline(h=0,lwd=2)
plot(hip,StanRes1, ylab="Standardized Residuals",pch=19,col=10)
abline(h=0,lwd=2)
plot(thigh,StanRes1, ylab="Standardized Residuals",pch=19,col=10)
abline(h=0,lwd=2)
plot(knee,StanRes1, ylab="Standardized Residuals",pch=19,col=10)
abline(h=0,lwd=2)
plot(ankle,StanRes1, ylab="Standardized Residuals",pch=19,col=10)
abline(h=0,lwd=2)
plot(biceps,StanRes1, ylab="Standardized Residuals",pch=19,col=10)
abline(h=0,lwd=2)
plot(forearm,StanRes1, ylab="Standardized Residuals",pch=19,col=10)
abline(h=0,lwd=2)
plot(wrist,StanRes1, ylab="Standardized Residuals",pch=19,col=10)
abline(h=0,lwd=2)


#Residual Plots vs Fits
par(mfrow=c(1,1))
plot(model$fitted.values,bodyfat$bodyfat,xlab="Fitted Values", ylab="Bodyfat",col=10,pch=19)
abline(lsfit(model$fitted.values,bodyfat$bodyfat),lwd=2)

#5 Added Variable Plots
library(car)
par(mfrow=c(2,2))
avPlots(model,terms=~.,ask=FALSE,pch=19)

#6 Response Vs Fitted
#??
model <- lm(formula = body_fat[,1] ~ body_fat[,2] + body_fat[,3] + body_fat[,4] + body_fat[,6] + body_fat[,7] + body_fat[,8] + body_fat[,9] + body_fat[,10] + body_fat[,11] + body_fat[,12] + body_fat[,13] + body_fat[,14])
summary(model)
par(mfrow = c(2,2))
plot(model)
#7 Marginal Model Plots
mmp(model)

#8 Variance Inflation Factors
vif(model)


#9 Conclusion