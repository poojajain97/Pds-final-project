#importing all relevant modules
import numpy as np
import pandas as pd
from pandas import *
from time import time
import matplotlib.pyplot as plt

# PART-1 : DATA PREPROCESSING
# reading CSV file
'''Removing header and giving column names
Converting Nan values to empty string values'''
df = pd.read_csv("mtsamples.csv", header=None, names=["serial no","description", "medical_specialty", "Diagnosis", "transcription", "keywords"])
df.fillna('', inplace=True)

# analysing the dimensions of the data
print(df.shape)

#Converting medical speciality into a list
list_sp = df['medical_specialty'].tolist()

#Spliting the values and creating a list of value
my1_list = list_sp
res_overall = [item.split(',') for item in my1_list]
res_overall_flat = [item for l in res_overall for item in l]

# Grouping the data on the basis of the medical speciality
group=df.groupby("medical_specialty")



'''Taking the subgroup 'SURGERY' and analysing all data entries under the speciality of surgery'''
#using loc to access multiple columns by name: 'surgery'
surg=df.loc[df.medical_specialty==" Surgery", : ]

#1. Converting 'diagnosis' column data to list
di_list = surg['Diagnosis'].tolist()

#Spliting the values and creating a list of values 
my1_list = di_list
di_1 = [item.split(',') for item in my1_list]
di_1_flat = [item for l in di_1 for item in l]
# print(di_1_flat)

#Splitting and removing all spaces ' ' before and after words, to make data uniform
di_2 = [item.split(' ') for item in di_1_flat]
di_2_flat = [item for l in di_2 for item in l]
di_2_final=[i for i in di_2_flat if i!='']
print(di_2_final)



#2. Converting 'keywords' column data to list
#Spliting the values and creating a list of values 
key_list= surg['keywords'].tolist()
my2_list= key_list
key_1= [item.split(',') for item in my2_list]
key_1_flat= [item for l in key_1 for item in l]
print(key_1_flat)



#3. Converting transcription to list
#Spliting the values and creating a list of values 
#Splitting and removing all spaces ' ' before and after words, to make data uniform
trans_list= surg['transcription'].tolist()

trans_1 = [item.split(',') for item in trans_list]
trans_1_flat = [item for l in trans_1 for item in l]
print(trans_1_flat)

trans_2 = [item.split(' ') for item in trans_1_flat]
trans_2_flat = [item for l in trans_2 for item in l]
trans_2_final=[i for i in trans_2_flat if i!='']
print(trans_2_final)




# PART-2: DATA ANALYSIS

#Question 1: What are the number of entries under the speciality 'Surgery'?
print(f'Total number of entries in surgery are {len(surg)}')
#Answer: Total number of entries in surgery are 1103

#Question 2: Any patients of circumcision?
s='Circumcision'
if s in di_2_final:
    print(f'{s} is present in the list')
else:
    print(f'{s} is not present in the list')
#Answer: 'Circumcision' is present in the list

#Question 3: What is the number of patients undergoing Circumcision?
s= 'Circumcision'
occurence = {item: di_2_final.count(item) for item in di_2_final}
# print(occurence.get(s))
print(f'Number of patients undergoing circumcision is {occurence.get(s)}')
# Other method of doing the same
print('Number of patients undergoing circumcision is ' + str(di_2_final.count('Circumcision')))
#Answer: Number of patients undergoing circumcision is 13

#Question 4: What is the total number of laparoscopic surgeries?
s= 'Laparoscopy'
t= 'Laparoscopic'
occurence = {item: di_2_final.count(item) for item in di_2_final}
print(f'Number of patients undergoing laparoscopic surgeries is {occurence.get(s)+occurence.get(t)}')
#Answer: Number of patients undergoing laparoscopic surgeries is 56

#Question 5: What is the number and distribution of different dignostic procedures?
occurence = {item: di_2_final.count(item) for item in di_2_final}
x=['Gastroscopy','Arthroscopy','Cystoscopy','Biopsy','Laryngoscopy']
y=[occurence['Gastroscopy'],occurence['Arthroscopy'],occurence['Cystoscopy'],occurence['Biopsy'],occurence['Laryngoscopy']]
d = {x[i]: y[i] for i in range(len(x))}
print(f'Number of diagnostic procedures is {d} respectively')
#Answer: Number of diagnostic procedures is {'Gastroscopy': 4, 'Arthroscopy': 10, 'Cystoscopy': 7, 'Biopsy': 38, 'Laryngoscopy': 5}

