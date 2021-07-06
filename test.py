def my_string(*args):
    for i in args:
        print(i[::-1])

my_string("anselm", "Steve", "Carol", "Max")