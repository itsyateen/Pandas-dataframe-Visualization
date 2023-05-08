#!/usr/bin/env python
# coding: utf-8

# In[27]:


import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')


# In[28]:


ab=pd.read_excel('D:\Data Science study Material\Python\Pandas Project files\Sales Dataset.xlsx')


# In[29]:


ab.head(2)


# In[30]:


ab.tail(2)


# In[31]:


# Remove the unwanted or missing data.


# In[32]:


ab.isnull().sum()  # columns name "Column1" has to many null values, hence we will drop that column from data


# In[5]:


# dispose the index & column1 columns 


# In[33]:


ab


# In[34]:


ab.drop('index',axis=1,inplace=True)
ab


# In[36]:


ab.drop('Column1',axis=1,inplace=True)
ab


# In[37]:


ab.tail(5)


# In[10]:


# remove the rows which are having Null values 


# In[38]:


ab.drop(34866,inplace=True) #removed row no. 34866 as it contain null values
ab


# In[39]:


ab.tail(2)


# In[40]:


ab.isnull().sum()    # as we can see thre is no null values in the dataset now.
                     # we have clean the data and get the information which is required for further anaysis.


# # Duplicated function

# In[41]:


ab.duplicated()                    # checking if we have any duplicate records in the datadrame
                                   # There is no dupicate data. 


# In[15]:


#retrieve the year wise sales report   - using LOC function


# # Year = 2015 , Quarter 1 = Sales report

# In[42]:


Year = 2015
Months = ['January','February','March']
Qtr1_2015 = ab.loc[(ab['Year']== 2015) & (ab['Month'].isin(Months)),['Year','Month','Revenue']]
Qtr1_2015


# In[17]:


# Count Product Category wise sale purchsed by Male and Female 

# there are 3 product Categories 
    #i)Accessories ii)Bikes iii)Clothing
# Gender wise sales report for product Category.


# In[43]:


ab[["Customer Gender","Product Category"]].value_counts()


# In[19]:


# Country wise Revenue for year 2016 for all categories
   # (This shows the Average revenue from the countries)


# In[44]:


ab.groupby(by = 'Country').Revenue.mean()


# In[21]:


# Sub Category wise revenue 


# In[45]:


ab.sort_values(by = 'Sub Category')[['Sub Category','Revenue']]


# In[25]:


# LEN function provides the number of rows available in the dataframe 


# In[20]:


len(ab)    # 34,866 rows in the dataframe 


# In[27]:


# RETRIEVE ONLY COLUMNS (Country||State || Product Category || Sub Category || Quantity) 


# In[21]:


ab.iloc[::, 5:10]


# # Random function + add a column in the dataframe with random inputs.

# In[29]:


Random_col = np.random.randint(10,size=len(ab))


# In[30]:


ab.insert(8,'Random_col',Random_col)


# In[31]:


ab     # as we can see the result the column "Random_col" has been added at the 8th position 


# # Delete the newly added column "Random_col"

# In[32]:


ab.drop("Random_col",axis = 1,inplace=True)
ab


# # SAMPLE FUNCTION

# In[33]:


ab.sample()


# # Unique Function

# In[ ]:


# find the unique values from sub category column


# In[34]:


ab['Sub Category'].unique()   


# # Nunique function

# In[35]:


ab["Sub Category"].nunique()   # this shows the count of unique values 


# # q-cut function

# In[38]:


# check how many customer comes from the particular age category


# In[38]:


pd.qcut(ab["Customer Age"],q=5).value_counts()


# In[37]:


ab['Customer Age'].describe()


# # nlargest & nsmallest function

# In[38]:


ab.nlargest(3,'Revenue')


# In[39]:


ab.nsmallest(3,"Revenue")


# # stack & unstack function

# In[40]:


ab.stack()  # this function used to reshape a DataFrame by pivoting the columns into rows


# In[41]:


ab.unstack() 


# # Apply Function

# In[ ]:


# Defined Function + sort cx type with new columns "Customer type"


# In[42]:


def Cxtype(Age):
    if Age >80:
        return "Trusted cx"
    elif Age >60 and Age<80:
        return"Loyal cx"
    elif Age >45 and Age<60:
        return "Bonding cx"
    elif Age >35 and Age<45:
        return"Growing cx"
    elif Age >20 and Age <35:
        return"Yough cx"
    else:
        return "Cild"


# In[43]:


ab['Customer type']=ab['Customer Age'].apply(Cxtype)
ab


