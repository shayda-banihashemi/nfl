import dataclasses


@dataclasses.dataclass
class Job:
    without_default_must_be_provided_at_init: str
    i_have_default_so_not_in_init: str = "something"
    job_name: str = ""

    def doit(self):
        return "done"


@dataclasses.dataclass
class Person:
    job: Job


j = Job("required value for first attribute")
p = Person(j)
p.job.job_name = "data engineer"
print(p.job.job_name)
result = p.job.doit()
assert result == "done"

clever_p = Person(Job("first", job_name="janitor"))
assert clever_p.job.job_name == "janitor"
