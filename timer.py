#
#   Author: Ruby Abrams
#   Description:
#       Gonna write a timer decorator function
#       to use in my other scripts to time how long they take
#
#
import time

# outputs time taken to execute function
def time_this(function):

    def wrapper():
        start_time = time.time()
        function()
        end_time = time.time()
        return 'duration: ' + str(end_time - start_time)

    return wrapper

if __name__ == '__main__':
    time_this()
