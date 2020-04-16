import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = (12,8)
import seaborn as sns
 
import os 
from os import path
from string import punctuation


def clean_strings(val):
	no_punc = ""
	for char in val:
		if char not in (punctuation):
			no_punc += char

	return no_punc


####### list all files

files = [file for file in os.listdir("./") if file[-3:] == "csv"]
print(files)

# ############################################# Shops.csv

# shops = pd.read_csv("./shops.csv")

# print(shops.head())
# print(shops.shape)

# # check any duplicates

# print(shops.shape[0] == shops.nunique()) #true, no duplicate so far

# # Manual explorations

# print(shops['shop_name'])
# print(len(shops['shop_name']), len(set(shops['shop_name']))) #no name is duplicated
# print(shops.duplicated('shop_name').unique())

# groupbySize = shops.groupby('shop_id').size()
# print(groupbySize)

# print(shops.isnull().sum()) # no null


# print(shops.sample(15))

# ###### Cleaning Shop names 

# clean_shop_names = shops['shop_name'].apply(clean_strings)
# print(clean_shop_names)

# shops = shops.join(clean_shop_names, on=['shop_id'], rsuffix="_clean")


# ############################# Items_category.csv
# items_cat = pd.read_csv("./item_categories.csv")
# print(items_cat.shape)

# print(items_cat.head(), "\n\n")
# print(items_cat.sample(10))

# print ("\n\n\n")

# print(items_cat.info(), "\n\n")
# print(items_cat.describe())

# #### duplicates?

# print(items_cat.shape[0] == items_cat.nunique()) # no duplicates


# pd.set_option("display.max_rows", items_cat.shape[0])
# print(items_cat)

# ################# items.csv

# items = pd.read_csv("./items.csv")

# print(items.shape)

# print(items.head(), "\n\n" )
# print(items.sample(10), "\n\n")

# print(items.describe(), "\n\n")
# print(items.info(), "\n\n")


# ## find duplicated?

# print(len(items['item_name']) == len(items['item_name'])) # no duplicates?

# print(items['item_name'].duplicated().unique()) #no duplicates


####### Sales
sales = pd.read_csv("./sales_train.csv")

# print(sales.shape)

# print("\n\n")

# print(sales.head())

# print("\n\n")

# print(sales.describe())

# print("\n\n")

# print(sales.info())


print("\n\n")

# print(sales['date_block_num'].unique(), sales['date_block_num'].nunique())
# print(sales['item_cnt_day'].unique(), sales['item_cnt_day'].nunique())

#### nulls?

# print(sales.isnull().sum(axis=0).sum()) # no null? strange!!!

# no_itemPrice = sales['item_price'] <= 0

# print(sales[no_itemPrice]) #only item with -1.0 price. there must be some other mistakes also. Can be found in VIZ




train = pd.read_csv("./sales_train.csv", parse_dates=['date'])

# print(train.head())

months = train['date'].dt.month

# sns.distplot(train['item_cnt_day'])

# plt.show()


print(train[['date','item_cnt_day']].set_index('date').resample("M").sum())


train[['date', 'item_cnt_day']].set_index('date').resample("M").sum().plot()
plt.legend()

print(train[['date', 'item_cnt_day']].set_index('date').resample("M").sum().index.max())
print(train[['date', 'item_cnt_day']].set_index('date').resample("M").sum().index.min())

### oneblock

dateBlock0 = train['date_block_num'].isin([0])
train[dateBlock0].set_index('date').resample("M").sum()['item_cnt_day'].plot()
plt.legend()


### all dateblock plots

dateBlocks = train['date_block_num'].unique()
for (i,dateBlock) in enumerate(dateBlocks): 

	print(dateBlock)
	block = train['date_block_num'].isin([dateBlock])
	plt.title(f"{dateBlock}_MONTH_SUM_sampled")
	train[block].set_index('date').resample("M").sum()['item_cnt_day'].plot()

	if (i%4==0 and i!= 0): 
		plt.show()
		plt.legend()

# plt.show()
