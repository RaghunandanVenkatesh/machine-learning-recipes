from sklearn import tree

features = [[140, 1], [130, 1], [150, 0], [170, 0]]
#bumpy = 0, smooth = 1
labels = [0, 0, 1, 1]
#0 = apple, 1 = orange
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)

print clf.predict([[90,0]])
print clf.predict([[190,1]])
