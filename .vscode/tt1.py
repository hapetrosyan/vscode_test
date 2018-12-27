


a = {'1. open': '42.3400', '2. high': '33.333'}
b = {}


print(a)

def format_dict(original_dict):
    output_dict = {}
    for k, v in original_dict.items():
        output_dict[k[3:]] = float(original_dict[k])
    return output_dict
    
print(format_dict(a))