# # Repalce function

# In[ ]:


#replace Customer type "Yough cx" to "Target cx", don't make the changes permanent.


# In[44]:


ab["Customer type"].replace("Yough cx","Target cx")


# # Between Function 

# In[45]:


# this function results in bool values, we can also use a variabel for the same.
# Age Group between 26 - 35 = "True" , apart from that = "False"


# In[46]:


ab['Customer Age'].between(26,35)


# # shape function

# In[47]:


ab.shape                          # thisn function gives the shape of the Dataframe rows 34866, columns 


# # astype function

# In[ ]:


#convert "Customer Age" columns to int format


# In[48]:


ab['Customer Age'] = ab['Customer Age'].astype(int)


# In[49]:


ab.head(3)


# In[ ]:





# # Sales Data Analytics 

# # Show the first Quarter comparision of sales revenue for year 2015 & 2016

# In[54]:


# Calculation of Sales revenue for year 2015 Quarter 1


# In[50]:


Year = 2015
Months = ['January','February','March']
Qtr1 = ab.loc[(ab['Year']== 2015) & (ab['Month'].isin(Months)),['Year','Month','Revenue']]
Qtr1


# # Total Revenue of Quarter 1

# In[51]:


Qtr1['Revenue'].sum()


# In[54]:


sb.catplot(x='Month',y='Revenue',data=Qtr1)


# In[53]:


import matplotlib.pyplot as plt
import seaborn as sb
import warnings
warnings.filterwarnings("ignore")


# In[58]:


# Calculation of Sales revenue for year 2016 Quarter 1


# In[55]:


Year = 2016
Months = ['January','February','March']
Qtr1_2016 = ab.loc[(ab['Year']== 2016) & (ab['Month'].isin(Months)),['Year','Month','Revenue']]
Qtr1_2016


# In[56]:


Qtr1_2016['Revenue'].sum()


# In[ ]:


# 2016 Quarter 1 Revenue status 


# In[57]:


sb.distplot(Qtr1_2016['Revenue'])
plt.show()


# In[58]:


Comparison_sales_Revenue = [740764.0,5339426.0]


# In[59]:


plt.bar(['2015 Q1 Sales','2016 Q1 Sales'],Comparison_sales_Revenue,color='blue')
plt.title('Quarter 1 Sales Comparision 2015 vs 2016')
plt.xlabel('Month Jan-Feb-Mar')
plt.ylabel('Sales Revenue')
plt.show()


# # Show the 2nd Quarter comparision of sales revenue for year 2015 & 2016

# In[60]:


Year = 2015
Months = ['April','May','June']
Qtr2_2015 = ab.loc[(ab['Year']==2015) & (ab['Month'].isin(Months)),['Year','Month','Revenue']]
Qtr2_2015


# In[61]:


Qtr2_2015['Revenue'].sum()


# In[62]:


Year = 2016
Months = ['April','May','June']
Qtr2_2016 = ab.loc[(ab['Year']==2016) & (ab['Month'].isin(Months)),['Year','Month','Revenue']]
Qtr2_2016


# In[63]:


Qtr2_2016['Revenue'].sum()


# In[64]:


Comparision_sales_revenue_Q2 = [942528.0,6565767.0]


# In[65]:


plt.bar(['2015 Quarter 2','2016 Quarter 2'],Comparision_sales_revenue_Q2,color='blue')
plt.title('2015 vs 2016 Quarter 2 Sales Comparision')
plt.xlabel('Month Apr-May-Jun')
plt.ylabel('Sales revenue')
plt.show()


# # Show the 3rd Quarter comparision of sales revenue for year 2015 & 2016

# In[66]:


Year = 2015
Months = ['July','August','September']
Qtr3_2015 = ab.loc[(ab['Year']==2015) & (ab['Month'].isin(Months)),['Year','Month','Revenue']]
Qtr3_2015       


# In[67]:


Qtr3_2015['Revenue'].sum()


# In[68]:


Year = 2016
Months = ['July','August','September']
Qtr3_2016 = ab.loc[(ab['Year']==2016) & (ab['Month'].isin(Months)),['Year','Month','Revenue']]
Qtr3_2016


# In[69]:


Qtr3_2016['Revenue'].sum()


# In[70]:


Comparision_sales_revenue_Q3 = [3332485.0,491612.0]


# In[71]:


