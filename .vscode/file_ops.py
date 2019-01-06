import os.path, time



# get json file last update date

def get_file_update_datetime(file_path_name):
    return time.ctime(os.path.getmtime(file_path_name))

def get_file_update_date(file_path_name):
    return time.ctime(os.path.getmtime(file_path_name))

# print("Last modified: %s" % time.ctime(os.path.getmtime("result_AMZN.json")))
# print("Created: %s" % time.ctime(os.path.getctime("result_AMZN.json")))
