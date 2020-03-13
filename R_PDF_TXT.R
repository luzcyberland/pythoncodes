library(pdftools)
lf <- list.files(path = "C:\\Users\\VE522FZ\\OneDrive - EY\\Documents\\Concilicaciones Bancarias\\TALISMAN SA\\BBVA\\GS\\2101016022\\EXTRACTO\\PDF",full.names = TRUE)
c <- 1
'&' <- function(x, y)paste0(x,y)
for (i in lf){
  tryCatch(
    {
    txt <- pdf_text(i)
    name <-basename(i)
    write(txt,"C:\\Users\\VE522FZ\\OneDrive - EY\\Documents\\Concilicaciones Bancarias\\TALISMAN SA\\BBVA\\GS\\2101016022\\EXTRACTO\\TXT\\"&name&".txt")
    }
    , error=function(e){cat("ERROR :",conditionMessage(e), "\n")})
  c <- c+1
} 


install.packages("pdftools")
