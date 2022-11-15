##############################X
#------ SQL homework 3 -------X
#--------- 11/15/2022 --------X
#----------- VAW -------------X
##############################X

# clean env
rm(list = ls())
gc()

# Load in libraries ----
library(DBI)
library(RSQLite)

## Question 1 ----
# 
# 1) (30pts) Revisiting the Lohr and Haag (2015) database, do the following after 
# opening the database called “lohr_and_haag.db”: 

# Establihs connection to DB ----
# connection
con <- dbConnect(drv = RSQLite::SQLite(), "SQL/lohr_and_haag.db")

# a) (10pts) Compute the min, max, and average reproductive output for each 
# population and output with information on what size lake each population is 
# from (large or small).  

calc <- dbGetQuery(con, 'SELECT size, AVG(ro) AS average, MIN(ro) AS min, 
                                MAX(ro) AS max FROM lohr_and_haag
                         GROUP BY size')
calc


# b) (10pts) Print out the unique populations. Delete all the records for populations 
# that start with "V" or "K" from the database. Print out the unique populations again 
# to check it worked.
unq <- dbGetQuery(con, 'SELECT DISTINCT pop FROM lohr_and_haag')
unq

del <- dbSendStatement(con, 'DELETE FROM lohr_and_haag WHERE "pop" = :x')
dbBind(del, params = list(x = "VOL", "VRI")) 

# c) (10pts) Iteratively (preferably with an implicit or explicit loop) query 
#     which populations (of those that are left) have a longer lifespan 
#      on average than 40 days, 50 days, 60 days, and 70 days. 













