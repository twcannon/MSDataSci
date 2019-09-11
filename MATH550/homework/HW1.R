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

qt <- qt(0.975, df = num_rows - 2)
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
x_new <- 400000

predict(object = fit, data.frame(LastWeek = x_new), interval = "prediction")




#### 2.3
## a)

invoices <- read.table('../data/invoices.txt', header=TRUE)
invoices
Time <- invoices$Time
Invoices <- invoices$Invoices
num_rows <- nrow(invoices)

invoices_fit <- lm(formula = Time ~ Invoices)
invoices_summary <- summary(invoices_fit)

confint(invoices_fit)[1,]


## b)

B_1_hat <- coefficients(invoices_summary)["Invoices", "Estimate"]
B_1_error <- coefficients(invoices_summary)["Invoices", "Std. Error"]
B_1_null = 0.01
inv_t <- ( B_1_hat - B_1_null ) / B_1_error
inv_t

inv_pt <- pt(q = inv_t, lower.tail = FALSE, df = num_rows - 2)
inv_ts_test <- 2*inv_pt
inv_ts_test


## c)

inv_prediction <- predict(invoices_fit, newdata = data.frame(Invoices = 130), 
        interval = "prediction", level = 0.95)
inv_prediction

