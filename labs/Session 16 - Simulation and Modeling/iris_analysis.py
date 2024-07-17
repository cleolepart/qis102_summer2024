#iris_analysis.py

# This script reads the iris dataset from a CSV file 
# and organizes the data by the iris variety (Setosa, Versicolor, Virginica), 
# extracting the petal length and petal width for each variety. 
# It then creates a scatter plot using matplotlib, 
# plotting petal length on the x-axis and petal width on the y-axis. 
# Different colors are used to represent each iris variety: 
# red for Setosa, blue for Versicolor, and green for Virginica.

import csv
import matplotlib.pyplot as plt

def load_iris_data(filename):
    data = {'Setosa': {'petal_length': [], 'petal_width': []},
            'Versicolor': {'petal_length': [], 'petal_width': []},
            'Virginica': {'petal_length': [], 'petal_width': []}}
    
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)  # Needed in order to skip the header row
        for row in csvreader:
            petal_length = float(row[2])
            petal_width = float(row[3])
            variety = row[4].strip()
            if variety == 'Setosa':
                data['Setosa']['petal_length'].append(petal_length)
                data['Setosa']['petal_width'].append(petal_width)
            elif variety == 'Versicolor':
                data['Versicolor']['petal_length'].append(petal_length)
                data['Versicolor']['petal_width'].append(petal_width)
            elif variety == 'Virginica':
                data['Virginica']['petal_length'].append(petal_length)
                data['Virginica']['petal_width'].append(petal_width)
    
    return data

def main():
    
    # Load the iris data
    filename = '/Users/clepart/qis102/labs/Session 16 - Simulation and Modeling/iris.csv'
    data = load_iris_data(filename)
    
    # Plot the data
    plt.scatter(data['Setosa']['petal_length'], data['Setosa']['petal_width'], label='Setosa', color='red')
    plt.scatter(data['Versicolor']['petal_length'], data['Versicolor']['petal_width'], label='Versicolor', color='blue')
    plt.scatter(data['Virginica']['petal_length'], data['Virginica']['petal_width'], label='Virginica', color='green')
    
    # Add labels and legend
    plt.xlabel('Petal Length (cm)')
    plt.ylabel('Petal Width (cm)')
    plt.title('Iris Flower Data')
    plt.legend()
    plt.grid(True)
    
    plt.show()

if __name__ == "__main__":
    main()
