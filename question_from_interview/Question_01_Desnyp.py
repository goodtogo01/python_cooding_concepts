# Replace Key from given dictionary
import collections
import json
print("--------- Dictionary Start -----------------")
my_dict = {
    'name': 'jamal',
    'em_id':11,
    'id': {
        'city_id': 18,
        'county_id':17
    }
}

print("------ Actual value of given Dictionary : ", json.dumps(my_dict, indent=4))
# Change key Method 1
my_dict['new_id']=my_dict.pop('id')
print("\n------Updated value of given Dictionary with  with pop Method : \n", json.dumps(my_dict, indent=4))

# Change key Method 1

my_dict = {key.replace('id', "id_number"): value for key , value in my_dict.items()}
print("\n------------Updated value of given Dictionary with key-replace Method  : \n", json.dumps(my_dict, indent=4))


print("--------- Dictionary End -----------------\n")
# Count frequent words from the string
print("--------- String Frequent words count Start -----------------")
s= "If you already have an older version of the Fliqlo screensaver installed"
r = {key: s.count(key)
     for key in s.split()
     }
print(json.dumps(r, indent=4))


# Swap first and Last number from the list
list = [3,2,1,5,4,7,8]


def swap(l):
    l[0] , l[-1]=  l[-1] ,l[0]
    return l
print("Swap List : ", swap(list))
