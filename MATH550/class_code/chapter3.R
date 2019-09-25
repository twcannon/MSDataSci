#  Sheather Chapter 3 Examples.

anscombe <- read.table("/Users/jonesm/Desktop/SheatherData/anscombe.txt",header=TRUE)
attach(anscombe)
head(anscombe)

#Figure 3.1 on page 46
par(mfrow=c(2,2))
plot(x1,y1,xlim=c(4,20),ylim=c(3,14),main="Data Set 1",pch=19,col=10)
abline(lsfit(x1,y1),lwd=2)
plot(x2,y2,xlim=c(4,20),ylim=c(3,14),main="Data Set 2",pch=19,col=11)
abline(lsfit(x2,y2),lwd=2)
plot(x3,y3,xlim=c(4,20),ylim=c(3,14),main="Data Set 3",pch=19,col=12)
abline(lsfit(x3,y3),lwd=2)
plot(x4,y4,xlim=c(4,20),ylim=c(3,14),main="Data Set 4",pch=19,col=10)
abline(lsfit(x4,y4),lwd=2)

#Regression output on page 47
m1 <- lm(y1~x1)
summary(m1)
m2 <- lm(y2~x2)
summary(m2)
m3 <- lm(y3~x3)
summary(m3)
m4 <- lm(y4~x4)
summary(m4)

#Figure 3.2 on page 48
par(mfrow=c(2,2))
plot(x1,m1$residuals,ylab="Residuals",xlim=c(4,20),ylim=c(-3.5,3.5),main="Data Set 1",pch=19)
abline(h=0,lwd=2)
plot(x2,m2$residuals,ylab="Residuals",xlim=c(4,20),ylim=c(-3.5,3.5),main="Data Set 2",pch=19)
abline(h=0,lwd=2)
plot(x3,m3$residuals,ylab="Residuals",xlim=c(4,20),ylim=c(-3.5,3.5),main="Data Set 3",pch=19)
abline(h=0,lwd=2)
plot(x4,m4$residuals,ylab="Residuals",xlim=c(4,20),ylim=c(-3.5,3.5),main="Data Set 4",pch=19)
abline(h=0,lwd=2)

#Figure 3.3 on page 50
par(mfrow=c(1,2))
plot(x2,y2,,ylim=c(3,10),pch=19,col=10)
abline(lsfit(x2,y2),lwd=2)
plot(x2,m2$residuals,ylab="Residuals",ylim=c(-2,2),main="Data Set 2",pch=19,col=10)
abline(h=0,lwd=2)

detach(anscombe)


huber <- read.table("/Users/jonesm/Desktop/SheatherData/huber.txt",header=TRUE)
attach(huber)
head(huber)

#Regression output on page 54
mBad <- lm(YBad~x)
summary(mBad)
mGood <- lm(YGood~x)
summary(mGood)

#Figure 3.7 on page 55
par(mfrow=c(1,2))
plot(x,YBad,ylim=c(-12,3),pch=19,col=10)
abline(lsfit(x,YBad),lwd=2)
plot(x,YGood,ylim=c(-12,3),pch=19,col=11)
abline(lsfit(x,YGood),lwd=2)

#Leverage values in Table 3.3 on page 57
lm.influence(mBad)$hat
lm.influence(mGood)$hat

#Regression output and Figure 3.8 on page 58
xq <- x^2
mBadq <- lm(YBad~x+I(x^2))
summary(mBadq)
xx <- c(-4:10)
yy <- summary(mBadq)$coef[1] + summary(mBadq)$coef[2]*xx + summary(mBadq)$coef[3]*xx^2
par(mfrow=c(1,1))
plot(xx,yy,ylim=c(-3,3),type="l",ylab="YBad",xlab="x",lwd=2)
points(x,YBad,pch=19,col=10)

detach(huber)

# Long Jump Data
library(Stat2Data)
data(LongJumpOlympics2016)
jump<-LongJumpOlympics2016
head(jump)
plot(Gold~Year,data=jump,col="darkgreen",pch=19)
jump.lm<-lm(Gold~Year,data=jump)
abline(jump.lm,lwd=2)
summary(jump.lm)
plot(jump.lm$residuals~jump.lm$fitted.values,pch=19,col=12)
abline(h=0,lwd=2)
par(mfrow=c(2,2))
plot(jump.lm,which=c(1,2,3,4),pch=19,col=10)
plot(jump.lm,pch=19,col=12)
lm.influence(jump.lm)$hat
jump[16,]
library(MASS)
stu<-studres(jump.lm)
standres<-stdres(jump.lm)
stu[16]
standres[16]
par(mfrow=c(1,1))
plot(stu~jump$Year,col="purple",pch=19)
abline(h=2,lty=2,lwd=2)
abline(h=3,lty=2,lwd=2)
abline(h=-1,lty=2,lwd=2)

