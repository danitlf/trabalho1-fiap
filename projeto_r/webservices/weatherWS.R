# install.packages(c("plumber", "httr", "jsonlite"))

library(plumber)
library(httr)
library(jsonlite)

 
get_weather <- function(cidade, latitude, longitude){
    url <- paste0("https://api.open-meteo.com/v1/forecast?latitude=", latitude,
                "&longitude=", longitude, "&current_weather=true")

    resposta <- GET(url)

    if (status_code(resposta) == 200) {
        dados <- fromJSON(content(resposta, as = "text"))
        
        temperature <- dados$current_weather$temperature
        velocidade_vento <- dados$current_weather$windspeed
        condicao_tempo <- dados$current_weather$weathercode
        altitude <- dados$elevation
        
        condicoes <- c("Céu limpo", "Principalmente limpo", "Parcialmente nublado",
                    "Nublado", "Névoa", "Chuva fraca", "Chuva forte", "Tempestade")

        condicao_traduzida <- ifelse(condicao_tempo <= 3, condicoes[condicao_tempo + 1], 
                                    ifelse(condicao_tempo == 45 | condicao_tempo == 48, condicoes[5],
                                            ifelse(condicao_tempo >= 51 & condicao_tempo <= 67, condicoes[6],
                                                ifelse(condicao_tempo >= 80 & condicao_tempo <= 99, condicoes[7], "Desconhecido"))))

        return(list(
            city = cidade, 
            lat = as.numeric(latitude), 
            lon = as.numeric(longitude), 
            temp = temperature, 
            wind_speed = as.numeric(velocidade_vento), 
            condition = condicao_traduzida,
            elevation = altitude
        ))
    } else {
        return(list(error = "Erro ao buscar os dados meteorológicos"))
    }

}