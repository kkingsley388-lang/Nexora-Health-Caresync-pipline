

# for example a manager wants to liquidates items by adding a 10% discount to the price of sum items.

#We can either, do it manually i.e create print state fo reach value in the list

discount = 0.10
prices = [12.99, 15.99, 7.99, 27.99]

print(prices[0]*(1-discount))
print(prices[1]*(1-discount))
print(prices[2]*(1-discount))
print(prices[3]*(1-discount))
#can you imagine how long it would take instead of 4 prices the list contained 100 prices
# prices = [12.99, 15.99, 7.99, 27.99]# this part of the code is where the for loop shines, why?



#ALTERNATIVE
#Implementing th discount with a FOR loop
prices = [12.99, 15.99, 7.99, 27.99]
for price in prices: #essential the variable name price is assigned each value in the list variable prices
  print(price *(1-discount))# this calculates the price and output the answer, python then returns to the code header. the variable price then takes on the next value in the list and does the same thing. the for loop ends up transversing through all the values in the list.
print("price discounted")

# exapmple 2
for ticket_number in range(1000, 1006):

  print("summer's super rafle ")
  print("Ticker number:",ticket_number )


#example 3; this is in relation to the extractor.py
#am trying to understand putting an IF inside a FOR loop.

columns_to_keep = ["Name", "Age", "Address"]

for column in columns_to_keep:
    if column == "Age": # == is a logical conditon that reads: the variable column equals Age.
        print(column)# read everythinh like this: For every column in columns_to_keep, if that column is "Age", print it.
#  column = "Name"
#    ↓
#  Is "Name" == "Age"? → No
#   ↓
#  Don't print

# Then:
# column = "Age"
#   ↓
# Is "Age" == "Age"? → Yes
# Print "Age"

#NOW THAT WE KNOW HOW TO COMBINE A FOR LOOP WITH AN IF STATEMENT. LETS LOOK OUT THE ACTUAL CODE IN extract.py: 
columns_to_keep = ["Name", "Age", "Address"]
actual_columns = ["Name", "Address"]

for column in columns_to_keep:
    if column not in actual_columns:
        print(column)
        #the variable column is assigned each pf the values in column to keep, i.e columm ="Name" if that value is NOT in the variable actual_columns print it


for age in range(0,100):
   if age >= 18 and age <= 30:
      print(age)

columns_to_keep = ["Name", "Age", "Address"]
actual_columns = ["Name", "Address"]

for column in columns_to_keep:
    if column not in actual_columns:
        actual_columns.append(column)# .that is a value the variable colum takes thats what is appended into actual_column
        print(column)