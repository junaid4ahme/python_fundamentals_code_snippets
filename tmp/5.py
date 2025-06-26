# DICTIONARY
# Removing a key and value from a dictionary
# we can use two methods pop as well as del
country = {"india": ("mumbai", "delhi", "kolkata"), "us": ("new york", "la", "las vegas")}
for i, j in country.items():
    print(i, j)


country.pop("india")
for i, j in country.items():
    print(i, j)


