bodyfat <- read.csv("/home/thomas/git/datascience/MSDataSci/MATH550/data/bodyfat.csv", header=TRUE)
attach(bodyfat)
head(bodyfat)



# 1
c <- cor(bodyfat)
round(c,3)
pairs(bodyfat$bodyfat~age+weight+height+neck+chest+abdomen+hip+thigh+knee+ankle+biceps+forearm+wrist)



# 2
model <- lm(bodyfat ~., data=bodyfat)
summary(model)


# 3
n <- length(model$residuals)
backAIC <- step(model,direction="backward", data=bodyfat)
backBIC <- step(model,direction="backward", data=bodyfat, k=log(n))

# using the four variables given by back BIC:
pairs(bodyfat$bodyfat~weight+abdomen+forearm+wrist)
model_new <- lm(bodyfat$bodyfat~weight+abdomen+forearm+wrist)
summary(model_new)



# 4

# Residual Plots vs Predictior
StanRes1 <- rstandard(model_new)
par(mfrow=c(2,2))
plot(weight,StanRes1, ylab="Standardized Residuals",pch=19,col=10)
abline(h=0,lwd=2)
plot(abdomen,StanRes1, ylab="Standardized Residuals",pch=19,col=10)
abline(h=0,lwd=2)
plot(forearm,StanRes1, ylab="Standardized Residuals",pch=19,col=10)
abline(h=0,lwd=2)
plot(wrist,StanRes1, ylab="Standardized Residuals",pch=19,col=10)
abline(h=0,lwd=2)

# Residual Plots vs Fits
par(mfrow=c(1,1))
plot(model_new$fitted.values,bodyfat$bodyfat,xlab="Fitted Values", ylab="Bodyfat",col=10,pch=19)
abline(lsfit(model_new$fitted.values,bodyfat$bodyfat),lwd=2)



# 5 Added Variable Plots
library(car)
par(mfrow=c(2,2))
avPlots(model_new,terms=~.,ask=FALSE,pch=19)



# 6 Response Vs Fitted
par(mfrow = c(2,2))
plot(model_new)



#7 Marginal Model Plots
par(mfrow = c(1,1))
mmp(model_new)



#8 Variance Inflation Factors
vif(model_new)


#9 Conclusion