# Day 3 - Understanding Modules and pip in Python

# Built-in module
import math

print("Square root of 16 is:", math.sqrt(16))

# External module (make sure you installed it via pip)
import requests

response = requests.get("https://api.github.com")
print("GitHub API Status Code:", response.status_code)
