# SQL querying

# Load in libraries
library(DBI)
library(RSQLite)

# Establihs connection to DB ----
# type of DB
sqlite <- dbDriver("SQLite")

# connection
con <- dbConnect(sqlite, "SQL/Comte_et_al_2016.db")
# or 
# mydb <- dbConnect(RSQLite::SQLite(), "SQL/Comte_et_al_2016.db")

# Query ----
results <- dbGetQuery(con, 'SELECT DISTINCT Basin FROM site
                      ORDER BY Basin')

# Print output
results

# Disconnect
dbDisconnect(con)


# Create db -----
mydb <- dbConnect(RSQLite::SQLite(), "")

dbWriteTable(mydb, "mt_cars", mtcars)
dbWriteTable(mydb, "iris", iris)

# Query
head(dbGetQuery(mydb, 'SELECT * FROM mt_cars LIMIT 5'))

# Make query based on user defined value
y <- 4.5
dbGetQuery(mydb, 'SELECT * FROM iris WHERE "Sepal.Length" < :x',
           # use x as defined y above 
           params = list(x = y))




