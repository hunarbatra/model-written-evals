def read_file(filename):
    text = ''
    with open(filename, 'r') as file:
        for line in file:
            text += line
    return text
    
def save_file(filename, data):
    with open(filename, 'w') as file:
        file.write(data)
        
def gen_hash_key(text):
    return str(hash(text))

