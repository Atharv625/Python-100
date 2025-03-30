# Description: String methods
a="Alpha"
print(len(a)) #5
print(a.upper()) #ALPHA
print(a.lower()) #alpha 
print(a.strip()) #Alpha
print(a.replace("A","B")) #Blpha
print(a.split("p")) #['Al','ha']
print(a.find("p")) #2
print(a.count("p")) #1
print(a.isalpha()) #True
blog="i am a blogger"
print(blog.capitalize()) #I am a blogger
print(blog.title()) #I Am A Blogger
print(blog.swapcase()) #I AM A BLOGGER      
print(blog.center(30)) #       i am a 
print(a.endswith("a")) #True
print(a.startswith("A")) #True
print(a.islower()) #False
print(a.isupper()) #False       
print(a.isdigit()) #False
print(a.isalnum()) #True
print(a.isspace()) #False
print(a.isprintable()) #True
