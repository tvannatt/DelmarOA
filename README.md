# DELMAR Technical Assessment Submission

Programming language used: Python, SQL

Outstanding questions for client:
* How frequently would log files be queried to determine loyal customer status?
    * How many files would be queried at a time?
* Are there any performance constraints?
* How are the log files structured?
* How are the log files stored/retrieved?
* What quantity of data is being analyzed?
* Are there any preferred technologies or methods of implementation?
* What use-cases did the client form their requirements around?




Notes: 
* Assuming comma delimited data as well as YYYY-MM-DD 
* Goal is to write python program to read log files into some type of datastructure.
    * Python for its versatility in data analysis, which seems to be the functional application of this question.
* Using glob and pandas libraries for ease of mass-appendage and dataframe conversion.
    * Landed on dataframes as I inted to use SQL to query the data due to my familiarity with it and lack of detailed requirements.
    * Could be achieved through chaining pandas functions(?)
* Program was inevitably designed to accept only two files as input, requiring user to specify the two days. 
    * Not very scalable or versatile, but an extremely simple, efficient solution depending on business requirements.
* Altered program to use subqueries at the cost of efficiency to query *multiple* files checking for users with consecutive sign on dates.
    * This operates under the assumption that the date *is* included in the timestamp. 
        * Only accomodates YYYY-MM-DD date format for the sake of this assessment, but in a business scenario, I'd have confirmed the format before writing the query. 
