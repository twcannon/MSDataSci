bodyfat <- read.csv("/home/thomas/git/datascience/MSDataSci/MATH550/data/bodyfat.csv", header=TRUE)
attach(bodyfat)
head(bodyfat)

library(car)
#powerTransform(cbind(AdPages,SubRevenue,NewsRevenue)~1)

pairs(bodyfat$bodyfat~age+weight+height+neck+chest+abdomen+hip+thigh+knee+ankle+biceps+forearm+wrist)

model <- lm(bodyfat$bodyfat~age+weight+height+neck+chest+abdomen+hip+thigh+knee+ankle+biceps+forearm+wrist)
summary(model)
par(mfrow=c(2,2))
plot(model)
vif(model)

backAIC <- step(m1,direction="backward", data=bodyfat)
backBIC <- step(m1,direction="backward", data=bodyfat, k=log(n))

