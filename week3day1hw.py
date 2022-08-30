Exercise #1
Filter out all of the empty strings from the list below

Output: ['Argentina', 'San Diego', 'Boston', 'New York']

places = [" ","Argentina", " ", "San Diego","","  ","","Boston","New York"]

print("Original list is : " + str(places))

while ("" in places):
    places.remove("")
    if (" " in places):
        places.remove(" ")
        if ("  "in places):
            places.remove("  ")
    
print("Output : " + str(places))

places = list(filter(lambda x: x != "", places))
print(places)

Exercise #2
Write an anonymous function that sorts this list by the last name...
Hint: Use the ".sort()" method and access the key"

Output: ['Victor aNisimov', 'Gary A.J. Bernstein', 'Joel Carter', 'Andrew P. Garfield', 'David hassELHOFF']

author = ["Joel Carter", "Victor aNisimov", "Andrew P. Garfield","David hassELHOFF","Gary A.J. Bernstein"]

author.sort(key=lambda name: name.split(" ")[-1].lower())
print(author)

Exercise #3
Convert the list below from Celsius to Farhenheit, using the map function with a lambda...

Output: [('Nashua', 89.6), ('Boston', 53.6), ('Los Angelos', 111.2), ('Miami', 84.2)]

# F = (9/5)*C + 32
places = [('Nashua',32),("Boston",12),("Los Angelos",44),("Miami",29)]

places = list(map(lambda c:  (c[0], (9/5) * c[1]+ 32), places))
print(places)

Exercise #4
¶
Write a recursion function to perform the fibonacci sequence up to the number passed in.

Output for fib(5) => 
Iteration 0: 1
Iteration 1: 1
Iteration 2: 2
Iteration 3: 3
Iteration 4: 5
Iteration 5: 8


n_terms = int(input ("How many terms the user wants to print? "))  
  
# First two terms  
n_1 = 0  
n_2 = 1  
count = 0  
  
# Now, we will check if the number of terms is valid or not  
if n_terms <= 0:  
    print ("Please enter a positive integer, the given number is not valid")  
# if there is only one term, it will return n_1  
elif n_terms == 1:  
    print ("The Fibonacci sequence of the numbers up to", n_terms, ": ")  
    print(n_1)  
# Then we will generate Fibonacci sequence of number  
else:  
    print ("The fibonacci sequence of the numbers is:")  
    while count < n_terms:  
        print(n_1)  
        nth = n_1 + n_2  
       # At last, we will update values  
        n_1 = n_2  
        n_2 = nth  
        count += 1 