library(car)
library(alr4)

# 1

golf <- read.csv("/home/thomas/git/datascience/MSDataSci/MATH550/data/pgatour2006.csv",header=TRUE)
# Removing unneeded columns
golf <- subset(golf, select=-c(Name,TigerWoods,AveDrivingDistance,BounceBack))
attach(golf)
golf
pairs(PrizeMoney~., data = golf)

model_golf <- lm(PrizeMoney ~., data=golf)
summary(model_golf)
# Running a full summary of a linear model now does not give us the best R-squared value at 0.3843.
# Let's try a transform...

par(mfrow = c(1,1))
invResults_golf <- invResPlot(model_golf)
# The Inverse response plot picked out a visually appropriate lambda-hat of about 0.12
# to use as an exponent in the power transform for PrizeMoney

# assigning lambda-hat to a variable
lambdaHat_golf <- invResults_golf$lambda[1]
p1 <- powerTransform(PrizeMoney ~.,data=golf)

# Power transforming PrizeMoney
golf_power <- golf
golf_power$PrizeMoney <- golf_power$PrizeMoney^lambdaHat_golf
golf_power
attach(golf_power)
pairs(PrizeMoney~., data = golf_power)
# The power transformed pairs plot looks much better. Now, a rough linear relationship can be seen
# between PrizeMoney and the predictors with some multicollinearity. 
model_golf_power <- lm(PrizeMoney ~., data=golf_power)
summary(model_golf_power)
# The adjusted R-squared value for the new power-transformed model is a lot better at 0.5354.
# Now, let's try a Log Transformation on Prize Money


# Log transforming PrizeMoney
golf_log <- golf
golf_log$PrizeMoney <- log(golf_log$PrizeMoney)
golf_log
attach(golf_log)
pairs(PrizeMoney~., data = golf_log)
# The log transformed pairs plot looks much better. Now, a rough linear relationship can be seen
# between PrizeMoney and the predictors. 
model_golf_log <- lm(PrizeMoney ~., data=golf_log)
summary(model_golf_log)
# The adjusted R-squared value for the new log-transformed model is 0.5412.
# Although the log transformation is slightly better than the power transformation given the 
# data provided, The inverse response plot visually looks like the data would be much better
# explained by a power transformation. I will continue with the power transformation

# In the new power transformation pairs plot, there looks to be a lot of multicollinearity.
# Because of this, I will perform backwards step AIC and BIC to reduce the
# number of predictors and potential multicollinearity
n <- length(model_golf_power$residuals)
backAIC  <- step(model_golf_power,direction="backward", data=golf_power)
backBIC  <- step(model_golf_power,direction="backward", data=golf_power, k=log(n))
# The step model results driven by AIC give us back SandSaves, Scrambling, GIR, and BirdieConversion
# as the best predictors.
# For BIC, I am given Scrambling, GIR, and BirdieConversion
# Since there are already so few terms, the BIC approach might not be completely necessary
# It might be better to evaluate the models for each before making a decision on the best

# AIC
model_golf_power <- lm(PrizeMoney~SandSaves+Scrambling+GIR+BirdieConversion, data=golf_power)
summary(model_golf_power)
# BIC
model_golf_power <- lm(PrizeMoney~Scrambling+GIR+BirdieConversion, data=golf_power)
summary(model_golf_power)
pairs(PrizeMoney~SandSaves+Scrambling+GIR+BirdieConversion, data = golf_power)
# While the AIC has an additional term, the R-squared is slightly higher than using BIC, yet negligible -
# a difference between 0.5378 (AIC) and 0.5315 (BIC)
# Since I do not expect the span of the addition of another variable from the AIC method over the BIC method
# To be much larger, I will default to the predictors picked by the back step BIC method.
# I do this because, since the influence of an additional predictor is very small, I do not want to run the
# risk of overfitting the data on that extra variable now and causing the model to falter with future data.


par(mfrow = c(2,2))
mmp(model_golf_power)
mmp(model_golf_power,Scrambling)
mmp(model_golf_power,GIR)
mmp(model_golf_power,BirdieConversion)
# The Marginal Model plots for the model and the individual predictors are looking good!
# The model is tracking well wit the data. 