# Palm Beach Election Data
data(PalmBeach)
palm<-PalmBeach
head(palm)
plot(Buchanan~Bush,data=palm,col="purple",pch=19)
palm.lm<-lm(Buchanan~Bush,data=palm)
abline(palm.lm,lwd=2)
plot(palm.lm$residuals~palm.lm$fitted.values,pch=19,col=12)
abline(h=0,lwd=2)
plot(Buchanan~Bush,data=palm,col="purple",pch=19)
abline(palm.lm,lwd=2)
palm.lm2<-lm(Buchanan~Bush,data=palm[-50,])
abline(palm.lm2,lwd=2,lty=2)
summary(palm.lm)
summary(palm.lm2)
stu<-studres(palm.lm)
standres<-stdres(palm.lm)
stu[50]
standres[50]


bonds <- read.table("/Users/jonesm/Desktop/SheatherData/bonds.txt",header=TRUE)
attach(bonds)
head(bonds)

#Figure 3.9 on page 63
par(mfrow=c(1,1))
plot(CouponRate,BidPrice,xlab="Coupon Rate (%)", ylab="Bid Price ($)",ylim=c(85,120),
     xlim=c(2,14),pch=19,col=10)
abline(lsfit(CouponRate,BidPrice),lwd=2)

#Regression output on page 63
m1 <- lm(BidPrice~CouponRate)
summary(m1)

#95% confidence intervals on page 63
round(confint(m1,level=0.95),3)

#Table 3.4 on page 62
leverage1 <- hatvalues(m1)
StanRes1 <- rstandard(m1)
residual1 <- m1$residuals
cbind(Case,CouponRate,BidPrice,round(leverage1,3),round(residual1,3),round(StanRes1,3))

#Figure 3.10 on page 64
plot(CouponRate,StanRes1,xlab="Coupon Rate (%)", ylab="Standardized Residuals",
     xlim=c(2,14),pch=19,col=10)
abline(h=2,lty=2,lwd=2)
abline(h=-2,lty=2,lwd=2)
identify(CouponRate,StanRes1,Case)
# Click near a point to identify its Case.
# This continues until you select "Stop" after clicking the right mouse button.

#Regression output on page 66
m2 <- update(m1, subset=(1:35)[-c(4,13,35)])
summary(m2)
confint(m2)

#Figure 3.11 on page 65
plot(CouponRate[-c(4,13,35)],BidPrice[-c(4,13,35)],xlab="Coupon Rate (%)",pch=19,col=10,
     ylab="Bid Price ($)",ylim=c(85,120),xlim=c(2,14),main="Regular Bonds")
abline(m2,lwd=2)

#Figure 3.12 on page 67
StanRes2 <- rstandard(m2)
plot(CouponRate[-c(4,13,35)],StanRes2,xlab="Coupon Rate (%)",pch=19,col=10,
     ylab="Standardized Residuals",xlim=c(2,14),main="Regular Bonds")
abline(h=2,lty=2,lwd=2)
abline(h=-2,lty=2,lwd=2)
identify(CouponRate[-c(4,13,35)],StanRes2,Case[-c(4,13,35)])

#Figure 3.13 on page 68
cd1 <- cooks.distance(m1)
plot(CouponRate,cd1,xlab="Coupon Rate (%)", ylab="Cook's Distance",pch=19,col=10)
abline(h=4/(35-2),lty=2,lwd=2)
identify(CouponRate,cd1,Case)
# Click near a point to identify its Case.
# This continues until you select "Stop" after clicking the right mouse button.

detach(bonds)


production <- read.table("/Users/jonesm/Desktop/SheatherData/production.txt",header=TRUE)
attach(production)
head(production)

m1 <- lm(RunTime~RunSize)

#Figure 3.14 on page 70
par(mfrow=c(2,2))
plot(m1,pch=19,col=10)

detach(production)

cleaning <- read.table("/Users/jonesm/Desktop/SheatherData/cleaning.txt",header=TRUE)
attach(cleaning)
head(cleaning)

