# QUESTION 4.1

profsal <- read.csv('../data/prof_sal_third_qu.csv', header=TRUE)
# here I just use 1/(numberof samples) as the weights
profsal$weights <- 1/profsal$sample
profsal

model.profsal <- lm(thirdq~years, data=profsal, weights=profsal$weights)
# lm seems to work just fine when passing in an additional vecor for weights
summary(model.profsal)
# so the weighted least squares model is:
# thirdq = 1,517.9*(years of experience) + 103,925.6 
six.years <- 1517.9*(6) + 103925.6
six.years
# the estimate for six years of experience is $113,003




# QUESTION 5.1
overdue <- read.table('../data/overdue.txt', header=TRUE)
overdue$type <- c(rep(1,48),rep(0,48))
head(overdue)

plot(x=overdue$BILL, y=overdue$LATE)
plot(overdue$BILL[overdue$type==0],overdue$LATE[overdue$type==0],col=c("black"),ylab="LATE",xlab="BILL",ylim=c(0, 100))
points(overdue$BILL[overdue$type==1],overdue$LATE[overdue$type==1],col=c("red"))
# visually, it looks like the type variable will play a role in the final model

model.all <- lm(LATE~BILL, data=overdue)
summary(model.all)
# without considering type, the R squared is very low, indicating that this is not a very good model when we only consider the bill amount

model.sep <-lm(LATE~BILL+type, data=overdue)
summary(model.sep)
# as a quick test to tell if the type variable will be significant, we add in the variable to the model.
# with an R squared of about .63, it is much better

# the test to check if there is a difference in the mean overdue dates based on the type of account 
model.anova <- lm(LATE~type, data=overdue)
anova(model.anova)
# the p value is much less than 0.05, so it is significant
# This means that the mean number of overdue days is not equal for commercial and residental




# QUESTION 5.2
houston <- read.csv("../data/HoustonChronicle.csv",header=TRUE)
head(houston)
plot(x=houston$X.Low.income.students, y=houston$X.Repeating.1st.Grade)
plot(houston$X.Low.income.students[houston$Year==1994],houston$X.Repeating.1st.Grade[houston$Year==1994],col=c("blue"),ylab="Repeat",xlab="Low Income")
points(houston$X.Low.income.students[houston$Year==2004],houston$X.Repeating.1st.Grade[houston$Year==2004],col=c("red"))
abline(model1)

# PART A
grade.model1 <- lm(X.Repeating.1st.Grade ~ X.Low.income.students, data = houston)
summary(grade.model1)
par(mfrow=c(2,2))
plot(grade.model1)
# The fit appears good with a significant slope.

# PART B
grade.model2 <- lm(X.Repeating.1st.Grade ~ Year, data = houston)
summary(grade.model2)
plot(grade.model2)
# there is no visually discernible difference between the two populations
t.test(houston$X.Repeating.1st.Grade~houston$Year)
# a quick t test also shows that with p value of over .10, there is not a significant difference in the two populations

# PART C
grade.model3 <- lm(X.Repeating.1st.Grade ~ Year + X.Low.income.students, data = houston)
summary(grade.model3)
plot(grade.model3)

grade.model4 <- lm(X.Repeating.1st.Grade ~ X.Low.income.students + Year + X.Low.income.students:Year, data = houston)
summary(grade.model4)
plot(grade.model4)
# There is not much to show for the association between the low-income students and failure rates between the years
anova(grade.model3,grade.model4)
anova(grade.model1,grade.model4)

# It is reasonable to not consider the Year in the model, but including low-income is better than not having it. 
# The year does not influence the model, but there is an association between low-income students and higher grade repitions.