
#understanding exceptions

#age = -5

#if  age < 0:   # if statement is a condtional statement 
#  raise ValueError("Age cannot be negative")# raise means Stop the program here and tell me what went wrong
#print("Age is valid")

# IF else and booleans statement

temperature = 55
is_cold = (temperature < 50)
if is_cold: #when python reaches this if statement it check out whether is_cold is true, runs the intended code
  print("wear a jacket")
else: # the else is used when the condition: if is_cold is False
  print("no jacket needed") # the else statement doesnt require a condition


actual_source_columns = ["ID", "NAME","CLASS","AGE","SCORE"]
columns_to_keep =["ID","CLASS","MARKS"]
missing_columns = []
#we want to go throgh all the columns from source dataset and check if the columns we decide to keep is even our datasour.
for columns in columns_to_keep:
  if columns not in actual_source_columns:
    missing_columns.append(columns)

if missing_columns:
  raise ValueError(f"{missing_columns} does not exist")
print(missing_columns)
