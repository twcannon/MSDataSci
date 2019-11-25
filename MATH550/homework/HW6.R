library(car)
library(alr4)

heart <- read.csv("/home/thomas/git/datascience/MSDataSci/MATH550/data/heart.csv",header=TRUE)
attach(heart)

#Change Absent/Present to 0/1 in famhist
lookup <- c("Absent" = 0, "Present" = 1)
heart$famhist <- lookup[heart$famhist]
attach(heart)
heart 
 
#1
#A pairs plot showing the relationships between the pairs of quantitative predictors.  
#Color the plot so that there is one color for patients with heart disease 
#and one color for those without heart disease.
 
group <- NA
group[heart$chd == 0] <- 1
group[heart$chd == 1] <- 2
 
 
pairs(chd~sbp+tobacco+ldl+adiposity+typea+obesity+alcohol+age+famhist,heart,
      col = c("black", "red")[group],pch = c(8, 18)[group],main = "Heart Disease Data with CHD")
 
#2
#Look at boxplots for the predictors versus chd.  
#Are any badly skewed to the right?  
#If so, consider log-transforming these variables.  
#For some variable with possible zero values, you made need to add a small constant 
#such as 0.01 to the values before taking logs.  
 
par(mfrow=c(3,3))
#SBP is Skewed
boxplot(sbp~chd, ylab="Systolic Blood Pressure",xlab=" CHD? (0=No, 1=Yes)",col=10, pch=19)
#Tobacco is Skewed and has 0
boxplot(tobacco~chd, ylab="Tobacco Use",xlab="CHD? (0=No, 1=Yes)",col=10, pch=19)
#LDL is Skewed
boxplot(ldl~chd, ylab="Low-Densty Lipid Level",xlab=" CHD? (0=No, 1=Yes)",col=10, pch=19)
boxplot(adiposity~chd, ylab="Adiposity",xlab=" CHD? (0=No, 1=Yes)",col=10, pch=19)
boxplot(typea~chd, ylab="Measure of Anxiety",xlab=" CHD? (0=No, 1=Yes)",col=10, pch=19)
#Obesity is skewed
boxplot(obesity~chd, ylab="Obesity",xlab=" CHD? (0=No, 1=Yes)",col=10, pch=19)
#Alcohol looks skewed and has 0 values
boxplot(alcohol~chd, ylab="Alcohol",xlab=" CHD? (0=No, 1=Yes)",col=10, pch=19)
#There's an issue with Family history because it's a binary measure
boxplot(famhist~chd, ylab="Family History",xlab=" CHD? (0=No, 1=Yes)",col=10, pch=19)
 
 
 
#Add 0.01 to Tobacco,alcohol
tobacco <- tobacco+0.01
alcohol <- alcohol+0.01
#Log Transform sbp,tobacco,ldl,obesity,alcohol
sbp<-log(sbp)
tobacco <- log(tobacco)
ldl<-log(ldl)
obesity<-log(obesity)
alcohol<-log(alcohol)
typea<-log(typea)
par(mfrow=c(3,3))
#SBP is Skewed
boxplot(sbp~chd, ylab="Systolic Blood Pressure",xlab=" CHD? (0=No, 1=Yes)",col=10, pch=19)
#Tobacco is Skewed and has 0
boxplot(tobacco~chd, ylab="Tobacco Use",xlab=" CHD? (0=No, 1=Yes)",col=10, pch=19)
#LDL is Skewed
boxplot(ldl~chd, ylab="Low-Densty Lipid Level",xlab=" CHD? (0=No, 1=Yes)",col=10, pch=19)
boxplot(adiposity~chd, ylab="Adiposity",xlab=" CHD? (0=No, 1=Yes)",col=10, pch=19)
boxplot(typea~chd, ylab="Measure of Anxiety",xlab=" CHD? (0=No, 1=Yes)",col=10, pch=19)
#Obesity is skewed
boxplot(obesity~chd, ylab="Obesity",xlab=" CHD? (0=No, 1=Yes)",col=10, pch=19)
#Alcohol looks skewed and has 0 values
boxplot(alcohol~chd, ylab="Alcohol",xlab=" CHD? (0=No, 1=Yes)",col=10, pch=19)
#There's an issue with Family history because it's a binary measure
###boxplot(famhist~chd, ylab="Family History",xlab=" CHD? (0=No, 1=Yes)",col=10, pch=19)
 
#3
#full model that leaves out famhist
m1 <- glm(chd~sbp+tobacco+ldl+adiposity+typea+obesity+alcohol+age,family=binomial(),data=heart)
summary(m1)
#full model with all interactions
m1 <- glm(chd~sbp+tobacco+ldl+adiposity+typea+obesity+alcohol+age+famhist+
            sbp*tobacco+
            sbp*ldl+
            sbp*adiposity+
            sbp*tobacco+
            sbp*typea+
            sbp*obesity+
            sbp*alcohol+
            sbp*age+
            sbp*famhist+
            famhist*tobacco+
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
#Variable Reduction
n <- length(m1$residuals)
#BIC gives a score of 509.84 and 6 variables
backBIC  <- step(m1,direction="backward", heart=heart, k=log(n))
#AIC gives us a score of 478.07 and 11 variables
backAIC  <- step(m1,direction="backward", heart=heart)
 
#Reduced Model
BICModel <- glm(chd ~ tobacco + ldl + typea + age + famhist + ldl:famhist,family=binomial(),data=heart)
summary(BICModel)
AICModel <- glm(chd ~ tobacco + ldl + adiposity + typea + obesity + alcohol + 
                  age + famhist + ldl:famhist + adiposity:famhist + alcohol:famhist + 
                  age:famhist + tobacco:typea + tobacco:alcohol + adiposity:obesity + 
                  adiposity:alcohol + typea:alcohol,family=binomial(),data=heart)
summary(AICModel)
reducedModel<-BICModel
 
 
#5
#Marginal Model Plots and Hosmer-Lemeshow
par(mfrow = c(3,2))
mmp(reducedModel)
mmp(reducedModel,tobacco)
mmp(reducedModel,ldl)
mmp(reducedModel,typea)
mmp(reducedModel,age)
#Issue with this mmp
mmp(reducedModel,famhist)

 
 
library(ResourceSelection)
hoslem.test(chd, fitted(AICModel), g=10)
hoslem.test(chd, fitted(BICModel), g=10)
hoslem.test(chd, fitted(reducedModel), g=10)
 
#6
#Create a confusion matrix

