def first_function():
  print("we did it!")

first_function()  #this calls the function

#Passing an argurement into a functions
def first_function(name):
  print(f"we did it {name}!")

first_function("kelechi")

#when we call a function we can send more than one argument.
def first_function(name , age ):
  print(f"next year, {name} will be {age} years old")

first_function("kelechi", 20)

def display_invoice(username, amount, due_date):
  print(f"Hello {username}")
  print(f"Your bill of ${amount: .2f} is due: {due_date}")

display_invoice("Kelechi Ofoegbu", 42.50, "01/01")

def celius_to_kelvin(num1): #num1 is the parameter.It is a placeholder. so num1 = 80
  kelvin = num1 + 273
  return kelvin
  # return sends the value calculated inside the function back to where the function was called. # If I store the function call in a variable, the returned value is stored in that variable. # Example: temperature = celius_to_kelvin(80) stores the returned value 353 in temperature.
temperature = celius_to_kelvin(80)
print(temperature, "k")#80 is the argument

def prospect(name_01, age_01, height_01, club_status):
  info = print(f"name: {name_01}\n" ## print output is stored in info and then 'return info' return that output to where the function was called  "prospect("kelechi Ofoegbu", str(20),"5,11", "free agent")"
      f"Age: {age_01}\n"
      f"height: {height_01}\n"
      f"club status: {club_status}"
)
  return info

print("transfer market profile")
profile = prospect("kelechi Ofoegbu", 20,"5,11", "free agent")
print(profile)



