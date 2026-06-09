import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
print("Loading Amazon Dataset") #LOADING DATASET
df=pd.read_csv("AmazonData.csv")
print("\n [STEP 1]Data Audit") #TRACK AND FLAG DATA CORRUPTION
expected_price=df['price']*(1-(df['discount']/100))
corrupted_mask=abs(df['final_price']-expected_price)>1.0 #IDENTIFYING CORRUPTED ROWS
total_corrupted=corrupted_mask.sum()
print(f"Detected {total_corrupted} rows with corrupted pricing math")
print("\n [STEP 2] Cleaning And Recalculation") #DATA CLEANING(BUSINESS LOGIC IMPUTATION)
df.loc[corrupted_mask,'final_price']=round(expected_price[corrupted_mask],2)
print("Corruption Applied Successfully!")
re_check_expected=df['price']*(1-(df['discount']/100))
remaining_corrupted=abs(df['final_price']-re_check_expected>1.0).sum()
print(f"Remaining pricing math anamolies after cleaning:{remaining_corrupted}")
print("\n [STEP 3] Exporting Cleaned Dataset")
df.to_csv("AmazonData_Cleaned.csv",index=False)
print("Success!Your pristine dataset is saved as 'AmazonData_cleaned.csv'.")

#EXPLORATORY VISUALIZATION
#print("missing values")
#print(df.isnull().sum())
#print(df['user_id'].sum(numeric_only=True))
x=df['price']
y=df['rating']
priceCount=(df['price']).values
rateCount=(df['rating']).values
plt.scatter(priceCount,rateCount,color="blue",s=1,alpha=0.1)
plt.ylabel("Rating")
plt.title("Product Price VS Customer Rating")
plt.show()
avg_rating = df.groupby('category')['rating'].mean()
avg_rating.plot(kind='bar')
plt.xlabel("Category")
plt.ylabel("Average Rating")
plt.title("Average Rating by Category")
plt.show()
