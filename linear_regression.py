from sklearn.linear_model import LinearRegression
hours = [[1], [2], [3], [4], [5]]
marks = [20, 30, 40, 50, 60]
model = LinearRegression()
model.fit(hours, marks)
predict_hours = [[6]]
predict_marks = model.predict(predict_hours)
print(f"hours studied : {predict_hours[0][0]}")
print(f"predict marks : {predict_marks[0]:.1f}")



