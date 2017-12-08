# first line: 1
@mem.cache
def get_data():
    data = load_svmlight_file(r'''C:\Users\HP\Desktop\australian_scale''',n_features=14)
    return data
