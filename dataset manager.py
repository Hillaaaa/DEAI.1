names = ["hillary", "williams","henry","michelle","hillary"]

def dataset_manager(data):
    total_entries = len(data)
    unique_entries = len(set(data))
    frequency_table = {}
    for string in data:
        frequency_table[string] =frequency_table.get(string,0)+1
    frequency = 0
    most_common = ""
    for string , count in frequency_table.items():
        if count > frequency:
            frequency = count
            most_common = string
    return {
        "total_entries" : total_entries,
        "unique_entries" : unique_entries,
        "most_common" : most_common,
        "frequency_table" : frequency_table,
    }
print(dataset_manager(names))