#Figure 3.15 on page 71
par(mfrow=c(1,1))
plot(Crews,Rooms,xlab="Number of Crews",ylab="Number of Rooms Cleaned",pch=19,col=11)
abline(lsfit(Crews,Rooms),lwd=2)

#Regression output on pages 72 and 73
m1 <- lm(Rooms~Crews)
summary(m1)
predict(m1,newdata=data.frame(Crews=c(4,16)),interval="prediction",level=0.95)

#Figure 3.16 on page 73
StanRes1 <- rstandard(m1)
plot(Crews,StanRes1,xlab="Number of Crews", ylab="Standardized Residuals",pch=19,col=12)
abline(h=0,lwd=2)

#Figure 3.17 on page 74
sabs <- sqrt(abs(StanRes1))
plot(Crews,sabs,xlab="Number of Crews", ylab="Square Root(|Standardized Residuals|)",
     pch=19,col=11)
abline(lsfit(Crews,sabs),lwd=2)

#Figure 3.18 on page 75
par(mfrow=c(2,2))
plot(m1,pch=19,col=10,lwd=2)

#Figure 3.19 on page 75
sqrt(tapply(Rooms,Crews,var))
sds <- c(3.000000,4.966555,4.690416,6.642665,7.927123,7.28991,12.000463)
xx <- c(2,4,6,8,10,12,16)
par(mfrow=c(1,1))
plot(xx,sds,xlab="Number of Crews", ylab="Standard deviation(Rooms Cleaned)",
     pch=19)
abline(lsfit(xx,sds),lwd=2)

#Regression output on page 77
sqrtcrews <- sqrt(Crews)
sqrtrooms <- sqrt(Rooms)
boxplot(Crews,Rooms,col=10,pch=19)
boxplot(sqrtcrews,sqrtrooms,col=10,pch=19)
m2 <- lm(sqrtrooms~sqrtcrews)
summary(m2)
(predict(m2,newdata=data.frame(sqrtcrews=c(2,4)),interval="prediction",level=0.95))^2
predict(m1,newdata=data.frame(Crews=c(4,16)),interval="prediction",level=0.95)

#Figure 3.20 on page 78
par(mfrow=c(1,2))
plot(sqrt(Crews),sqrt(Rooms),xlab="Square Root(Number of Crews)",
     ylab="Square Root(Number of Rooms Cleaned)",pch=19,col=10)
abline(lsfit(sqrt(Crews),sqrt(Rooms)),lwd=2)
StanRes2 <- rstandard(m2)
plot(sqrtcrews,StanRes2,xlab="Square Root(Number of Crews)", 
     ylab="Standardized Residuals",pch=19,col=10)
abline(h=0,lwd=2)

#Figure 3.21 on page 78
par(mfrow=c(2,2))
plot(m2,pch=19)

detach(cleaning)


confood1 <- read.table("/Users/jonesm/Desktop/SheatherData/confood1.txt",header=TRUE)
attach(confood1)
head(confood1)

#Figure 3.22 on page 80
par(mfrow=c(1,1))
plot(Price,Sales,pch=19,col=9)
abline(lsfit(Price,Sales),lwd=2)

#Figure 3.23 on page 81
plot(log(Price),log(Sales),xlab="log(Price)",ylab="log(Sales)",pch=19,col=10)
abline(lsfit(log(Price),log(Sales)),lwd=2)

#Regression output on page 82
m1 <- lm(log(Sales)~log(Price))
summary(m1)

#Figure 3.24 on page 82
StanRes1 <- rstandard(m1)
plot(log(Price),StanRes1,xlab="log(Price)", ylab="Standardized Residuals",pch=19,col=10)
abline(h=0,lwd=2)
par(mfrow=c(2,2))
plot(m1,pch=19,col=10,which=c(1,2,3,4))
influence.measures(m1)

detach(confood1)

# Mammal Brain Data
library(MASS)
data(mammals)
head(mammals)
par(mfrow=c(1,1))
plot(brain~body,pch=19,col=12,data=mammals)
brain.lm1<-lm(brain~body,data=mammals)
abline(brain.lm1,lwd=2)
plot(log(brain)~log(body),data=mammals,pch=19,col=11)
brain.lm2<-lm(log(brain)~log(body),data=mammals)
abline(brain.lm2,lwd=2)
summary(brain.lm2)
par(mfrow=c(2,2))
plot(brain.lm2,which=c(1,2,3,4),col=12,pch=19)
beta1hat<-brain.lm2$coefficients[2]
beta1hat
2^beta1hat

