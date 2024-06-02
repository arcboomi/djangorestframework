from django.db import models

# Create your models here.

class TimestampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add =True)
    updated_at = models.DateTimeField(auto_now =True)

    class Meta:
        abstract = True

class Environment(TimestampModel):
    environment_name = models.CharField(max_length = 180)
    environment_description = models.TextField(max_length = 250)

    def __str__(self):
        return self.environment_name

class Solution(TimestampModel):
    solution_name = models.CharField(max_length=180)
    solution_description = models.CharField(max_length=180)

    def __str__(self):
        return self.solution_name

class Computer(TimestampModel):
    computer_name = models.CharField(max_length=180)
    computer_ip = models.CharField(max_length=180)
    solution = models.ForeignKey(Solution, on_delete=models.CASCADE)
    environment = models.ForeignKey(Environment, on_delete=models.CASCADE)


    def __str__(self):
        return self.computer_name
