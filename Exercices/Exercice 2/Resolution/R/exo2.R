starttime <- Sys.time()
a <- read.csv(r"[G:\Shared drives\CatalystRPA\Clients\Technifutur\Cours 09-2021\Exercices\Exercice 2\Resolution\R\A.csv]")
b <- read.csv(r"[G:\Shared drives\CatalystRPA\Clients\Technifutur\Cours 09-2021\Exercices\Exercice 2\Resolution\R\B.csv]")
result <- rbind(a,b) #concatenating data from both files
result$double_age <- result$Age*2
endtime <- Sys.time()
endtime-starttime
print(result)

