dwaste <- read.csv("/home/thomas/git/datascience/MSDataSci/MATH550/data/dwaste.csv", header=TRUE)
# removing Day
dwaste <- subset(dwaste, select=-c(Day))
attach(dwaste)
pairs(O2UP~., data = dwaste)
# Already, I see that a transformation of at least the O2UP variable might be needed.
# This assupmtion is just based onvisual inspectiona and will be investigated later.

model <- lm(O2UP ~., data=dwaste)
summary(model)
# Running a full summary of a linear model now doesnot give us the best R-squared value.
# Let's try a transform...

library(car)
par(mfrow = c(1,1))
invResults <- invResPlot(model)
# The Inverse response plot picked out a visually appropriate lambda-hat of about 0.04
# to use as an exponent int he power transform for O2UP

# assigning lambda-hat to a variable
lambdaHat <- invResults$lambda[1]
p1 <- powerTransform(O2UP ~.,data=dwaste)

# transforming O2UP
dwaste$O2UP <- dwaste$O2UP^lambdaHat
dwaste
attach(dwaste)
pairs(O2UP~., data = dwaste)
# The new pairs plot looks much better. Now, a rough linear relationship can be seen
# between O2UP and the predictors. 

model <- lm(O2UP ~., data=dwaste)
summary(model)
# The adjusted R-squared value for the new power-transformed model is a lot better.

# In the problem summary (and as can be seen in the new pairs plot),
# it alluded that there were several predictors that coud be correlated.
# because of this, Iwill perform backwards step AIC and BIC to reduce the
# number of predictors and potential multicollinearity
n <- length(model$residuals)
backAIC  <- step(model,direction="backward", data=dwaste)
backBIC  <- step(model,direction="backward", data=dwaste, k=log(n))
# The step model results driven by AIC give us back TKN, TS, and COD as the best predictors
# For BIC, I am given TS and COD
# Since there are already so few terms, the BIC approach might not be completely necessary
# It might be better to evaluate the models for each before making a decision on the best

# AIC
model <- lm(O2UP~TKN+TS+COD, data=dwaste)
summary(model)
# BIC
model <- lm(O2UP~TS+COD, data=dwaste)
summary(model)
pairs(O2UP~TKN+TS+COD, data = dwaste)
# While the AIC has an additional term, the R-squared is slightly higher than using BIC
# When I go back to look at the problem statement, it does not specifically mention
# any previously understood relationship between TKN, TS, and COD.
# This suggests that perhaps the span of these three predictors will still be appropriate 
# for a model. So, I will beusing the predictors given to us by the AIC step results. 



library(alr4)
par(mfrow = c(2,2))
mmp(model)
mmp(model,TKN)
mmp(model,TS)
mmp(model,COD)
# the Marginal Model plots for the model and the individual predictors
# look good. The data tracks well with the proposed model


StanRes <- rstandard(model)
par(mfrow = c(2,2))
plot(TKN,StanRes, ylab="Standardized Residuals",pch=19,col=10)
abline(h=0,lwd=2)
plot(TS,StanRes, ylab="Standardized Residuals",pch=19,col=10)
abline(h=0,lwd=2)
plot(COD,StanRes, ylab="Standardized Residuals",pch=19,col=10)
abline(h=0,lwd=2)
# The standard residuals also are looking nice and flat.

# If I had to investigate the model further, I would look into a log transform of O2UP
# instead of just a power transform. Also, there are a few points that look like they might be 
# providing much more leverage than others and may need to be addressed.

