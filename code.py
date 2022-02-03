#Name: Anooshka Bajaj

import pandas as pd
df=pd.read_csv(r'E:\pima_indians_diabetes_miss.csv')
import matplotlib.pyplot as plt


#1
x=df.columns                        
y=df.isnull().sum()                 #to find the number of missing values i.e. NaN in a single dataframe column
plt.bar(x,y)
plt.ylabel('Number of missing values')
plt.xlabel('Attributes')
plt.show()

print(y)               #to display the number of missing values of each attribute


#2

#2(a)
del_tup1=[]
for i in df.index:
    if df.iloc[i].isnull().sum() >= (1/3)*len(df.columns):
        del_tup1.append(i)
        
m=df.drop(del_tup1)
print('Total number of tuples deleted:', len(del_tup1))
print('\nRow numbers of the deleted tuples:', [(x) for x in del_tup1])          


#2(b)
del_tup2=[]
for j in m.index:
    if(str(m.loc[j]['class'])=='nan'):
        del_tup2.append(j)                          
        
n=m.drop(del_tup2)
print('Total number of tuples deleted:', len(del_tup2))
print('\nRow numbers of the deleted tuples:', del_tup2)


#3
print('The number of missing values in each attribute:')
print(n.isnull().sum())

print('\nThe total number of missing values in the file:')
print(n.isnull().sum().sum())


#4
pd.set_option('display.max_rows',1000)       #to display all rows
pd.set_option('display.max_columns',50)         #to display all columns

#4(a) Mean

#(i) 
print('Original data:')
print(df.describe().round(2))
print(df.mode())

b=n.fillna(n.mean())
print('Data filled by mean:')
print(b.describe().round(2))
print(b.mode())

#(ii) RMSE




#4(b) Linear interpolation 

#(i)
a=n.interpolate('linear')
print('Data filled by interpolation:')
print(a.describe().round(2))
print(a.mode())

#(ii) RMSE




#5

#(i)
#finding outliers
l1=[]
p1=a['Age']
outliers1=p1.between((2.5*p1.quantile(.25)) - (1.5* p1.quantile(.75)),(2.5*p1.quantile(0.75)) - (1.5*p1.quantile(0.25)))
for k in p1.index:
    if (str(outliers1[k]) == 'False'):
        l1.append(p1[k])
print('Outliers in Age :', l1)


l2=[]
p2=a['BMI']
outliers2=p2.between((2.5*p2.quantile(.25)) - (1.5* p2.quantile(.75)),(2.5*p2.quantile(0.75)) - (1.5*p2.quantile(0.25)))
for q in p2.index:
    if (str(outliers2[q]) == 'False'):
        l2.append(p2[q])
print('Outliers in BMI:', l2)

#boxplot
a.boxplot(column=['Age'], figsize=(8,8))    #boxplot for Age
plt.ylabel('Age in years')
plt.title('Without replacing Outliers')
plt.show()

a.boxplot(column=['BMI'], figsize=(8,8))    #boxplot for BMI
plt.title('Without replacing Outliers')
plt.show()

#(ii)
#replacing outliers with median
g=a.replace(l1,p1.median())
g.boxplot(column=['Age'])    #boxplot for Age
plt.ylabel('Age in years')
plt.title('After replacing Outliers')
plt.show()

f=a.replace(l2,p2.median())
f.boxplot(column=['BMI'])    #boxplot for BMI
plt.title('After replacing Outliers')
plt.show()









 













