import pickle

def read_pickle_and_extract_frequency(filename):
    with open(filename, 'rb') as f:
        data = pickle.load(f)
    if 'frequency' in data:
        return data['frequency']
    else:
        raise KeyError("The 'frequency' key was not found in the pickle data")

# Provide the directory where your pickle files are located
pickle_directory = '/path/to/pickle/files/'

# Iterate through the pickle files in the directory
for filename in os.listdir(pickle_directory):
    if filename.endswith('.p'):
        full_path = os.path.join(pickle_directory, filename)
        try:
            frequency_value = read_pickle_and_extract_frequency(full_path)
            print(f"Frequency value from {filename}: {frequency_value}")
        except Exception as e:
            print(f"Error processing {filename}: {e}")
