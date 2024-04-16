library(assertthat)
setwd("G:/Shared drives/CatalystRPA/Technifutur/Cours 09-2021/Exercices/Exercice 2/Resolution/UIPath/")
getwd()

mydate <- as.character(Sys.time())
myrandom <- rnorm(1)

parameter_names <- c("Date", "Random")
parameter_values <- c(mydate, myrandom)
params <- data.frame(cbind(parameter_names, parameter_values), stringsAsFactors = F)
write.csv(params, "integrationtest.csv", row.names=F)

assert_that("integrationtest.csv" %in% list.files(), msg="No file found")

system('"C:/Users/gauth/AppData/Local/UiPath/app-21.4.3/UiRobot.exe" -f "G:/Shared drives/CatalystRPA/Technifutur/Cours 09-2021/Exercices/Exercice 2/Resolution/UIPath/integration.xaml"')



