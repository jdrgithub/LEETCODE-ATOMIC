# PYTHON PRACTICE

# ARGS AND KWARGS - EXAMPLE #1
print("ARGS AND KWARGS EXAMPLE #1")

def print_args(*args):
  for arg in args:
    print(args)

print(1, "five", True, "\n")

def print_kwargs(**kwargs):
  for key, value in kwargs.items():
    print(f"KEY: {key} VALUE: {value} \n")

print_kwargs(i=5, name="Wendy", status=True)

def show_all(a, b, *args, **kwargs):
  print(f"a: {a}, b: {b}")
  print(f"args: {args}")
  print(f"kwargs: {kwargs}")

show_all("a", "b", "args", keywordargs="kwargs")
print("\n")
  
 # ARGS AND KWARGS - EXAMPLE #2
 # Passing *args **kwargs from one function to another
print("ARGS AND KWARGS - EXAMPLE #2 \n")

def inner(*args, **kwargs):
  print("Inner:", args, kwargs)

def outer(*args, **kwargs):
  print("Outer:", args, kwargs)
  inner(*args, **kwargs)

outer("this", "that", thing="thing", thing2="thing2")

print("\n")

# ARGS AMD KWARGS - EXAMPLE #3
# Forwarding Parameters in Wrapper Functions / Decorators
print("\n")

def log_calls(func):
  def wrapper(*args, **kwargs):
    print(f"Calling {func.__name__} with {args} and {kwargs}")
    return func(*args, **kwargs)
  return wrapper

@log_calls
def greet(name, greeting="Hello"):
  print(f"{greeting}, {name}! \n")

greet("Pam", "Yo")
print("\n")

# ARGS AND KWARGS - EXAMPLE #4
# Extending Classes While Preserving Parent Signatures
# You're extending a parent class and want to add new functionality without rewriting the full constructor

class Animal:
  def __init__(self, name, species):
    self.name = name
    self.species = species

class Dog(Animal):
  def __init__(self, *args, bark_volume=10, **kwargs):
    super().__init__(*args, **kwargs)
    self.bark_volume = bark_volume
    print(f"{self.name} barks this loud {bark_volume}. That {self.species} is loud!")

dog = Dog("Fido", "Terrier", bark_volume=7)
print("\n")

# ARGS AND KWARGS - EXAMPLE #5
# Flexible Logging or Event Tracking

# Create a logger that can accept arbitrary event details, without having to predefine all the possible fields.
def log_event(event_type, **event_data):
  print(f"--- {event_type.upper()} EVENT ---")
  for key, value in event_data.items():
    print(f"{key}: {value}")

log_event("user_login", user_id=42, ip="192.168.1.10", method="password")
log_event("file_upload", user_id=43, filename="report.pdf", size_kb=234)
print("\n")



# ARGS AND KWARGS - EXAMPLE #6
# Flexible Function Parameters with **kwargs
'''
Scenario:
You’re writing a send_email function. 
You always need to, subject, and body, 
but you want to optionally support things like:

cc
bcc
reply_to
priority
attachments

Rather than clutter the function signature with 10+ optional parameters, you use **kwargs.
'''
def send_email(to, subject, body, **headers):
  print(f"To: {to}")
  print(f"Subject: {subject}")
  print(f"Body: {body}\n")

  if headers:
    print("Optional Headers:")
    for key, value in headers.items():
      print(f"   {key}: {value}")

      
send_email("Bob Johnson", "Hey, Bob!", body="Thanks for signing up!", cc="others", priority="high", reply_to="others@others.com")
print("\n")

'''
-----------
DECORATORS
-----------
EXAMPLE #1

Here’s exactly what happens when Python sees @my_decorator:
1) greet is passed to my_decorator, producing a new function: wrapper
2) greet is replaced by wrapper in the namespace
3) When you call greet(...), you're actually calling wrapper(...)
4) wrapper receives your arguments as *args and **kwargs
5) wrapper passes them to the original func, which is still stored inside

'''
def my_decorator(func):
  def wrapper(*args, **kwargs):
    # pre-processing
    result = func(*args, **kwargs)
    # post-processing
    return result
  return wrapper

@my_decorator
def greet(name, punctuation="!"):
  print(f"Hello, {name}{punctuation}")

# the arguments go to the wrapper not the function
# then the wrapper sends the args to the function.
greet("Pamela", ".")
print("\n")

# DECORATOR - EXAMPLE # 2
# Same as above but with print statements

def my_decorator(func):
  def wrapper(*args, **kwargs):
    print("[WRAPPER] Received:", args, kwargs)
    result = func(*args, **kwargs)
    print("[WRAPPER] Result:", result)
  return wrapper

@my_decorator
def greet(name, punctuation="!"):
  print("[GREET] Executing...")
  return f"Hello, {name}{punctuation}"

greet("Jonathan", punctuation=".")
print("\n")


# DECORATOR - EXAMPLE #3
# USE CASE: Enforce that certain functions can only run if the user is authenticated.

def require_login(func):
  def wrapper(user):
    if not user.get("authenticated"):
      print("Access denied: user not logged in.")
      return None
    return func(user)
  return wrapper

@require_login
def view_account(user):
  print(f"Welcome, {user['name']}! Accessing account dashboard...")

anon = {"name": "Guest", "authenticated": False}
admin = {"name": "Jonathan", "authenticated": True}

view_account(anon)
view_account(admin)
print("\n")

# DECORATOR - EXAMPLE #3
# GOAL: Retry a function n times if it raises an exception. 
# This is useful for:
# API calls
# flaky operations
# transient network/database issues

def retry(n):
  def decorator(func):
    def wrapper(*args, **kwargs): 
      for attempt in range(1, n + 1):
        try:
          return func(*args, **kwargs)
        except Exception as e:
          print(f"[Attempt {attempt}] Error: {e}")
      print("All attempts failed.")
      return None
    return wrapper
  return decorator

import random

@retry(3)
def flaky_operation():
  if random.random() < 0.8:
    raise ValueError("Random failure!")
  print("Operation succeeded!")
  return True

flaky_operation()

'''
Why Use *args, **kwargs?
Because we don’t know what the decorated function’s signature is. 

It might take any number of:
Positional arguments
Keyword arguments
Without *args, **kwargs, this decorator would only work on 0-argument functions.
'''

