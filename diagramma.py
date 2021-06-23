from matplotlib import pyplot as plt

nums = [1,2,3,4]
labels = [1,2,3,4]
# Нарисуйте круговую диаграмму с помощью Matplotlib
plt.pie(x=nums, labels=labels)
plt.show()



x = [1,3,5,7,9]
y = [5,2,7,8,2]
wid = 0.7
#Here we import ther matplotlib package with alias name as pltimport matplotlib.pyplot as plt
plt.bar(x,y,wid, label="Example one", color = 'g')
#plt.bar([2,4,6,8,10],[8,6,2,5,6], label=”Example two”, color=’g’)
#plt.legend(wordcounts)
plt.xlabel('bar number')
plt.ylabel('bar height')
plt.title('Диаграмма предложений')
#plt.show()