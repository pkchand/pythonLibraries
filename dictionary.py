my_dict={ "bug":"An error", "feature":"things to do"}
print(my_dict)
my_dict1={
    "bug":"An error", 
    "feature":"things to do"
}
for i in my_dict1:
    print(my_dict1[i])

travel_log={
    "France":{
        "nun_times_visited":0,
        "cities_visited":["Paris","Lille", "Dijon"],
    },
    "Germany":["Stuttgart","Berlin"],
}

print(travel_log["France"]["cities_visited"][1])