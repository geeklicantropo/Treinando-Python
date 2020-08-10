import os

string_to_find = "wolf"
directory_to_search = 'C://Desktop//list_names.txt'
wolf_docs = []

for file in os.listdir(directory_to_search):
    with open(directory_to_search + file) as f:
        if string_to_find in f.read():
            wolf_docs.append(file)
            
print(wolf_docs)