# Inverse Response Plot Example.

responsetransformation <- read.table("/Users/jonesm/Desktop/SheatherData/responsetransformation.txt",header=TRUE)
attach(responsetransformation)

#Figure 3.25 on page 84
par(mfrow=c(1,1))
plot(x,y,pch=19,col=10)

#Figure 3.26 on page 85
m1 <- lm(y~x)
par(mfrow=c(1,2))
StanRes1 <- rstandard(m1)
absrtsr1 <- sqrt(abs(StanRes1))
plot(x,StanRes1,ylab="Standardized Residuals",pch=19,col=10)
plot(x,absrtsr1,ylab="Square Root(|Standardized Residuals|)",pch=19,col=10)

#Figure 3.27 on page 86
par(mfrow=c(3,2))
plot(density(y,bw="SJ",kern="gaussian"),type="l",
     main="Gaussian kernel density estimate",xlab="y")
rug(y)
boxplot(y,ylab="Y")
qqnorm(y, ylab = "Y")
qqline(y, lty = 2, col=2)
sj <- bw.SJ(x,lower = 0.05, upper = 100)
plot(density(x,bw=sj,kern="gaussian"),type="l",
     main="Gaussian kernel density estimate",xlab="x")
rug(x)
boxplot(x,ylab="x")
qqnorm(x, ylab = "x")
qqline(x, lty = 2, col=2)

#Figure 3.28 on page 87

library(car)
par(mfrow=c(1,1))
invResPlot(m1,key=TRUE)


#Figure 3.29 on page 88
invResPlot(m1,lam=c(-1,-0.5, -0.33, -0.25, 0, 0.25, 0.33, 0.5,1))
lambda <- c(-1,-0.5, -0.33, -0.25, 0, 0.25, 0.33, 0.5,1)
RSS <- c(46673.9,24090.7,15264.2,11637.1,3583.8,440,266,880.2,7136.9)
plot(lambda,RSS,type="l",ylab=expression(RSS(lambda)),xlab=expression(lambda),lwd=2)

#Figure 3.30 on page 92
library(MASS)
par(mfrow=c(1,2))
boxcox(m1,lambda=seq(0.28,0.39,length=20))
boxcox(m1,lambda=seq(0.325,0.34,length=20))

#Regression output & Figure 3.31 on page 93
ty <- y^(1/3)
par(mfrow=c(2,2))
sj <- bw.SJ(ty,lower = 0.05, upper = 100)
plot(density(ty,bw=sj,kern="gaussian"),type="l",
     main="Gaussian kernel density estimate",xlab=expression(Y^(1/3)))
rug(ty)
boxplot(ty,ylab=expression(Y^(1/3)))
qqnorm(ty, ylab = expression(Y^(1/3)))
qqline(ty, lty = 2, col=2)
m2 <- lm(ty~x)
plot(x,ty,ylab=expression(Y^(1/3)))
abline(m2)
summary(m2)

detach(responsetransformation)


##  Government Salay Data
salarygov<-read.table("/Users/jonesm/Desktop/SheatherData/salarygov.txt",header=T)
attach(salarygov)
head(salarygov)

#Figure 3.32 on page 96
m1 <- lm(MaxSalary~Score)
par(mfrow=c(2,2))
plot(Score,MaxSalary,pch=19,col=10)
abline(m1,lty=2,lwd=2)
StanRes1 <- rstandard(m1)
absrtsr1 <- sqrt(abs(StanRes1))
plot(Score,StanRes1,ylab="Standardized Residuals",pch=19,col=10)
abline(h=0,lwd=2)
plot(Score,absrtsr1,ylab="Square Root(|Standardized Residuals|)",pch=19,col=10)
abline(lsfit(Score,absrtsr1),lty=2,lwd=2)

#Output from R on page 96
salary.lm<-lm(MaxSalary~Score)
summary(salary.lm)
par(mfrow=c(1,1))
library(MASS)
boxcox(MaxSalary~1)
boxcox(Score~1)
par(mfrow=c(1,1))
library(car)
powerTransform(MaxSalary~1)
powerTransform(Score~1)
powerTransform(cbind(MaxSalary,Score)~1)


#Figure 3.33 on page 97

