dog_name = input("Enter dog name: ")
dog_type = input("Enter dog type: ")

if dog_type == "corgi" or dog_type == "beagle":
    print("I will walk " + dog_name + " at 12:00pm")
elif dog_type == "bulldog":
    print("I will walk " + dog_name + " at 1:00pm")
else:
    print("I will walk " + dog_name + " at 2:00pm")