#Question 6:  What is total number of keywords in Surgery?
my_list_key = key_1_flat
my_list_key = list(dict.fromkeys(my_list_key))
print("Total number of keywords in surgery is: " + str(len(my_list_key)))
# Answer: Total number of keywords in surgery is: 6266

#Question 7: What is the number of times different types of anesthesia is used?
s= 'local'
t= 'General'
a1=[s,t]
b1=[trans_2_final.count(s), trans_2_final.count(t)]
print(f'Local anesthesia is used {trans_2_final.count(s)} times and general anesthesia is used {trans_2_final.count(t)} times')
#Answer: Local anesthesia is used 155 times and general anesthesia is used 376 times

#Question 8: how many patients have pain as chief complaint and how many have swelling as chief complaint?
s= 'pain'
t= 'swelling'
a=[s, t]
b=[trans_2_final.count(s),trans_2_final.count(t)]
print(f'Pain is a chief complaint {trans_2_final.count(s)} times while swelling is a chief complaint {trans_2_final.count(t)} times')
#Answer: Pain is a chief complaint 365 times while swelling is a chief complaint 29 times

#Question 9: What is the number of OBG cases wrongly assigned the speciality as surgery?
s,t,u,v,w='Delivery','Hysterectomy', 'Hysteroscopy', 'D&C','TAH'
occurence = {item: di_2_final.count(item) for item in di_2_final}
print(f'Number of OBG cases wrongly assigned the speciality as surgery is {occurence.get(s)+occurence.get(t)+occurence.get(u)+occurence.get(v)+occurence.get(w)}')
#Answer: Number of OBG cases wrongly assigned the speciality as surgery is 48

#Question 10: What is the number of surgeries of inguinal region?
print('Number of patients undergoing surgeries of inguinal region are ' + str(di_2_final.count('Inguinal')))
#Answer: Number of patients undergoing surgeries of inguinal region are 17



#PART-3: DATA VISUALIZATION

#Histogram of different medical specialities
t1 = res_overall_flat
plt.hist(t1, 40)
plt.title("Medical specialities")
plt.xlabel("Speciality")
plt.ylabel("Frequencies")
plt.xticks(rotation=90)
plt.show()


#Histogram plot of different diagnosis in surgery
t2 = di_list
plt.hist(t2, 70)
plt.title("Diagnosis in surgery")
plt.xlabel("Diagnosis")
plt.ylabel("Frequencies")
plt.xticks(rotation=90)
plt.show()


#Histogram plots of different diagnosis in surgery(Magnified)
t3 = di_list[1:50]
plt.hist(t3, 50)
plt.title("Diagnosis in surgery(magnified")
plt.xlabel("Diagnosis")
plt.ylabel("Frequencies")
plt.xticks(rotation=90)
plt.show()

t4= di_list[50:100]
plt.hist(t4, 50)
plt.title("Diagnosis in surgery(magnified")
plt.xlabel("Diagnosis")
plt.ylabel("Frequencies")
plt.xticks(rotation=90)
plt.show()

#Bar plot of the different types of diagnostic procedures in surgery
plt.bar(x,y)
plt.xlabel("Procedure")
plt.ylabel("frequency")  
plt.title("diagnostic procedures")
plt.show()

#Piechart of the different types of diagnostic procedures in surgery
fig = plt.figure(figsize =(10, 7))
plt.title('Diagnostic procedures in surgery')
plt.pie(y, labels = x)
plt.show()

#bar plot of the anesthetic procedures used during surgery
plt.bar(a1, b1)
plt.xlabel("anesthesia")
plt.ylabel("frequency")  
plt.title("anesthesia")
plt.show()

#bar plot of the most common chief complaints in surgery
plt.bar(a, b)
plt.xlabel("chief complaint")
plt.ylabel("frequency")  
plt.title("Chief complaints")
plt.show()

