import file_ops as fo

dt = fo.get_file_update_datetime('result_AMZN.json')
dtt = fo.get_file_update_datetime('result_AMZN.json')

print(dt, "\n", dtt)