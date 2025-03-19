# install.packages(c("plumber", "httr", "jsonlite"))

required_packages <- c("plumber", "httr", "jsonlite")
for (pkg in required_packages) {
    if (!require(pkg, character.only = TRUE)) {
        install.packages(pkg, dependencies = TRUE, repos="https://cran.rstudio.com/")
        library(pkg, character.only = TRUE)
    }
}

httr::set_config(httr::config(ssl_verifypeer = 0L))

args <- commandArgs(trailingOnly = TRUE)
cidade <- args[1]

source("projeto_r/webservices/weatherWS.R")
source("projeto_r/webservices/locationWS.R")


get_weather_for_location <- function(city_name) {
    location <- get_location(city_name)
    
    if (!is.null(location$error)) {
        return(list(error = "Não foi possível encontrar a localização da cidade"))
    }
    
    weather <- get_weather(city_name, location$latitude, location$longitude) 
    
    if (!is.null(weather$error)) {
        return(list(error = "Não foi possível obter os dados meteorológicos"))
    }
    
    return(list(
        city = city_name,
        latitude = location$latitude,
        longitude = location$longitude,
        temperature = weather$temp,
        wind_speed = weather$wind_speed,
        condition = weather$condition,
        elevation = weather$elevation
    ))
}
get_weather_for_location(cidade)
