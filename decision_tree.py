#-------------------------------------------------------------------------
# AUTHOR: Austin Martinez
# FILENAME: decision_tree.py
# SPECIFICATION: A program that reads the accompanying contact_lens.csv and assigns a numerical value to the
# read feature values using a dictionary. It performs this same logic with the read class labels.
# It then uses these values to create a decision tree.
# FOR: CS 4210- Assignment #1
# TIME SPENT: 1 hour. I am still new to Python!
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#importing some Python libraries
from sklearn import tree
import matplotlib.pyplot as plt
import csv
db = []
X = []
Y = []

#reading the data in a csv file
print("\n--- INPUT MATRIX ---")
with open('contact_lens.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)
         print(row)

"""
X MATRIX LOGIC
"""

#transform the original categorical training features into numbers and add to the 4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3
# so X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]
#--> add your Python code here
# X =

# Assign each feature value a numerical value
featuresDict = {
    #Age
    "Young" : 1,
    "Presbyopic" : 2,
    "Prepresbyopic" : 3,

    #Spectacle Prescription
    "Myope" : 1,
    "Hypermetrope" : 2,

    #Astigmatism
    "No" : 1,
    "Yes" : 2,

    #Tear Production Rate
    "Normal" : 1,
    "Reduced" : 2
}

# Creating the training feature values matrix.

# Set our row and column values equal to the dimensions of db matrix
rows = len(db)
cols = len(db[0])-1 # "-1" because we don't want to include the class label in our feature values matrix

# Initialize feature values matrix size
for i in range(rows):
    row = [0] * cols
    X.append(row)

# Convert feature values using a dictionary and assign them to feature values matrix
# We print the matrix to display the feature values converted into numerical values
print("\n--- FEATURE VALUES MATRIX ---")
for row in range(rows):
    output = ""
    for col in range(cols):
        X[row][col] = featuresDict.get(db[row][col], db[row][col])
        output += str(X[row][col]) + " "
    print(output)


"""
Y ARRAY LOGIC
"""

#transform the original categorical training classes into numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
#--> addd your Python code here
# Y =


# Assign each class value a numerical value
classDict = {
    #Reccomended Lenses
    "Yes" : 1,
    "No" : 2
}

# Set our row value equal to the row dimension of the db matrix and ensure that Y's col value is equal to 1 as there is 1 class.


#Initialize class values matrix size
for row in range(rows):
    row = [0] * 1
    Y.append(row)


# Convert class values using a dictionary and assign them to class values matrix
# We print the matrix to display the class values converted into numerical values
print("\n--- CLASS LABELS ARRAY ---")
for row in range(rows):
    output = ""
    Y[row][0] = classDict.get(db[row][cols], db[row][cols])
    output += str(Y[row][0]) + " "
    print(output)


#fitting the decision tree to the data
clf = tree.DecisionTreeClassifier(criterion = 'entropy')
clf = clf.fit(X, Y)

#plotting the decision tree
tree.plot_tree(clf, feature_names=['Age', 'Spectacle', 'Astigmatism', 'Tear'], class_names=['Yes','No'], filled=True, rounded=True)
plt.show()