plt.bar(['2015 Quarter 3','2016 Quarter 3'],Comparision_sales_revenue_Q3,color='Green')
plt.title('2015 Vs 2016 Quarter 3 Sales Comparision')
plt.xlabel('Month Jul-Aug-Sept')
plt.ylabel('Sales Revenue')
plt.show()


# In[72]:


# Assuming company is performing its 3rd quarter 2016, the above bar shows the july month revenue of 3rd quarter 2016. 
# which means we can plan the strategy to hit the highest target compare to previous year Q3 sales.


# In[73]:


# from 80 till 99 = "Trusted cx"
# 60 to 80 = "Loyal cx"
# 45 to 60 = "Target cx"
# 35 to 45 = "Growing cx"
# 20 to 35 = "Yough cx"
# below 20 = "Child cx"


# # show the Age group wise Sales Revenue for 2015 and 2016

# In[74]:


ab.head(2)


# # 2015 Sales Age 80 - 99

# In[75]:


age_wise_sales_2015 = ab.loc[(ab['Year']==2015) & (ab['Customer Age'] >80) & (ab['Customer Age'] <99),['Customer Age','Country','State','Product Category','Revenue']]
print(age_wise_sales_2015)


# In[76]:


age_wise_sales_2015['Revenue'].sum()   # Total revenue from >80 Age cx 2015


# In[77]:


age_wise_sales_2015['Customer Age'].count()   # count of cx 2015 age > 80


# # 2016 Sales Age 80 - 99

# In[78]:


age_wise_sales_2016 = ab.loc[(ab['Year']==2016) & (ab['Customer Age'] >80) & (ab['Customer Age'] <99),['Customer Age','Country','State','Product Category','Revenue']]
print(age_wise_sales_2016)


# In[79]:


age_wise_sales_2016['Revenue'].sum()   # Total revenue from >80 Age cx 2016


# In[80]:


age_wise_sales_2016['Customer Age'].count()    # count of cx 2016 age > 80


# # 2015 sales Age 60 - 80

# In[81]:


age_wise_sales_loyalcx_2015 = ab.loc[(ab['Year']==2015) & (ab['Customer Age'] >=60) &(ab['Customer Age'] <80),['Customer Age','Country','State','Product Category','Revenue']]
print(age_wise_sales_loyalcx_2015)


# In[87]:


#total sales revenue of age group 60 - 80 2015


# In[82]:


age_wise_sales_loyalcx_2015['Revenue'].sum()


# In[89]:


# total number of cx (age group 60 - 80) 2015


# In[83]:


age_wise_sales_loyalcx_2015['Customer Age'].count()


# # 2016 sales Age 60 -80

# In[84]:


age_wise_sales_loyalcx_2016 = ab.loc[(ab['Year']==2016) & (ab['Customer Age'] >=60) & (ab['Customer Age'] <80),['Customer Age','Country','State','Product Category','Revenue']]
print(age_wise_sales_loyalcx_2016)


# In[92]:


#total sales revenue of age group 60 - 80 2016


# In[85]:


age_wise_sales_loyalcx_2016['Revenue'].sum()


# In[94]:


# total number of cx (age group 60 - 80) 2016


# In[86]:


age_wise_sales_loyalcx_2016['Customer Age'].count()


# # 2015 sales Age 45 - 60

# In[87]:


age_wise_sales_Bondingcx_2015 = ab.loc[(ab['Year']==2015) & (ab['Customer Age'] >=45) & (ab['Customer Age'] <60),['Customer Age','Country','State','Product Category','Revenue']]
print(age_wise_sales_Bondingcx_2015)


# In[100]:


# Total Sales revenue age group 45 to 60 2015


# In[88]:


age_wise_sales_Bondingcx_2015['Revenue'].sum()


# In[102]:


# Total no of customer age group 45 to 60 2015


# In[89]:


age_wise_sales_Bondingcx_2015['Customer Age'].count()


# # 2016 Sales Age 45 - 60

# In[90]:


age_wise_sales_Bondingcx_2016 = ab.loc[(ab['Year']==2016) & (ab['Customer Age'] >=45) & (ab['Customer Age'] <60),['Customer Age','Country','State','Product Category','Revenue']]
print(age_wise_sales_Bondingcx_2016)


# In[130]:


# Total Sales revenue age group 45 to 60 2016


# In[91]:


age_wise_sales_Bondingcx_2016['Revenue'].sum()


# In[106]:


# Total no of customer age group 45 to 60 2016


# In[92]:


age_wise_sales_Bondingcx_2016['Customer Age'].count()


