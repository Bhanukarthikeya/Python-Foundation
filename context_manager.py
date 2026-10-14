import contextlib
import traceback


# @contextlib.contextmanager
# def ef_context_manager():
#     print("Before") #CODE BEFORE

#     yield

#     print("After") #CODE AFTER

# with ef_context_manager():
#     print("test")
    

import time

# start = time.time()
# for i in range(1000000000):
#     pass
# print('your code here.....')

# end = time.time()

# timer = end - start

# print(f"time taken {timer} seconds")

import contextlib
@contextlib.contextmanager
# def  time_it():
#     start = time.time() #BEFORE
#     yield
#     end = time.time() #AFTER
#     timer = end - start
#     print(f"time taken {timer} seconds")

# with time_it():
#     result = []
#     for i in range(100000):
#         result.append(i*3)

# with time_it():
#     result = [i*3 for i in range(100000)]


# def try_accept(debug = False):
#     try:
#         yield
#     except:
#         if debug:
#             print(traceback.format_exc())

# with try_accept():
#     print(1/0)
# with try_accept(debug = True):
#     print(1/0)



