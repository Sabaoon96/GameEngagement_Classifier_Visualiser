# Reading in CSV file
data = read.csv("dataToConvert.csv")

# Extracting and storing "Electrode" column
singleCol = data$Electrode

# Averaging column data for every 512 rows
averagedData = colMeans(matrix(singleCol, nrow=512))

# Formatting output 
finalData = capture.output(cat('{"raw_values": [', paste(as.character(averagedData), collapse=", "), ']}'))

# Exporting and writing to JSON file
write(finalData, file = "testOutput.json")