# # 2015 Sales Age 35 - 45

# In[93]:


age_wise_sales_Targetcx_2015 = ab.loc[(ab['Year']==2015) & (ab['Customer Age'] >=35) & (ab['Customer Age'] <45),['Customer Age','Country','State','Product Category','Revenue']]
print(age_wise_sales_Targetcx_2015)


# In[ ]:


# Total Sales revenue age group 35 to 45 2015


# In[94]:


age_wise_sales_Targetcx_2015['Revenue'].sum()


# In[117]:


# Total no of customer age group 35 to 45 2016


# In[95]:


age_wise_sales_Targetcx_2015['Customer Age'].count()


# # 2015 Sales Age 20 - 35

# In[96]:


age_wise_sales_Youngcx_2015 = ab.loc[(ab['Year']==2015) & (ab['Customer Age'] >=20) & (ab['Customer Age'] <35),['Customer Age','Country','State','Product Category','Revenue']]
print(age_wise_sales_Youngcx_2015)


# In[ ]:


# Sales Revenue btwn age 20 - 35 


# In[98]:


sb.distplot(age_wise_sales_Youngcx_2015['Revenue'],hist=False,color='green')
plt.show()


# In[ ]:


# Total Sales revenue age group 20 to 35 2015


# In[99]:


age_wise_sales_Youngcx_2015['Revenue'].sum()


# In[ ]:


# Total no of customer age group 20 to 35 2015


# In[100]:


age_wise_sales_Youngcx_2015['Customer Age'].count()


# # 2015 Sales Age below 20

# In[101]:


age_wise_sales_Childcx_2015 = ab.loc[(ab['Year']==2015) & (ab['Customer Age'] <20),['Customer Age','Country','State','Product Category','Revenue']]
print(age_wise_sales_Childcx_2015)


# In[ ]:


# Total Sales revenue age group below 20


# In[102]:


age_wise_sales_Childcx_2015['Revenue'].sum()


# In[125]:


# Total no of customer age group below 20


# In[103]:


age_wise_sales_Childcx_2015['Customer Age'].count()


# # 2016 Sales age 35 -45

# In[104]:


age_wise_sales_Targetcx_2016 = ab.loc[(ab['Year']==2016) & (ab['Customer Age'] >=35) & (ab['Customer Age'] <45),['Customer Age','Country','State','Product Category','Revenue']]
print(age_wise_sales_Targetcx_2016)


# In[128]:


# Total Sales revenue age group 35 to 45 2016


# In[105]:


age_wise_sales_Targetcx_2016['Revenue'].sum()


# In[130]:


# Total no of customer age group 35 to 45 2016


# In[106]:


age_wise_sales_Targetcx_2016['Customer Age'].count()


# # 2016 Sales Age 20 - 35

# In[107]:


age_wise_sales_Youngcx_2016 = ab.loc[(ab['Year']==2016) & (ab['Customer Age'] >=20) & (ab['Customer Age'] <35),['Customer Age','Country','State','Product Category','Revenue']]
print(age_wise_sales_Youngcx_2016)


# In[109]:


sb.distplot(age_wise_sales_Youngcx_2016['Revenue'],hist=True,kde=False,color='green')
plt.show()


# In[ ]:





# In[133]:


# Total Sales revenue age group 20 to 35 2016


# In[110]:


age_wise_sales_Youngcx_2016['Revenue'].sum()


# In[135]:


# Total no of customer age group 20 to 35 2016


# In[111]:


age_wise_sales_Youngcx_2016['Customer Age'].count()


# # 2016 sales Age below 20

# In[112]:


age_wise_sales_Childcx_2016 = ab.loc[(ab['Year']==2016) & (ab['Customer Age'] <20),['Customer Age','Country','State','Product Category','Revenue']]
print(age_wise_sales_Childcx_2016)


# In[138]:


# Total Sales revenue age group below 20


# In[113]:


age_wise_sales_Childcx_2016['Revenue'].sum()


# In[140]:


# Total no of customer age group below 20


# In[114]:


age_wise_sales_Childcx_2016['Customer Age'].count()


# In[115]:


Sales_2015_by_age_2015 = [1383.0,199076.0,1853005.0,2728323.0,4774772.0,391212.0]


# # Sales comparision considering Age group 

# In[116]:


plt.bar(['80-99','60-80','45-60','35-45','20-35','<20'],Sales_2015_by_age_2015)
plt.title('Sales Revenue comparision by Age group Year 2015 ')
plt.xlabel('Age')
plt.ylabel('Sales Revenue 2015')
plt.show()


