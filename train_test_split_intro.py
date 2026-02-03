# Simple train-test split idea (without libraries)

data = [10, 20, 30, 40, 50, 60, 70, 80]

# 75% train, 25% test
split_index = int(len(data) * 0.75)

train_data = data[:split_index]
test_data = data[split_index:]

print("Train Data:", train_data)
print("Test Data:", test_data)