par(mfrow=c(3,2))
plot(density(MaxSalary,bw="SJ",kern="gaussian"),type="l",
     main="Gaussian kernel density estimate",xlab="MaxSalary")
rug(MaxSalary)
boxplot(MaxSalary,ylab="MaxSalary")
qqnorm(MaxSalary, ylab = "MaxSalary")
qqline(MaxSalary, lty = 2, col=2)
plot(density(Score,bw="SJ",kern="gaussian"),type="l",
     main="Gaussian kernel density estimate",xlab="Score")
rug(Score)
boxplot(Score,ylab="Score")
qqnorm(Score, ylab = "Score")
qqline(Score, lty = 2, col=2)

#Figure 3.34 on page 97
par(mfrow=c(1,1))
plot(sqrt(Score),log(MaxSalary),xlab=expression(sqrt(Score)),col=10,pch=19)
abline(lsfit(sqrt(Score),log(MaxSalary)),lty=2,lwd=2)

#Figure 3.35 on page 98
par(mfrow=c(3,2))
plot(density(log(MaxSalary),bw="SJ",kern="gaussian"),type="l",
     main="Gaussian kernel density estimate",xlab="log(MaxSalary)")
rug(log(MaxSalary))
boxplot(log(MaxSalary),ylab="log(MaxSalary)")
qqnorm(log(MaxSalary), ylab = "log(MaxSalary)")
qqline(log(MaxSalary), lty = 2, col=2)
sj <- bw.SJ(sqrt(Score),lower = 0.05, upper = 100)
plot(density(sqrt(Score),bw=sj,kern="gaussian"),type="l",
     main="Gaussian kernel density estimate",xlab=expression(sqrt(Score)))
rug(sqrt(Score))
boxplot(sqrt(Score),ylab=expression(sqrt(Score)))
qqnorm(sqrt(Score), ylab=expression(sqrt(Score)))
qqline(sqrt(Score), lty = 2, col=2)

#Figure 3.36 on page 99
m2 <- lm(log(MaxSalary)~sqrt(Score))
par(mfrow=c(1,2))
StanRes2 <- rstandard(m2)
absrtsr2 <- sqrt(abs(StanRes2))
plot(sqrt(Score),StanRes2,ylab="Standardized Residuals",xlab=expression(sqrt(Score)),pch=19,col=10)
plot(sqrt(Score),absrtsr2,ylab="Square Root(|Standardized Residuals|)",xlab=expression(sqrt(Score)),pch=19,col=10)
abline(lsfit(sqrt(Score),absrtsr2),lty=2,lwd=2)



#Figure 3.37 on page 100
m3 <- lm(MaxSalary~sqrt(Score))
par(mfrow=c(1,1))
library(car)
invResPlot(m3,key=TRUE,pch=19,col=10)
#Click on the plot where you want to put the legend

#Figure 3.38 on page 101
par(mfrow=c(2,2))
plot(density(MaxSalary^-0.25,bw="SJ",kern="gaussian"),type="l",
     main="Gaussian kernel density estimate",xlab=expression(MaxSalary^-0.25),col=10,pch=19)
rug(MaxSalary^-0.25)
boxplot(MaxSalary^-0.25,ylab=expression(MaxSalary^-0.25),col=10,pch=19)
qqnorm(MaxSalary^-0.25,ylab=expression(MaxSalary^-0.25),col=10,pch=19)
qqline(MaxSalary^-0.25,lty=2,lwd=2)

#Figure 3.39 on page 102
par(mfrow=c(2,2))
plot(sqrt(Score),MaxSalary^-0.25,xlab=expression(sqrt(Score)),ylab=expression(MaxSalary^-0.25),col=10,pch=19)
abline(lsfit(sqrt(Score),MaxSalary^-0.25),lty=2,lwd=2)
m3 <- lm(MaxSalary^-0.25~sqrt(Score))
StanRes3 <- rstandard(m3)
absrtsr3 <- sqrt(abs(StanRes3))
plot(sqrt(Score),StanRes3,ylab="Standardized Residuals",xlab=expression(sqrt(Score)),pch=19,col=10)
plot(sqrt(Score),absrtsr3,ylab="Square Root(|Standardized Residuals|)",xlab=expression(sqrt(Score)),col=10,pch=19)
abline(lsfit(sqrt(Score),absrtsr3),lty=2,lwd=2)

detach(salarygov)