# In[117]:


Sales_2015_by_age_2016 = [10813.0,307039.0,2615050.0,4241002.0,4947773.0,274264.0]


# In[118]:


plt.bar(['80-99','60-80','45-60','35-45','20-35','>20'],Sales_2015_by_age_2016)
plt.title('Sales Revenue comparision by Age group Year 2016')
plt.xlabel('Age')
plt.ylabel('Sales Revenue 2016')
plt.show()


# In[119]:


ab.head(4)


# # 2015 Monthly Sales 

# # january month sales 2015

# In[120]:


january_month_2015 = ab.loc[(ab['Year']==2015) & (ab['Month']=='January') & (ab['Revenue']),['Month','Revenue','Country']]
print(january_month_2015)


# In[121]:


january_month_2015['Revenue'].sum()


# # february month sales 2015

# In[122]:


february_month_2015 = ab.loc[(ab['Year']==2015) & (ab['Month']=='February') & (ab['Revenue']),['Month','Revenue','Country']]
print(february_month_2015)


# In[123]:


february_month_2015['Revenue'].sum()


# # march month sales 2015

# In[124]:


march_month_2015 = ab.loc[(ab['Year']==2015) & (ab['Month']=='March') & (ab['Revenue']),['Month','Revenue','Country']]
print(march_month_2015)


# In[125]:


march_month_2015['Revenue'].sum()


# # April month sales 2015

# In[126]:


april_month_2015 = ab.loc[(ab['Year']==2015) & (ab['Month']=='April') & (ab['Revenue']),['Month','Revenue','Country']]
print(april_month_2015)


# In[127]:


april_month_2015['Revenue'].sum()


# # May month sales 2015

# In[128]:


may_month_2015 = ab.loc[(ab['Year']==2015) & (ab['Month']=='May') & (ab['Revenue']),['Month','Revenue','Country']]
print(may_month_2015)


# In[129]:


may_month_2015['Revenue'].sum()


# # June month sales 2015

# In[132]:


june_sales_2015 = ab.loc[(ab['Year']==2015) & (ab['Month']=="June"),['Month','Revenue','Country']]
print(june_sales_2015)


# In[134]:


june_sales_2015['Revenue'].sum()


# # July month sales 2015

# In[135]:


july_month_2015 = ab.loc[(ab['Year']==2015) & (ab['Month']=='July') & (ab['Revenue']),['Month','Revenue','Country']]
print(july_month_2015)


# In[136]:


july_month_2015['Revenue'].sum()


# # August month sales 2015

# In[137]:


aug_month_2015 = ab.loc[(ab['Year']==2015) & (ab['Month']=='August') & (ab['Revenue']),['Month','Revenue','Country']]
print(aug_month_2015)


# In[138]:


aug_month_2015['Revenue'].sum()


# # Sept month sales 2015

# In[139]:


sept_month_2015 = ab.loc[(ab['Year']==2015) & (ab['Month']=='September') & (ab['Revenue']),['Month','Revenue','Country']]
print(sept_month_2015)


# In[140]:


sept_month_2015['Revenue'].sum()


# # October month sales 2015

# In[141]:


oct_month_2015 = ab.loc[(ab['Year']==2015) & (ab['Month']=='October') & (ab['Revenue']),['Month','Revenue','Country']]
print(oct_month_2015)


# In[142]:


oct_month_2015['Revenue'].sum()


# # Nov month sales 2015

# In[143]:


nov_month_2015 = ab.loc[(ab['Year']==2015) & (ab['Month']=='November') & (ab['Revenue']),['Month','Revenue','Country']]
print(nov_month_2015)


# In[144]:


nov_month_2015['Revenue'].sum()


# # Dec monthl sales 2015

# In[145]:


dec_month_2015 = ab.loc[(ab['Year']==2015) & (ab['Month']=='December') & (ab['Revenue']),['Month','Revenue','Country']]
print(dec_month_2015)


# In[146]:


dec_month_2015['Revenue'].sum()


# In[147]:


Monthly_sales_2015 = [230549.0,259857.0,250358.0,284143.0,320629.0,320629.0,789054.0,1248185.0,1295246.0,1376969.0,1438928.0,2116097.0]


# # 2015 Monthly sales 

# In[148]:


