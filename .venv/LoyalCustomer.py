import pandas as pd
import duckdb
import glob

#Change filepath to where log files are stored.
checked_files = glob.glob('./*.txt')
li = list()
for  f in checked_files:
    df = pd.read_csv(f, sep=", ", engine = "python")
    li.append(df)
logframe = pd.concat(li, ignore_index=True)
#Forming table 
duckdb.sql("CREATE TABLE logs AS SELECT * FROM logframe")



# While complex in appearance, all this actually does is select the CustomerID from a subquery that contains every date interval from the uploaded 
# logs with an interval of 1 day (meaning they were active on two consecutive days - the "start" and "end" date of the interval). 

# striptime(Timestamp) was used consecutively to account for both VARCHAR and datetime datatypes from the logs since it is not specified.

# Assumptions were made about the date format, but this can easily be altered to account for any particular date format. 
# Knowing the date format would simplify this query allowing me to import it into a dateframe as the correct type, eliminating the need to use strptime to convert.                 



result = duckdb.sql("SELECT DISTINCT CustomerID as LoyalCustomer FROM \
                    (SELECT DISTINCT CustomerID, PageID, strptime(timestamp[:-12], '%Y-%m-%d') - LAG(strptime(timestamp[:-12], '%Y-%m-%d')) \
                    OVER (PARTITION BY CustomerID ORDER BY strptime(timestamp[:-12], '%Y-%m-%d')) AS DIFFERENCE \
                    FROM logs) \
                    subquery WHERE difference = INTERVAL '1 day' \
                    AND CustomerID IN (SELECT CustomerID FROM logs GROUP BY CustomerID HAVING COUNT(DISTINCT PageID) > 1)")
print(result)
                        







   
        