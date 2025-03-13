# Install jsonlite if not already installed
install.packages("jsonlite", repos="https://cran.rstudio.com/")

# Load the library
library(jsonlite)

# Read the JSON file
data <- fromJSON(readLines("storage.json", warn = FALSE, encoding = "UTF-8"))


# View the data
print(paste("A média de insumos das culturas é ", mean(data$insumos)))
print(paste("A média de area das culturas é ", mean(data$area_total)))

print(summary(data[, c("area_total", "insumos")]))

cat("\n")


# Basic Statistics
for(coluna in names(data)){

  # Select Column Values
  values <- data[[coluna]]
  
  if(is.numeric(values)){
    cat("Estatísticas para", coluna, ":\n")
    
    # Count total values
    count <- length(values)
    
    # Count values not NA
    count_not_na <- sum(!is.na(values))
    
    # Count values NA
    count_na <- sum(is.na(values))
    
    # min max values
    min_value <- min(values, na.rm = TRUE)
    max_value <- max(values, na.rm = TRUE)
    
    # STD
    std <- sd(values, na.rm = TRUE)
    
    # Quartis (25%, 50% and 75%)
    quartis <- quantile(values, probs = c(0.25, 0.5, 0.75), na.rm = TRUE)
    
    # Mean
    media <- mean(values, na.rm = TRUE)
    
    # Results
    cat("Média:", media, "\n")
    cat("Contagem:", count, "\n")
    cat("Contagem Não Nulos:", count_not_na, "\n")  
    cat("Contagem Nulos:", count_na, "\n")
    cat("Min:", min_value, "\n")
    cat("Max:", max_value, "\n")
    cat("Desvio Padrão:", std, "\n")
    cat("Quartis:\n")
    print(quartis)
  } else {
    # Non numeric columns:
    cat("Informações para", coluna, ":\n")
    
    # Count Total
    count <- length(values)
    
    # Count NA and not NA
    count_na <- sum(is.na(values))
    count_not_na <- sum(!is.na(values))
    
    # Unique Values
    unique_obs <- length(unique(values))
    unique_values <- unique(values)
    
    # Results
    cat("Contagem:", count, "\n")
    cat("Contagem Nulos (NA):", count_na, "\n")
    cat("Contagem Não Nulos:", count_not_na, "\n")
    cat("Observações Únicas:", unique_obs, "\n")
    cat("Valores Únicos:", paste(unique_values, collapse = ", "), "\n")
  }
  cat("\n")
}


