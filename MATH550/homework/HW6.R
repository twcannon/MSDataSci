library(car)
library(alr4)
library(ResourceSelection)

heart <- read.csv("/home/thomas/git/datascience/MSDataSci/MATH550/data/heart.csv",header=TRUE)
attach(heart)

#Change Absent/Present to 0/1 in famhist
lookup <- c("Absent" = 0, "Present" = 1)
heart$famhist <- lookup[heart$famhist]
attach(heart)
heart 
 


#1
 
group <- NA
group[heart$chd == 0] <- 1
group[heart$chd == 1] <- 2

pairs(chd~sbp+tobacco+ldl+adiposity+typea+obesity+alcohol+age+famhist,heart,
      col = c("black", "red")[group],pch = c(8, 18)[group],main = "Heart Disease Data with CHD")
 


#2
 
par(mfrow=c(3,3))
# Skewed
boxplot(sbp~chd, ylab="Systolic Blood Pressure",xlab=" CHD? (0=No, 1=Yes)",col=10, pch=19)

# Skewed
boxplot(tobacco~chd, ylab="Tobacco Use",xlab="CHD? (0=No, 1=Yes)",col=10, pch=19)

# Skewed
boxplot(ldl~chd, ylab="Low-Densty Lipid Level",xlab=" CHD? (0=No, 1=Yes)",col=10, pch=19)

#Looks OK
boxplot(adiposity~chd, ylab="Adiposity",xlab=" CHD? (0=No, 1=Yes)",col=10, pch=19)

#Looks OK
boxplot(typea~chd, ylab="Measure of Anxiety",xlab=" CHD? (0=No, 1=Yes)",col=10, pch=19)

# Skewed
boxplot(obesity~chd, ylab="Obesity",xlab=" CHD? (0=No, 1=Yes)",col=10, pch=19)

# Badly Skewed
boxplot(alcohol~chd, ylab="Alcohol",xlab=" CHD? (0=No, 1=Yes)",col=10, pch=19)
 
 
 
# Add 0.001 to Tobacco and alcohol for log transforms
heart$tobacco <- tobacco+0.001
heart$alcohol <- alcohol+0.001

#Log Transform sbp,tobacco,ldl,obesity,alcohol
heart$sbp<-log(heart$sbp)
heart$tobacco <- log(heart$tobacco)
heart$ldl<-log(heart$ldl)
heart$obesity<-log(heart$obesity)
heart$alcohol<-log(heart$alcohol)
heart$typea<-log(heart$typea)
par(mfrow=c(3,3))
attach(heart)
# Skewed
boxplot(heart$sbp~chd, ylab="Systolic Blood Pressure",xlab=" CHD? (0=No, 1=Yes)",col=10, pch=19)

# Skewed
boxplot(tobacco~chd, ylab="Tobacco Use",xlab=" CHD? (0=No, 1=Yes)",col=10, pch=19)

# Skewed
boxplot(ldl~chd, ylab="Low-Densty Lipid Level",xlab=" CHD? (0=No, 1=Yes)",col=10, pch=19)

# Looks OK
boxplot(adiposity~chd, ylab="Adiposity",xlab=" CHD? (0=No, 1=Yes)",col=10, pch=19)

# Looks OK
boxplot(typea~chd, ylab="Measure of Anxiety",xlab=" CHD? (0=No, 1=Yes)",col=10, pch=19)

# Skewed
boxplot(obesity~chd, ylab="Obesity",xlab=" CHD? (0=No, 1=Yes)",col=10, pch=19)

# Skewed
boxplot(alcohol~chd, ylab="Alcohol",xlab=" CHD? (0=No, 1=Yes)",col=10, pch=19)



#3
#full model that leaves out famhist
m1 <- glm(chd~sbp+tobacco+ldl+adiposity+typea+obesity+alcohol+age,family=binomial(),data=heart)
summary(m1)
#full model with all interactions
m1 <- glm(chd~sbp+tobacco+ldl+adiposity+typea+obesity+alcohol+age+famhist+
             sbp*ldl+
             sbp*adiposity+
             sbp*tobacco+
             sbp*typea+
             sbp*obesity+
             sbp*alcohol+
             sbp*age+
             sbp*famhist+
             famhist*ldl+
             famhist*adiposity+
             famhist*tobacco+
             famhist*typea+
             famhist*obesity+
             famhist*alcohol+
             famhist*age+
             tobacco*ldl+
             tobacco*adiposity+
             tobacco*typea+
             tobacco*obesity+
             tobacco*alcohol+
             tobacco*age+
             ldl*adiposity+
             ldl*typea+
             ldl*obesity+
             ldl*alcohol+
             ldl*age+
             adiposity*typea+
             adiposity*obesity+
             adiposity*alcohol+
             adiposity*age+
             typea*obesity+
             typea*alcohol+
             typea*age+
             obesity*alcohol+
             obesity*age+
             alcohol*age
          ,family=binomial(),data=heart)
summary(m1)
 

 
#4
# Variable Reduction
n <- length(m1$residuals)

# BIC gives a score of 513.44 and 3 variables
backBIC  <- step(m1,direction="backward", heart=heart, k=log(n))

# AIC gives us a score of 480.36 and the same 3 variables
backAIC  <- step(m1,direction="backward", heart=heart)

# It is interesting to see that the significant ineraction predictors are the ones 
# that ended up in the back step models. 
 
#Reduced Model
reducedModel <- glm(chd ~ age + tobacco:typea + ldl:famhist,family=binomial(),data=heart)
summary(reducedModel)


 
#5
#Marginal Model Plots and Hosmer-Lemeshow
par(mfrow = c(2,2))
mmp(reducedModel)
mmp(reducedModel,age)
mmp(reducedModel,tobacco*typea)
mmp(reducedModel,ldl*famhist)

 
hoslem.test(chd, fitted(reducedModel), g=10)





 
#6
#Create a confusion matrix
y_hat <- predict(reducedModel, type='response')
cat(y_hat)

myPredict <- ifelse(y_hat>0.5,1,0)
cat(myPredict)
conf_matrix <- table(myPredict, heart$chd)
conf_matrix

Accuracy <- (78 + 259) / (78 + 259 + 82 + 43)
Precision <- 78 / (78 + 82)
Accuracy
Precision
