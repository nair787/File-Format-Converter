Run-time Arguments and Enviroment Variable

how to customize a runtime behaviour of an application
using either arguments or Enviroment Variable

There are multiple ways to customize the runtime behaviour
of an application

when it comes to SDLC (Software Development Life Cycle)
we have a different phases like software development 
testing and the production phases ,In some cases we might 
have additional phases as well 

when it comes to these phases or stages, we might have to
pass different arguments or Enviroment Variable to customize
the runtime behaviour based on the phase or stage the application
is running 


In envioroment varaiable 

For eg : we have a set of servers ,Even the external system
will be different
let's say we developed a application which talks with
a db. In development the database server details will be 
different compared to database server that is used in testing
and the database server that is used in production 

UAT:
UAT stands for User Acceptance Test. For software testing, 
the UAT environment is a final step in the testing process 
that ensures the application meets customer requirements 
and expectations.

This application reauires to set the Enviroment variables 
$Env:SRC_BASE_DIR = "data/retail_db"
$Env:TGT_BASE_DIR = "data/retail_db_json"
Pass the run arguments
python app.py '[\"orders\",\"order_items\"]'

Q what are the tools that company uses to pass the environment variables in different enviroments
