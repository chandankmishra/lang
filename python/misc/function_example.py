from functools import reduce

#=============================

def example_function():
    print("example_function")
    return

example_function()
print()

#=============================

def pass_by_value(arg_number):
    print("In pass_by_value = ", arg_number)
    arg_number = arg_number + 200
    return

number = 100
print("Before pass_by_value = ", number)
pass_by_value(100)
print("After pass_by_value = ", number)
print()

#=============================

def fibnocci(max_number):
    n1, n2 = 0, 1
    print("[", end=" ")
    while n1 < max_number:
        print(n1, end=" ")
        n1, n2 = n2, n1+n2
    print("] ")

fibnocci(100)
print()

#=============================

def fibnocci_return_list(max_number):
    return_list = [ ]
    n1, n2 = 0, 1
    while n1 < max_number:
        return_list.append(n1)
        n1, n2 = n2, n1+n2
    return return_list

fibnocci_list = fibnocci_return_list(100)
print(fibnocci_list)
print()

#=============================

def default_arguments(name, age=30, company="Juniper"):
    print("Name: ", name)
    print("Age: ", age)
    print("Company: ", company)
    print()


default_arguments("James")
default_arguments("John",age=40)
default_arguments("Victor", company="abc")
default_arguments("Vivian",25,"xyz")

#=============================

def careful_with_default_arguments(number, mylist=[]):
    mylist.append(number)
    print(mylist)

careful_with_default_arguments(100)
careful_with_default_arguments(200)
careful_with_default_arguments(300)

#=============================

def prefer_default_arguments_this_way(number, mylist=None):
    if mylist is None:
        mylist = []
    mylist.append(number)
    print(mylist)

prefer_default_arguments_this_way(1000)
prefer_default_arguments_this_way(2000)
prefer_default_arguments_this_way(3000)
print()

#=============================

def pass_function():
    print("Invoking pass_function")
    pass

pass_function()
print()

#=============================


def anonymous_increment_function(step_count):
    return lambda x: x+step_count

mylambda = anonymous_increment_function(10)
print("mylambda(100) = ",mylambda(100))

#=============================

def enclose_function(step_count):
    def inner_function(multipler):
        return step_count*multipler
    return inner_function

myencloser = enclose_function(1000)
print("myencloser(20) = ", myencloser(20))
print()

#============================= standard for loop ======

multiple_of_2 = []
for count in range(10):
    multiple_of_2.append(count*2)
print("using for loop: multiple_of_2 = ", multiple_of_2)
print()

#============================= list comprehension ========

lc_multiple_of_2 = [count*2 for count in range(10)]
print("using list comprehension: multiple_of_2 = ", lc_multiple_of_2)
print()

#============================= list comprehension ======

my_matrix = [(x,y) for x in range(1,4,1) for y in range(1,6,1)]
print("using list comprehension: my_matrix = ", my_matrix)
print()

#============================= zip example =======

rows=[x for x in range(1,6,1)]
columns=[y for y in range(1, 4, 1)]
zip_matrix = zip(rows, columns)
print("zip_matrix = ",list(zip_matrix))
print()

#============================= map function =======

def map_function_inc_by_5(number):
    return number+5

base_list=[10,20,30,40,50,60,70,80,90,100]
map_list = list(map(map_function_inc_by_5, base_list))
print("mapped_list = ", map_list)
print()

#============================= filter function =======

filter_list = list(filter(lambda x: x%3 == 0, map_list))
print("filtered_list = ", filter_list)
print()


#============================= reduce function =======

reduce_max_value = reduce(lambda x,y: x if (x>y) else y, filter_list)
print("reduced_max_value = ", reduce_max_value)
print()

#============================= decorator =======

def beautify_add_frame(what_to_be_framed):
    print("Item is framed")
    return what_to_be_framed

@beautify_add_frame
def beautify_code(beautify_block):
    print("You are beautified")
    return beautify_block

@beautify_code
def beautify_paragraph():
    print("Beautifying Paragraph complete")

beautify_paragraph()
print()

#============================= Interator =======

my_iter = iter(list(range(1,11)))
print("My Iterator Object = ", my_iter)
print("my_iter.next() = ", next(my_iter))
print("my_iter.next() = ", next(my_iter))
print("my_iter.next() = ", next(my_iter))
print()

#============================= Generator =======
def example_generator(max):
    value = 1000
    while (value < max):
        yield(value)
        value += 100

my_generator = example_generator(2000)
print("my_generator = ", my_generator)
print("next value in my generator = ", next(my_generator))
print("next value in my generator = ", next(my_generator))
print("next value in my generator = ", next(my_generator))
print()

#============================= The End =======







