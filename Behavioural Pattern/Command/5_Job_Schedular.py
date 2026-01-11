# Job Schedular

from abc import ABC, abstractmethod
import time


class command(ABC):
    @abstractmethod
    def execute(self):
        pass


class Job:
    def __init__(self, name):
        self.name = name

    def execute_job(self):
        print(f"{self.name} is executing.....")
        time.sleep(2)


class ScheduleJob(command):
    def __init__(self, job):
        self.job = job

    def execute(self):
        self.job.execute_job()


class JobSchedular:
    def __init__(self):
        self.jobs = []

    def schedule_job(self, command):
        command.execute()
        self.jobs.append(command)


if __name__ == "__main__":

    job_schedular = JobSchedular()

    job1 = Job("Job-1")
    job2 = Job("Job-2")
    job3 = Job("Job-3")
    job4 = Job("Job-4")

    schedule_command1 = ScheduleJob(job1)
    schedule_command2 = ScheduleJob(job2)
    schedule_command3 = ScheduleJob(job3)
    schedule_command4 = ScheduleJob(job4)

    job_schedular.schedule_job(schedule_command1)
    job_schedular.schedule_job(schedule_command2)
    job_schedular.schedule_job(schedule_command3)
    job_schedular.schedule_job(schedule_command4)
