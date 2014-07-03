scheduler
=========

Usage: python scheduler.py

Info:
  The jobs file contains a list of jobs to be run in the following format:
    start_minute start_hour job_name dependancy command
    
  Start minute and start hour represent the time of day to run the job (in 24hr time format).
  Job name can be any text.
  Dependancy must match another jobs job_name.
  Command is the command needed to run the process.
  
  
  test1.sh, test2.sh, test3.sh are example scripts that could be run by the scheduler.
  
TODO:
  Add lots more error handling!
  Optimize some parts, like getting next job time.
  
