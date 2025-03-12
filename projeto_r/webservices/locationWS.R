# install.packages(c("plumber", "httr", "jsonlite"))

library(plumber)
library(httr)
library(jsonlite)

get_location <- function(cidade = "") {
    if (cidade == "") {
        return(list(error = "Cidade não informada"))
    }
    
    url <- paste0("https://nominatim.openstreetmap.org/search?q=", 
                    URLencode(cidade), "&format=json&limit=1")
    
    response <- GET(url, user_agent("MeuWebServiceR/1.0"))
    
    content <- fromJSON(content(response, as = "text"), flatten = TRUE)
    
    if (length(content) == 0) { 
        return(list(error = "Cidade não encontrada"))
    }
    
    lat <- content$lat[1]
    lon <- content$lon[1]
    
    return(list(cidade = cidade, latitude = as.numeric(lat), longitude = as.numeric(lon)))
}