plt.figure(figsize=(10,5))
xaxis= ['Jan','Feb','Mar','Apr','May','June','Jul','Aug','Sept','Oct','Nov','Dec']
yaxis = [230549.0,259857.0,250358.0,284143.0,320629.0,320629.0,789054.0,1248185.0,1295246.0,1376969.0,1438928.0,2116097.0]
plt.barh(xaxis,yaxis)
plt.title('2015 Monthly Sales')
plt.show()


# # 2016 Monthly Sales 

# # January month Sales 2016

# In[149]:


january_sales_2016 = ab.loc[(ab['Year']==2016) & (ab['Month']=="January"),['Year','Month','Revenue','Country']]
print(january_sales_2016)


# In[150]:


january_sales_2016['Revenue'].sum()


# # February month Sales 2016

# In[151]:


feb_sales_2016 = ab.loc[(ab['Year']==2016) & (ab['Month']=="February"),['Year','Month','Revenue','Country']]
print(feb_sales_2016)


# In[152]:


feb_sales_2016['Revenue'].sum()


# # March month Sales 2016

# In[153]:


mar_sales_2016 = ab.loc[(ab['Year']==2016) & (ab['Month']=="March"),['Year','Month','Revenue','Country']]
print(mar_sales_2016)


# In[154]:


mar_sales_2016['Revenue'].sum()


# # April month Sales 2016

# In[155]:


apr_sales_2016 = ab.loc[(ab['Year']==2016) & (ab['Month']=="April"),['Year','Month','Revenue','Country']]
print(apr_sales_2016)


# In[156]:


apr_sales_2016['Revenue'].sum()


# In[292]:


sb.violinplot(x='Country',y='Revenue',data=apr_sales_2016,)
plt.title('Country wise sales for the month of April 2016')
plt.show()


# # May month Sales 2016

# In[157]:


may_sales_2016 = ab.loc[(ab['Year']==2016) & (ab['Month']=="May"),['Year','Month','Revenue','Country']]
print(may_sales_2016)


# In[158]:


may_sales_2016['Revenue'].sum()


# # June month Sales 2016

# In[159]:


jun_sales_2016 = ab.loc[(ab['Year']==2016) & (ab['Month']=="June"),['Year','Month','Revenue','Country']]
print(jun_sales_2016)


# In[160]:


jun_sales_2016['Revenue'].sum()


# # July month Sales 2016

# In[161]:


jul_sales_2016 = ab.loc[(ab['Year']==2016) & (ab['Month']=="July"),['Year','Month','Revenue','Country']]
print(jul_sales_2016)


# In[162]:


jul_sales_2016['Revenue'].sum()


# # Aug month Sales 2016

# In[163]:


aug_sales_2016 = ab.loc[(ab['Year']==2016) & (ab['Month']=="Aug"),['Year','Month','Revenue','Country']]
print(aug_sales_2016)


# # 2016 Monthly sales  till July

# In[164]:


plt.figure(figsize=(10,5))
xaxis = ['Jan','Feb','Mar','Apr','May','June','Jul','Aug','Sept','Oct','Nov','Dec']
yaxis = [1720072.0,1734376.0,1884978.0,1916347.0,2305191.0,2344229.0,491612.0,0,0,0,0,0]
plt.title('2016 Monthly Sales till JULY ')
plt.barh(xaxis,yaxis)
plt.show()


# # Gender Wise sales Report 

# In[165]:


# Gender Male Total sales 2015


# In[166]:


Gender_M_Sales_revenue = ab.loc[(ab['Year']==2015) & (ab['Customer Gender']=="M"),['Year','Customer Gender','Country','Revenue']]
print(Gender_M_Sales_revenue)


# In[167]:


# Total sales by Male customer in 2015


# In[168]:


Gender_M_Sales_revenue['Revenue'].sum()


# In[169]:


# Total no of Male Customers in 2015


# In[170]:


Gender_M_Sales_revenue['Customer Gender'].count()


# In[ ]:


# Gender Female Total sales in 2015


# In[171]:


Gender_F_Sales_revenue = ab.loc[(ab['Year']==2015) & (ab['Customer Gender']=="F"),['Year','Customer Gender','Country','Revenue']]
print(Gender_F_Sales_revenue)


# In[172]:


# Total sales by Gender F in 2015


# In[173]:


Gender_F_Sales_revenue['Revenue'].sum()


# In[ ]:


# Total no. of  Female customers in 2015


# In[174]:


Gender_F_Sales_revenue['Customer Gender'].count()


# In[ ]:


# Total sales by Gender M in 2016


# In[175]:


