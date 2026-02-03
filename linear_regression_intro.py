# Simple linear regression idea (without libraries)

# Sample data: hours studied vs marks
hours = [1, 2, 3, 4, 5]
marks = [40, 50, 60, 70, 80]

# Simple prediction rule
def predict_marks(hour):
    return 30 + 10 * hour

print("Predicted marks for 6 hours:", predict_marks(6))
