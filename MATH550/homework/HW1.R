#### 2.1
## a)
getwd()
setwd('/home/thomas/git/datascience/MSDataSci/MATH550/homework')

broadway <- read.csv('../data/playbill.csv')
broadway

CurrentWeek <- broadway$CurrentWeek
LastWeek <- broadway$LastWeek
num_rows <-nrow(broadway)

fit <- lm(formula = CurrentWeek ~ LastWeek)
summary <- summary(fit)
summary

qt <- qt(0.95, df = num_rows - 2)
qt
B_1_hat <- coefficients(summary)["LastWeek", "Estimate"]
B_1_hat
B_1_error <- coefficients(summary)["LastWeek", "Std. Error"]
B_1_error
error <- qt * B_1_error
error
lower = B_1_hat - error
upper = B_1_hat + error
lower
upper


## b)
B_0_null = 10000
B_0_hat <- coefficients(summary)["(Intercept)", "Estimate"]
B_0_error <- coefficients(summary)["(Intercept)", "Std. Error"]

t <- ( B_0_hat - B_0_null ) / B_0_error
t
pt <- pt(q = t, df = num_rows-2)
ts_test <- 2*pt
ts_test


## c)
(y_hat <- predict(object = fit))
x_star <- 400000
unname(coefficients(fit)[1] + coefficients(fit)[2]*x_star)

