 # a dictionary is a collection of key-value pairs, where each key is unique and maps to a specific value. Dictionaries are defined using curly braces {} and the key-value pairs are separated by commas. The keys and values can be of any data type, including strings, numbers, lists, and even other dictionaries.
user = {
  "id": 1,
  "age": 20,
  "city": "New York"
}

#dictionary methods
#accessing a value from the dictionary using the key
print(user.get("name", "unknown")) #this will print "unknown" because the key "name" does not exist in the dictionary.

print(user.get("city")) # will print out the specific value for that key


user["name"]= "kelechi" #this will add a new key-value pair to the dictionary

print(user.get("name", "unknown")) #this will print "kelechi" because the key "name" now exists in the dictionary

#dictionary_Name.keys() - returns a list of all keys in the dictionary

user.keys() #this will print all the keys in the dictionary
print(user.keys())

#checks
print("id" in user) #this will print True because the key "id" exists in the dictionary


#checking if a key exists in the dictionary
print("age" in user)

#view objects
print(user.values()) #this will print all the values in the dictionary
print(user.items()) #this will print all the key-value pairs in the dictionary. this is perfect when you need key and value together for looping, transforming, building new dicts, comparing and more.

#looping 
for values in user.values(): #this will loop through all the values in the dictionary
    print(values) #this will print each value in the dictionary

for dict in user:
    print(dict)

for keys in user.keys():
    print(keys) #this will print each key in the dictionary

for key, value in user.items(): #this will loop through all the key-value pairs in the dictionary
    print(key, value) #this will print each key and its corresponding value in the dictionary


# add, remove, and update key-value pairs in a dictionary
print(user)

user["age"]=21
print(user) #this will print the updated dictionary with the new value for the key "age"S

user["gender"] = "male" #this will add a new key-value pair to the dictionary
print(user)

print(user["age"], user["gender"]) #this will print the value of the key "age" and the value of the key "gender"


Premier_League_table = [
    {
    "team": "Manchester United",
    "position": 1,
    "points": 80,
    "manager": "Alex Ferguson"
    },
    {
    "team": "manchester city",
    "position": 2,    
    "points": 75,
    "manager": "Pep Guardiola"
    }
]
#this is a list of dictionaries, where each dictionary represents a team in the Premier League table. Each dictionary contains key-value pairs for the team's name, position, points, and manager.

Premier_League_table[1]["position"] = 3
print(Premier_League_table[1].keys())
# i can either make a list of dictionaries or a dictionary with a list of dictionaries. the choice depends on the data structure and how you want to access the data. if you want to access the data by team name, then a dictionary with team names as keys would be more appropriate. if you want to access the data by position, then a list of dictionaries would be more appropriate.

Premier_League_table = {
   "team_1" : {
        "team": "Manchester United",
        "position": 1,
        "points": 80,
        "manager": "Alex Ferguson"
    },
   "team_2" : {
        "team": "Everton",
        "position": 3,
        "points": 90,
        "manager": "David"
    },
   "team_3" : {
    "team": "manchester city",
    "position": 2,    
    "points": 75,
    "manager": "Pep Guardiola"
    }
}# this is a dicitonary with 3 entries

for  keys, values in Premier_League_table["team_2"].items():
    print(keys, values)
    # team_2 is speciified before the dictionary method .item() to specify the dictionay we are tying to loop through team_2 acts as the index, if the index was nt defined, the default index will be 1

dataset = {
    "file": "patient.csv"
    },
{
    "columns" : [
        "id",
        "Birthdate",
        "Deathdate",
        "Address",
    ]
}

print()