StanRes <- rstandard(model_golf_power)
par(mfrow = c(2,2))
plot(Scrambling,StanRes, ylab="Standardized Residuals",pch=19,col=10)
abline(h=0,lwd=2)
plot(GIR,StanRes, ylab="Standardized Residuals",pch=19,col=10)
abline(h=0,lwd=2)
plot(BirdieConversion,StanRes, ylab="Standardized Residuals",pch=19,col=10)
abline(h=0,lwd=2)
# The standard residuals also are looking nice and flat.

# If I had to investigate the model further, I would look into Outlier Detection. 
# There are a few points that look like they might be providing slightly more 
# leverage than others and may need to be addressed.






















dwaste <- read.csv("/home/thomas/git/datascience/MSDataSci/MATH550/data/dwaste.csv", header=TRUE)
# removing Day
dwaste <- subset(dwaste, select=-c(Day))
attach(dwaste)
pairs(O2UP~., data = dwaste)
# Already, I see that a transformation of at least the O2UP variable might be needed.
# This assupmtion is just based onvisual inspectiona and will be investigated later.

model <- lm(O2UP ~., data=dwaste)
summary(model)
# Running a full summary of a linear model now does not give us the best R-squared value at 0.2609.
# Let's try a transform...

par(mfrow = c(1,1))
invResults_dwaste <- invResPlot(model)
# The Inverse response plot picked out a visually appropriate lambda-hat of about 0.04
# to use as an exponent in the power transform for O2UP

# assigning lambda-hat to a variable
lambdaHat_dwaste <- invResults_dwaste$lambda[1]
p1 <- powerTransform(O2UP ~.,data=dwaste)

# Power transforming O2UP
dwaste_power <- dwaste
dwaste_power$O2UP <- dwaste_power$O2UP^lambdaHat_dwaste
dwaste_power
attach(dwaste_power)
pairs(O2UP~., data = dwaste_power)
# The new pairs plot looks much better. Now, a rough linear relationship can be seen
# between O2UP and the predictors. 
model_dwaste_power <- lm(O2UP ~., data=dwaste_power)
summary(model_dwaste_power)
# The adjusted R-squared value for the new power-transformed model is a lot better at 0.715.

# Log transforming O2UP
dwaste_log <- dwaste
dwaste_log$O2UP <- log(dwaste_log$O2UP)
dwaste_log
attach(dwaste_log)
pairs(O2UP~., data = dwaste_log)
# The new pairs plot looks much better. Now, a rough linear relationship can be seen
# between O2UP and the predictors. 
model_dwaste_log <- lm(O2UP ~., data=dwaste_log)
summary(model_dwaste_log)
# The adjusted R-squared value for the new power-transformed model is a lot better at 0.7413.
# the log-transform performs slightly better than the power transform.
# I will be continuing with the log transform model.




# In the problem summary (and as can be seen in the new pairs plot),
# it alluded that there were several predictors that coud be correlated.
# because of this, Iwill perform backwards step AIC and BIC to reduce the
# number of predictors and potential multicollinearity
n <- length(model_dwaste_log$residuals)
backAIC  <- step(model_dwaste_log,direction="backward", data=dwaste_log)
backBIC  <- step(model_dwaste_log,direction="backward", data=dwaste_log, k=log(n))
# For both the AIC and BIC bact step methods, I am given TS and COD
# This simplifies the decision making for which method to choose because they both agree. 


# AIC & BIC
model_dwaste_log <- lm(O2UP~TS+COD, data=dwaste_log)
summary(model_dwaste_log)
pairs(O2UP~TS+COD, data = dwaste_log)
# When I go back to look at the problem statement, it does not specifically mention
# any previously understood relationship between TS, and COD.
# This suggests that perhaps the span of these two predictors will still be appropriate 
# for a model. So, I will be using the predictors given to us by the AIC and BIC step results. 



par(mfrow = c(2,2))
mmp(model_dwaste_log)
mmp(model_dwaste_log,TS)
mmp(model_dwaste_log,COD)
# the Marginal Model plots for the model and the individual predictors
# look good. The data tracks well with the proposed model


StanRes <- rstandard(model_dwaste_log)
par(mfrow = c(2,2))
plot(TS,StanRes, ylab="Standardized Residuals",pch=19,col=10)
abline(h=0,lwd=2)
plot(COD,StanRes, ylab="Standardized Residuals",pch=19,col=10)
abline(h=0,lwd=2)
# The standard residuals also are looking nice and flat.

# If I had to investigate the model further, I would look into Outlier Detection.
# There are a few points that look like they might beproviding much more leverage 
# than others and may need to be addressed.
