Gender_M_Sales_revenue_2016 = ab.loc[(ab['Year']==2016) & (ab['Customer Gender']=="M"),['Year','Customer Gender','Country','Revenue']]
print(Gender_M_Sales_revenue_2016)


# In[ ]:


# Total sales by Male Customers in 2016


# In[176]:


Gender_M_Sales_revenue_2016['Revenue'].sum()


# In[ ]:


# Total no of Male Customers in 2016


# In[177]:


Gender_M_Sales_revenue_2016['Customer Gender'].count()


# In[ ]:


# Gender Female Total sales in 2016


# In[178]:


Gender_F_Sales_revenue_2016 = ab.loc[(ab['Year']==2016) & (ab['Customer Gender']=="F"),['Year','Customer Gender','Country','Revenue']]
print(Gender_F_Sales_revenue_2016)


# In[ ]:


# Total sales by Female Customers in 2016


# In[179]:


Gender_F_Sales_revenue_2016['Revenue'].sum()


# In[ ]:


# Total no of Female Customers in 2016


# In[180]:


Gender_F_Sales_revenue_2016['Customer Gender'].count()


# In[181]:


#Creating a dataframe for Graph representation
import pandas as pd
import seaborn as sb


# In[182]:


Sales = {'Year':['2015','2015','2016','2016'],
        'Gender': ['Male','Female','Male','Female'],
        'Sales':[4896235, 5051536, 6515707, 5881098]}
G_Sales = pd.DataFrame(Sales)


# # Show Sales report by Gender 2015 & 2016

# In[183]:


sb.barplot(data=G_Sales,x='Gender',y='Sales',hue='Year')

plt.xlabel('Gender')
plt.ylabel('Sales Revenue')
plt.title('Sales Report by Geder 2015 vs 2016')
plt.show()


# In[ ]:


# Country wise sales 2015 vs 2016


# In[184]:


sales_by_france = ab.loc[(ab['Year']==2015) & (ab['Country']=='France'),['Year','Country','State','Revenue']]
print(sales_by_france)


# In[185]:


sales_by_france['Revenue'].sum()


# In[186]:


sales_by_germany = ab.loc[(ab['Year']==2015) & (ab['Country']=='Germany'),['Year','Country','State','Revenue']]
print(sales_by_germany)


# In[187]:


sales_by_germany['Revenue'].sum()


# In[256]:


sb.relplot(x='State',y='Revenue',data=sales_by_germany,kind='line')
plt.show()


# In[188]:


sales_by_uk = ab.loc[(ab['Year']==2015) & (ab['Country']=='United Kingdom'),['Year','Country','State','Revenue']]
print(sales_by_uk)


# In[189]:


sales_by_uk['Revenue'].sum()


# In[190]:


sales_by_us = ab.loc[(ab['Year']==2015) & (ab['Country']=='United States'),['Year','Country','State','Revenue']]
print(sales_by_us)


# In[191]:


sales_by_us['Revenue'].sum()


# In[ ]:


sb.swarmplot(x='State',y='Revenue',data=sales_by_us)
plt.show()


# In[251]:


# 2015 countries sales = Fr = 1544573.0 || Gr = 1773323.0 || UK = 1894467.0 || US = 4735408.0


# In[192]:


sales_by_france_16 = ab.loc[(ab['Year']==2016) & (ab['Country']=='France'),['Year','Country','State','Revenue']]
print(sales_by_france_16)


# In[193]:


sales_by_france_16['Revenue'].sum()


# In[263]:


sales_by_germany_16 = ab.loc[(ab['Year']==2016) & (ab['Country']=='Germany'),['Year','Country','State','Revenue']]
print(sales_by_germany_16)


# In[195]:


sales_by_germany_16['Revenue'].sum()


# In[196]:


sales_by_uk_16 = ab.loc[(ab['Year']==2016) & (ab['Country']=='United Kingdom'),['Year','Country','State','Revenue']]
print(sales_by_uk_16)


# In[197]:


sales_by_uk_16['Revenue'].sum()


# In[198]:


sales_by_us_16 = ab.loc[(ab['Year']==2016) & (ab['Country']=='United States'),['Year','Country','State','Revenue']]
print(sales_by_us_16)


# In[199]:


sales_by_us_16['Revenue'].sum()


# # Country wise Sales Report 2015 vs 2016

# In[200]:


Country2015 = ['France','Germany','United Kingdom','US']
Sales2015 = [1544573.0,1773323.0,1894467.0,4735408.0]

