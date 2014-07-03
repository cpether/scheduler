
from datetime import datetime
from datetime import timedelta
import subprocess

class Job:

	# status can be N, Y or R (Not started, complete, or running)
	status = 'N'

	# Set up job data.
	def __init__(self, data):
		l = data.split()
		self.name       = l[2]
		self.dependancy = l[3]
		self.cmd        = l[4:]
		self.min_time   = datetime(datetime.today().year, \
						datetime.today().month, \
						datetime.today().day, \
						int(l[1]),int(l[0]))


	def get_name(self):
		return self.name

	def get_time(self):
		return self.min_time

	def get_status(self):
		return self.status

	def get_dependancy(self):
		return self.dependancy

	def set_status(self,new_status):
		self.status = new_status

	def set_dependancy(self,new_dep):
		self.dependancy = new_dep


	# Run the process in the background.
	def run_job(self):
		print 'Running job - ' + self.name
		self.process = subprocess.Popen(self.cmd)


	# Check on the status of the jobs process.
	def get_process_status(self):
		if hasattr(self, 'process'):
			if hasattr(self.process, 'poll'):
				return self.process.poll()


	# Mark the job as running, and reset the time.
	def mark_started(self):
		self.status = 'R'
		self.min_time = self.min_time + timedelta(days=1)


	# A job can't run because of dependancies, so try again in a minute.
	def postpone_job(self):
		self.min_time = self.min_time + timedelta(minutes=1)


	# Used for debugging.
	def print_job(self):
		print 'Job: ' + self.name
		print 'status ' + self.status
		print 'run time ' + str(self.min_time)

