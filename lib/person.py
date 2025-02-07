#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name=None, job=None):
        # Validate and set the name
        if name is not None:
            if not isinstance(name, str) or not (1 <= len(name) <= 25):
                print("Name must be string between 1 and 25 characters.")
                return
            self.name = name.title()  # Convert name to title case

        # Validate and set the job
        if job is not None:
            if job not in APPROVED_JOBS:
                print("Job must be in list of approved jobs.")
                return
            self.job = job  # Assign the job
