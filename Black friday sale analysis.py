import pandas as pd
df=pd.read_csv(r'C:\Users\hp\Downloads\blackfriday.csv')
print(df)

#task1.find shape of dataframe i.e number of rows and column

#check the the shape of dataframe
print(df.shape)
#check dimention of dataframe
print(df.ndim)

#Task 2. Print top 10 rows and last 10 rows from dataset

# Lets view the first five rows of the dataframe using head()
print(df.head(5))
# Lets customize and check for top 10 rows
print(df.head(10))
# We can also check rows from last using tail().By default , it also give last 5. Lets check for last 10 rows
print(df.tail(10))

#Task 3. Check if there is any duplicate

#checking for duplicate rows
print(sum(df.duplicated()))

#Task 4. Create new dataset with all product related columns.

# Lets check columns present in dataframe
print(df.columns)
# First of all , lets check for all columns which is having details related to product
#Lets try to create another dataset which will be subset of original and will have columns related to products.
print([i for i in df.columns if 'product' in i])
# Lets create new dataframe with these product related columns
df_product = df[['Product_ID', 'Product_Category_1', 'Product_Category_2', 'Product_Category_3']]
print(df_product)
# axes returns a list of the row axis labels as well as columns
print(df.axes)
# values returns the Series of values as ndarray.
print(df.Gender.values)
# Size returns the number of elements in the underlying dataset/column. Lets try with dataset first.
print(df.size)
# Lets try to check size of gender column
print(df.Gender.size)

#Task 8. Check for all columns datatype

# Lets use info() function
df.info()
# Lets only check datatype of each columns
print(df.dtypes)

#Task 9. Generate descriptive statistical values for numerical columns.
# Lets use describe on top of our dataset
print(df.describe())

#Task 10. Try to use same function on categorical columns
# Apart from int and float , we have datatype as object . Lets do for those columns
print(df.describe(include=['object']))

#Task 11. Get percentage distribution of each product id available in dataset and find with highest occuring product id in dataset.
#We can use value_counts for checking different values in categorical columns
# lets check for Product_ID
print(df['Product_ID'].value_counts())
# Get normalized value
print(df['Product_ID'].value_counts(normalize=True))
# check sum of all percentage values
print(round(df['Product_ID'].value_counts(normalize=True)*100,3))
# check sum of all percentage values
print(round(df['Product_ID'].value_counts(normalize=True)*100,3).sum())

#Task 12 . Check for columns having null values and count of null contaning rows.
# Lets check on our dataset
print(df.isnull().sum())
# Print Product_Category_2
print(df.Product_Category_2)
# Print Product_Category_3
print(df.Product_Category_3)

#Task 13. Handle missing value using dropping and imputing both options.
#lets first try with drop option. dropping product_category_2 using axis 1
df_temp=df.drop('Product_Category_2',axis=1,inplace=False)
# Verify with info().
print(df_temp.info())
# Verify with isnull()
print(df_temp.isnull().sum())
# Get index for all rows with Product_Category_3 missing
print(df_temp[df_temp.Product_Category_3.isnull()].index)
# Drop Product_Category_3 using axis 0
df_temp=df_temp.drop(df_temp[df_temp.Product_Category_3.isnull()].index,axis=0,inplace=False)
# Verify using info()
df_temp.info()
#here we will fill the missing values with forward or backward filling.
#The pad or fill option fill values forward, while bfill or backfill option fill values backward.
# Impute using forward filling
df=df.fillna(method='pad')
# Verify using isnull()
print(df.isnull().sum())
#We can see that the Product_Category_2 and Product_Category_3 have 1 missing value. We can use the head() to check this.
# Print both columns
print(df[['Product_Category_2','Product_Category_3']].head())
# Impute using backword filling
df=df.fillna(method='backfill')
# Verify using isnull()
print(df.isnull().sum())

### Indexing and slicing in pandas 

#Task 14. Print age and occupation columns using loc and select 1st, 5th and 10th rows with 1st, 4th and 7th columns using iloc
# make a copy of dataframe
df1=df.copy()
print(df1)
# select first row of dataframe using loc
print(df1.loc[0])
# Lets try to print 'Purchase' for all rows using loc
print(df1.loc[:,'Purchase'])
#select first five rows for a specific column 'purchase'
print(df1.loc[:4,'Purchase'])
# Print 'Age' and 'Occupation' using loc
print(df1.loc[:,['Age','Occupation']])
# We can also specify row label. Lets print first five rows with Age and Occupation columns
df1.loc[[0,1,3,4],['Age','Occupation']]

#Task 15 . fetch row having maximum purchase amount with complete row details
# get index of first occurence of maximum Purchase value 
print(df1['Purchase'].idxmax())
# get values of maximum purchase amount
print(df1.Purchase[df1['Purchase'].idxmax()])
# get the row with the maximum Purchase value 
print(df1[df1['Purchase']==23961])

