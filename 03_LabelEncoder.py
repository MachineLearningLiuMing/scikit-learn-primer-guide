from sklearn import preprocessing
le = preprocessing.LabelEncoder()

le.fit(["paris", "paris", "tokyo", "amsterdam"])

print(le.transform(["tokyo", "tokyo", "paris"]))
print(list(le.inverse_transform([2, 2, 1])))