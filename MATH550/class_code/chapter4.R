#March 17, 2009

#Please change the file path in the command below to coincide with where you have stored the data.
# Chapter 4 Sheather

cleaningwtd <- read.table("/Users/jonesm/Desktop/SheatherData/cleaningwtd.txt",header=TRUE)
attach(cleaningwtd)
head(cleaningwtd)

#Regression output on page 117
wm1 <- lm(Rooms~Crews,weights=1/StdDev^2)
summary(wm1)
predict(wm1,newdata=data.frame(Crews=c(4,16)),interval="prediction",level=0.95)

#Regression output on page 120
ynew <- Rooms/StdDev
x1new <- 1/StdDev
x2new <- Crews/StdDev
wm1check <- lm(ynew~x1new + x2new - 1)
summary(wm1check)
mypredict<-predict(wm1check,newdata=data.frame(x1new=c(1/4.966555,1/12.000463),x2new=c(4/4.966555,16/12.000463)),interval="prediction",level=0.95)
mypredict
mypredict[1,]*4.97
mypredict[2,]*12

detach(cleaningwtd)