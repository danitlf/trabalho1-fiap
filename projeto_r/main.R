# Install jsonlite if not already installed
install.packages("jsonlite", repos="https://cran.rstudio.com/")

# Load the library
library(jsonlite)

# Read the JSON file
data <- fromJSON(readLines("/Users/daniel.lima/Documents/fiap/trabalho_1/projeto_r/storage.json", warn = FALSE, encoding = "UTF-8"))


# View the data
print(paste("A média de insumos das culturas é ", mean(data$insumos)))
print(paste("A média de area das culturas é ", mean(data$area_total)))

print(summary(data[, c("area", "insumos")]))

