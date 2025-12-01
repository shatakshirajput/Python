d ={
    "name":"abc",
    "cgpa": 9.2,
    "subjects":["math","science"]
}

# keys
print(d.keys())

# values
print(d.values())

# items(key,values)
print(d.items())

# returns val (for the key, if key doesnt exist returns none)
print(d.get("name"))

# update
d.update({
    "city":"delhi"
})
print(d)