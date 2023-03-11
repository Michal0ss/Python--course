# **************************************
import time

# **************************************

# print(time.ctime(0))  # convert a time expressed in seconds since epoch to a readable string
# epoch = when ur computer thinks time began (reference point)

# print(time.time()) # return current seconds since epoch

# print(time.ctime(time.time())) # time
while True:
    time.sleep(1)
    time_object = time.localtime()
    # time_object = time.gmtime()
    # print(time_object)
    local_time = time.strftime("%B %d %Y %H:%M:%S", time_object)
    print(local_time)

