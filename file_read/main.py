####1 basic way of reading files###
# file = open("sample.txt","r")
# content=file.read()
# print(content)
# file.close()   ### file open , read file , close file


#### 2 nd way ####
### opens reads closes automatically ##context manager
# with open("sample.txt","r") as file:
#     content=file.read()
# print(content)



#3## readlines -  reads line by line
# with open("sample.txt","r") as file:
#     content=file.readlines()
# print(content)


# ##4 reads line by line
# with open("sample.txt","r") as file:
#      content=file.readline()
#      print(content)

#      content=file.readline()
#      print(content)
#      print(content)


# ## to read few chrs like 10 or 20
# with open("sample.txt","r") as file:
#      content=file.read(10)
#      print(content)


### to read chunk

#### to read content in loop line by line 
# with open("sample.txt","r") as file:
#      for i in file:
#           print(i)



chunk_size=10
with open("sample.txt","r") as file:
    while True:
        chunk=file.read(chunk_size)
        print(chunk)
        if not chunk:
            
            break