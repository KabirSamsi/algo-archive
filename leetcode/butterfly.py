#LIBRARIES
import matplotlib.pyplot as plt
import numpy as np

def mean(arr):
    return sum(arr)/len(arr)

#AVERAGES QUESTION

eyespots_1889 = [1.4, 1.4, 0.3, 0.5, 1.8, 1.1, 0.4, 0.7, 0.0, 0.1, 0.7, 1.3, 0.4, 1.1, 0.6, 1.1, 0.5, 1.0, 1.0, 0.6]
eyespots_1890= [0.6, 0.9, 0.7, 0.9, 0.2, 0.1, 0.4, 0.7, 0.3, 0.4]

print("1889 " + str(mean(eyespots_1889)))
print("1890 " + str(mean(eyespots_1890)))


#SCATTERPLOT QUESTION
parents = list(map(lambda x : float(x), #Build array of all parent data
"""0.9
0.1
0.3
0.4
0.4
0.5
0.5
0.6
0.6
0.7
0.7
1.0
1.0
1.1
1.1
1.1
1.3
1.4
1.4
1.8""".split('\n')))

children = list(map(lambda x : float(x), #Build array of all children data
"""0.98
0.2
0.2
0.5
0.3
0.6
0.4
0.7
0.5
0.8
0.6
1.1
0.9
1.2
1.0
1.2
1.2
1.5
1.3
1.9""".split('\n')))

m, b = np.polyfit(np.array(parents), np.array(children), 1) #Slope-intercept line of best fit

#Develop graph
plt.scatter(np.array(parents), np.array(children), color="purple") #Develop scatterplot
plt.plot(np.array(parents), m*np.array(parents)+b, color="purple") #Develop line of best fit
plt.title("Heritability of Eyespot Diameter in Buckeye Butterflies")
plt.xlabel("Mid-Parent Eyespot Diameter in Buckeye Butterflies (mm)")
plt.ylabel("Mid-Offspring Eyespot Diameter in Buckeye Butterflies (mm)")
plt.show()

#QUESTION 6
survived_offspring = list(map(lambda x : float(x), 
"""0.9
0.1
0.6
0.7
0.1
0.4
0.3
0.0
0.1
1.4
0.0
0.2
0.9
0.0
0.9
0.9
0.4
0.9
1.0
0.7""".split('\n')
))

print(str(mean(survived_offspring)))