##############################X
#--Programming for Ecologists-X
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
dbListTables(con)
dbListFields(con, "lohr_and_haag")
# a) (10pts) Compute the min, max, and average reproductive output for each 
# population and output with information on what size lake each population is 
# from (large or small).  

calc <- dbGetQuery(con, 'SELECT size, AVG(ro) AS mean, MIN(ro) AS min, 
                                MAX(ro) AS max FROM lohr_and_haag
                   GROUP BY size')
calc


# b) (10pts) Print out the unique populations. Delete all the records for populations 
# that start with "V" or "K" from the database. Print out the unique populations again 
# to check it worked.
unq <- dbGetQuery(con, 'SELECT DISTINCT pop FROM lohr_and_haag')
unq

del <- dbExecute(con, 'DELETE FROM lohr_and_haag WHERE pop LIKE 
                       "V%" OR pop LIKE "K%"')
del

# check
ck <- dbGetQuery(con, 'SELECT DISTINCT pop FROM lohr_and_haag')
ck

# c) (10pts) Iteratively (preferably with an implicit or explicit loop) query 
#     which populations (of those that are left) have a longer lifespan 
#      on average than 40 days, 50 days, 60 days, and 70 days. 

# ages to loop over
ages <- c(40, 50, 60, 70)
# query statement
longer <- dbSendQuery(con, 'SELECT pop, AVG(ad) FROM lohr_and_haag 
                      GROUP BY pop HAVING AVG(ad) > :x')
# loop
for(i in ages){
  
  # bind statement for above query
  dbBind(longer, params = list(x = i))
  
  # print title statement and subsequent results
  print(paste("pop with avg lifespan > ", i))
  print(dbFetch(longer))
  
  #Done
}

# Question 2 ----
# 2) (20pts) Revisiting the Comte et al. (2016) database once again, do the following 
# after opening the database called “Comte_et_al_2016.db”: 
con2 <- dbConnect(drv = RSQLite::SQLite(), "SQL/Comte_et_al_2016.db")
dbListTables(con2)
  
# a) (10pts) Join the “trans” and “site” tables using the key “SiteID” and save as a VIEW 
# called “together”. Then using a separate statement, store this VIEW. Finally print out the 
# first few lines. This should be done using SQL code within Python or R. 
together <- dbGetQuery(con2, 'SELECT * FROM trans LEFT JOIN site
                 ON trans.SiteID = site.SiteID LIMIT 10')
together

# b) (10pts) What is the count of extirpations from P1 to P2 for northern pike (lucius) 
# for each basin? This should be done using SQL code within Python or R. 
count <- dbGetQuery(con2, 'SELECT Basin, COUNT(lucius) AS luciusEXT
                    FROM together WHERE lucius = "extirpated" AND Per1 = "P1" AND Per2 = "P2"
                    GROUP BY Basin')
count

# Done!



