# Data-Cleaning
Handling Missing Values and Outlier Analyses.
I am given with two csv files. The “pima_indians_diabetes_miss.csv” is a file that contains some missing values. The “pima_indians_diabetes_original.csv” is the 
original file without any missing values. This dataset is originally from the National Institute of Diabetes and Digestive and Kidney Diseases, USA. The objective of this dataset is to predict whether a patient has diabetes based on diagnostic measurements. 

Following are the details of the attributes in the data:\
• pregs (Pregnancies) : Number of Pregnancies\
• plas (Glucose) : Plasma glucose concentration a 2 hours in an oral glucose tolerance test.\
• pres (Blood Pressure) : Diastolic blood pressure (mm Hg).\
• skin (Skin Thickness) : Triceps skin fold thickness (mm).\
• test (Insulin) : 2-Hour serum insulin (mu U/ml).\
• BMI (BMI) : Body mass index (weight in kg/(height in m)^2).\
• pedi (Diabetes pedigree function) : Diabetes pedigree function.\
• Age (Age) : Age of patients (years).\
• Class (Outcome) : Class variable (0 or 1). 0 indicates not presence of diabetics and 1 indicates presence of diabetics. 268 patients out of 768 are 1, the others are 0.

I have written a python program (with pandas) to do the following:

1. Plot a graph of the attribute names with the number of missing values in them.
 
2. Deleting Tuples:\
a. Delete the tuples having equal to or more than one third of attributes with missing values. Print the total number of tuples deleted and also print the row numbers of 
the deleted tuples. \
b. Drop the tuples having missing value in the target (class) attribute. Print the total number of tuples deleted and also print the row numbers of the deleted tuples.

3. After step 2, count and print the number of missing values in each attributes. Also find and print the total number of missing values in the file (after the deletion of tuples).

4. Experiments on filling missing values:

   a. Replace the missing values by mean of their respective attribute. 
   i. Compute the mean, median, mode and standard deviation for each attributes 
   and compare the same with that of the original file. 
   ii. Calculate the root mean square error (RMSE) between the original and replaced values for each attribute. Plot these RMSE with respect to the attributes.

   b. Replace the missing values in each attribute using linear interpolation technique. 
   i. Compute the mean, median, mode and standard deviation for each attributes 
   and compare with that of the original file. 
   ii. Calculate the root mean square error (RMSE) between the original and replaced values for each attributes. Plot these RMSE with respect to the attributes. 

5. Outlier detection:\
i. After replacing the missing values by interpolation method, find the outliers in the attributes “Age” and “BMI”. \
ii. Replace these outliers by the median of the attribute. Plot the boxplot again and 
observe the difference with that of the boxplot in 5.i. 
