
import time
from datetime import datetime
from job import Job

class Scheduler:

	# List of Job objects
	jobs = []

	def __init__(self):
		pass


	# Set up jobs to run and start scheduler.
	def start(self):
		print 'Starting scheduler...'
		self.read_jobs()
		self.apply_dependancies()
		self.main_loop()


	# Check the next job to run, and run it at scheduled time.
	def main_loop(self):
		while len(self.jobs):
			self.cleanup()
			idx = self.get_next_job()
			cur_time = datetime.now()
			next_time = self.jobs[idx].get_time()
			if next_time <= cur_time:
				self.run_job(idx)
			else:
				wait = next_time - cur_time
				time.sleep(wait.total_seconds())


	# Check for dependancies before running job.
	def run_job(self,idx):
		dep = self.jobs[idx].get_dependancy()
		if isinstance(dep, Job):
			if dep.get_status() != 'Y':
				self.jobs[idx].postpone_job()
				return
		self.jobs[idx].mark_started()
		self.jobs[idx].run_job()


	# Read jobs from input file.
	def read_jobs(self):
		# read the jobs file
		f = open('jobs','r')
		for line in f:
			self.jobs.append(Job(line))
		f.close


	# Get the next job to run based on job time.
	def get_next_job(self):
		i = j = 0
		for job in self.jobs:
			if i == 0:
				earliest = job.get_time()
			else:
				if job.get_time() < earliest:
					earliest = job.get_time()
					j = i
			i += 1
		return j


	# Link jobs to thier dependancies.
	def apply_dependancies(self):
		for job in self.jobs:
			if job.get_dependancy() != 'none':
				for dep in self.jobs:
					if dep.get_name() == job.get_dependancy():
						job.set_dependancy(dep)
						break


	# If a job is set as running, check it's status and update,
	#  if all jobs are complete, reset them all for tomorrow.
	def cleanup(self):
		all_done = 1
		for job in self.jobs:
			if job.get_status() == 'R':
				all_done = 0
				if job.get_process_status() == 0:
					job.set_status('Y')
			elif job.get_status() == 'N':
				all_done = 0
		if all_done == 1:
			self.reset_jobs()


	# Set a jobs status to 'N'.
	def reset_jobs(self):
		for job in self.jobs:
			job.set_status('N')


	# Used for debugging.
	def print_jobs(self):
		for job in self.jobs:
			job.print_job()


# Start the app.
if __name__ == '__main__':
	scheduler = Scheduler()
	scheduler.start()

