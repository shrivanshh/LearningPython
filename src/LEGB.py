# This is just an understanding between different types of python scopes, in this example, we will see how
# different types of scopes are used. LEGB
# L: Local Variable
# E: Enclosing function variable
# G: Global Variable
# B: Built-in variable


# Example
my_list = [1, 2, 3, 4, 5] # Global


def my_length(my_list):
    print "The Length of my_list is {my_list}".format(my_list=len(my_list))  # my_list is global
    my_list = [1, 2, 3, 4] # Local
    print "The Length of my_list is {my_list}" .format(my_list=len(my_list)) # len is built-in here

    def nested_func (my_list):
        print "The Length of my_list is {my_list}".format(my_list=len(my_list)) # Enclosing function local

    nested_func(my_list)

my_length(my_list) # should return

