dwaste <- read.csv("/home/thomas/git/datascience/MSDataSci/MATH550/data/dwaste.csv", header=TRUE)
dwaste <- subset(dwaste, select=-c(Day))
dwaste
dwaste <- dwaste[-1,]
dwaste
attach(dwaste)

pairs(dwaste$O2UP~., data = dwaste)
pairs(log(dwaste$O2UP)~., data = dwaste)

# 2
model <- lm(dwaste$O2UP ~., data=dwaste)
model <- lm(log(dwaste$O2UP) ~., data=dwaste)
summary(model)

library(car)
invResPlot(model)
p1 <- powerTransform(dwaste$O2UP ~.,data=dwaste)
testTransform(p1,0.9)

n <- length(model$residuals)
backAIC  <- step(model,direction="backward", data=dwaste)
backBIC  <- step(model,direction="backward", data=dwaste, k=log(n))

pairs(dwaste$O2UP~COD, data = dwaste)

library(alr4)
mmp(model)
par(mfrow = c(2,2))
mmp(model,dwaste$BOD)
mmp(model,dwaste$TKN)
mmp(model,dwaste$TVS)
mmp(model,dwaste$COD)

StanRes <- rstandard(model)
par(mfrow=c(2,2))
plot(BOD,StanRes, ylab="Standardized Residuals",pch=19,col=10)
abline(h=0,lwd=2)
plot(TKN,StanRes, ylab="Standardized Residuals",pch=19,col=10)
abline(h=0,lwd=2)
plot(TVS,StanRes, ylab="Standardized Residuals",pch=19,col=10)
abline(h=0,lwd=2)
plot(COD,StanRes, ylab="Standardized Residuals",pch=19,col=10)
abline(h=0,lwd=2)