#Task 16. Get the purchase amount from 3rd row
# get value at 3rd row and Purchase column pair
print(df1.at[3,'Purchase'])
# get value at 3rd row and 11th column pair
print(df1.iat[2,11])

#Task 17.find the purchase amount for a user_id (1006039) and product_id (P00371644)
purchase_amount=df1.loc[((df1['User_ID']==1006039)&(df1['Product_ID']=='P00371644')),'Purchase']
print(purchase_amount)

#Task 18. find the user those are in city 'A' with more than 4 years and purchase amount more than 10000
print(df1[(df1['City_Category']=='A')&(df1['Stay_In_Current_City_Years']=='4+')&(df1['Purchase']>10000)])

#Task 19. Discard all female users those are in city 'B' with 3 years and purchase amount less than 5000
print(df1[~((df1['Gender']=='F')&(df1['City_Category']=='B')&(df1['Stay_In_Current_City_Years']=='3')&(df1['Purchase']<5000))])

#Task 20. find the record in dataset with below details :
#[1006038,'P00375436','F','55+',1,'C','2',0,20,2.0,11.0,365]
values=[1006038,'P00375436','F','55+',1,'C','2',0,20,2.0,11.0,365]
df1_indexed=df1.isin(values)
print(df1_indexed)
# Lets use all condition
df1_indexed=df1.isin(values).all(axis=1)
print(df1[df1_indexed])

#Task 21. Visualize records with Occupation value 10 and mask everything left.
newdf=df1.mask(df1['Occupation'] !=10)
print(newdf.head())

#Task 22. Sort dataset row wise and column wise
# Sort dataset row wise
print(df1.sort_index())
# Sort dataset column wise
print(df1.sort_index(axis=1))
# Sort row wise in descending order
print(df1.sort_index(ascending=False))

#Task 23. Find top 20 most revenue generated customer and their purchased product id
# Lets try to sort dataset using Purchase column
print(df1.sort_values(by=['Purchase']))
# Sort by multiple columns
print(df1.sort_values(by=['Age','Purchase']).head(10))
# Lets get top 20
top20=df1.sort_values(by=['Purchase'],ascending=False).iloc[:20,:]
print(top20)
# Visualize products included in top 20
print(top20.Product_ID.value_counts())

#Task 24. Find which age group is much active for purchasing product from website
# Lets use unique to get distinct values
print(df1['Gender'].unique())
# Lets use value_counts to get count of distinct values
print(df1['Gender'].value_counts())
# Lets get age count sorted in descending order
print(df1['Age'].value_counts(ascending=False))

#Task 25. Generate list of User ID with corresponding age and find the total count of purchases thet have done.
# Lets get list first using values anf tolist
print(df1[['User_ID','Age']].values.tolist())
# Lets check for count of purchases for all distinct user_id and age combination
print(df1[['User_ID','Age']].value_counts())

#Task 26. Get different statistical values for Purchase column
import numpy as np
# Lets use describe on Purchase
print(df1['Purchase'].describe())

#Task 27. Find the total amount generated via website by selling product
# Lets use np.sum aggregation to get total puchased amount
print(df1['Purchase'].aggregate(np.sum))
# find sum and mean value after doing aggregation over purchase column
print(df1['Purchase'].aggregate([np.sum,np.mean]))
# find mean for 'Product_Category_1', 'Product_Category_2', 'Product_Category_3'
print(df1[['Product_Category_1','Product_Category_2','Product_Category_3']].aggregate(np.mean))
# Find mean and sum for 'Product_Category_1', 'Product_Category_2', 'Product_Category_3'
print(df1[['Product_Category_1','Product_Category_2','Product_Category_3']].aggregate([np.sum,np.mean]))

#Task 28. Tag records to 'high focused' transaction where purchase amount has been more than 5000. Remaining can be tagged as general transaction.
# Try to use apply function on Product_Category_1
print(df1.Product_Category_1.apply(lambda x : x*10))
# Lets add new column as 'category' which will have tags based on purchase amount
df1['Category']=df1.Purchase.apply(lambda x : 'High Focused' if x > 5000 else 'General')
print(df1.head())
# Lets check value for high focused row
print(df1.Category.value_counts())

#Task 30. Create new columns based on City_Category values and drop the original column
# Check different values for City_Category
print(df1.City_Category.value_counts())
# Apply get_dummies function to get new columns
dummy_df=pd.get_dummies(df1.City_Category,drop_first=True)
print(dummy_df.head())
# Concatenate both dataframes
df1=pd.concat([df1,dummy_df],axis=1)
print(df1)
#drop orignal one
df1.drop(['City_Category'],axis=1,inplace=True)
print(df1.head())
#verify shape
print(df1.shape)