Country2016 = ['France','Germany','United Kingdom','US']
Sales2016 = [1901531.0,2471187.0,2381753.0,5642334.0]

fig, (ax1,ax2) = plt.subplots(1,2)

ax1.pie(Sales2015,labels=Country2015,autopct="%1.0f%%",shadow=True,explode=[0,0,0,0.1])
ax1.set_title('Countries Sales for 2015')

ax2.pie(Sales2016,labels=Country2016,autopct="%1.0f%%",shadow=True,explode=[0,0,0,0.1])
ax2.set_title('Countries Sales for 2016 till "JULY"')

plt.subplots_adjust(wspace=1.0)

plt.show()


# In[ ]:


# Country wise + Gender wise sales 2015 vs 2016


# In[201]:


CG_fr_2015 = ab.loc[(ab['Year']==2015) & (ab['Country']=="France") & (ab['Customer Gender']=="M"),['Year','Country','Customer Gender','Revenue']]
print(CG_fr_2015)


# In[202]:


CG_fr_2015['Revenue'].sum()


# In[205]:


CG_fr_2015_F = ab.loc[(ab['Year']==2015) & (ab['Country']=='France') & (ab['Customer Gender']=="F"),['Year','Country','Customer Gender','Revenue']]
print(CG_fr_2015_F)


# In[206]:


CG_fr_2015_F['Revenue'].sum()


# # Sales report by Gender from France sector

# In[207]:


Gender = ['Male','Female']
Revenue = [824730.0,719843.0]
plt.pie(Revenue,labels=Gender,autopct="%1.0f%%",shadow=True,explode=[0.1,0])
plt.title('Sales report by Gender "France" 2015')
plt.show()


# In[ ]:


# Show USA Gender Ratio of cxs


# In[208]:


CG_us_2015 = ab.loc[(ab['Year']==2015) & (ab['Country']=="United States") & (ab['Customer Gender']=="M"),['Year','Country','Customer Gender','Revenue']]
print(CG_us_2015)


# In[209]:


CG_us_2015['Revenue'].sum()


# In[210]:


CG_us_2015_f = ab.loc[(ab['Year']==2015) & (ab['Country']=="United States") & (ab['Customer Gender']=="F"),['Year','Country','Customer Gender','Revenue']]
print(CG_us_2015_f)


# In[211]:


CG_us_2015_f['Revenue'].sum()


# # Sales report by Gender from USA sector

# In[212]:


Gender = ['Male','Female']
Revenue = [2290942.0,2444466.0]
plt.pie(Revenue,labels=Gender,autopct="%1.0f%%",shadow=True,explode=[0,0.1])
plt.title('Sales report by Gender "USA" 2015')
plt.show()


# In[213]:


prdt_sales_us_2015 = ab[(ab['Year']==2015) & (ab['Country']=="United States")].groupby('Sub Category')['Revenue'].sum()
print(prdt_sales_us_2015)


# # show the USA reveue by sub category & find the highest revenue collecter product

# In[252]:


Sales = [40372.0,137966.0,44308.0,22042.0,523236.0,96544.0,394577.0,1276071.0,783915.0,247293.0,15574.0,642074.0,416035.0,95401.0]
Sub_Category = ['Bike Stands','Bottles and Cages','Caps','Cleaners','Helmets','Hydration Packs','Jerseys','Mountain Bikes','Road Bikes','Shorts','Socks','Tires and Tubes','Touring Bikes','Vests']
plt.pie(Sales,labels=Sub_Category,autopct="%1.0f%%",shadow=True,)
plt.title('Sub Category wise Revenue "Country = USA" 2015')
plt.show()


# In[218]:


ab.head(2)


# # show the Gender wise sub Category sales

# In[251]:


plt.figure(figsize = (10,6))

sb.countplot(data = ab, x = "Sub Category",hue = "Customer Gender",palette = "pastel")
plt.xticks(rotation = 90)

plt.show()


# # Show the country wise sub-category sales

# In[226]:


plt.figure(figsize = (10,5))

plt.subplot(2,1,1)
sb.countplot(data = ab,x= "Sub Category",hue = "Country",palette = "pastel")
plt.xticks(rotation = 90)

plt.show()


# # Pair plot

# In[249]:


sb.pairplot(ab)
plt.show()


# In[284]:


corr=ab.corr()
plt.figure(figsize=(8,6),dpi=80)
sb.heatmap(corr)
plt.show()


# In[ ]:




