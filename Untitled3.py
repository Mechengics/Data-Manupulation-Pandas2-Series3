#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Essential functionality


# In[2]:


import pandas as pd
import numpy as np


# In[3]:


#this section will walk you through the fundamental mechanics of handling with data.


# In[4]:


#Reindexing.


# In[5]:


obj1=pd.Series([4,5,6,7],index=["a","b","c","d"])
obj1


# In[6]:


obj1.reindex(["a","b","c","d","e"])


# In[7]:


#learn the concept of forward filling the data.
#using ffil will do it.
obj2=pd.Series(["dog","cat","baboon"],index=[0,2,4])
obj2


# In[12]:


obj3=obj2.reindex(np.arange(6),method="ffill")


# In[13]:


obj3


# In[14]:


obj2


# In[15]:


#Lets deal with dataframe:
#reindex can alter the row index, columns or both. When only sequence is passed it reindexes the rows


# In[25]:


frame1=pd.DataFrame(np.arange(9).reshape(3,3),
                   index=["a","b","c"],
                   columns=["max","july","hari"])
frame1


# In[19]:


#reindixing this data frame: 
frame1.reindex(["a","b","c","d","e"])


# In[21]:


#Now i want to deal with columns. 
names=["max","july","hari","tommy","Arthur"]
frame1.reindex(columns=names)


# In[31]:


#Another way to do this is defining the axis
frame2=frame1.reindex(names, axis="columns")
frame2


# In[ ]:


#lEARN ABOUT MORE REINDEX FUNCTION ARGUMENTS 
#backfill, and forward fill are two important ways of filling an empty index.
#limit: when forward filling or backfiling the maximuz size gap.
#tolerance: 
#level: 
#copy:true always copy the statement and false than don't copy the statement


# In[30]:


#Rendixng using loc operator. 
#This method of using loc operator reindexes the column and rows on the basis of comma and many prefer to do this way
#but the issue is that it cannot update new columns or index in the data frame. 
frame2.loc[["a","b","c"],["max","july","tommy","hari","Arthur"]]


# In[32]:


#Dropping entries from Series
obj3=pd.Series(np.arange(5), index=["a","b","c","d","e"])
obj3


# In[35]:


new_obj=obj3.drop("c")
new_obj


# In[37]:


#want to drop multiple rows from the given series you can do
obj3.drop(["d","c"])


# In[42]:


#Using Drop in the data frame:
#first of all lets create a  data frame
frame3=pd.DataFrame(np.arange(16).reshape((4,4)),
                   index=["a","b","c","d"],
                   columns=["one","two","three","four"])
frame3


# In[43]:


frame3.drop(index=["a","b"])#drop two index from the data frame.


# In[44]:


frame3.drop(columns=["two"])#drop columns from the data frame.


# In[45]:


#remember while learning numpys we had said that axis=1 means column\
frame3.drop("three", axis=1) #also say axis=columns.


# In[48]:


#Indexing selection and filtering. 
#In order to solve this let's create a series first. 
obj4=pd.Series(np.arange(5),index=["a","b","c","d","e"])
obj4


# In[49]:


#This is similar to numpy indexing but the primary difference is thatin numpy arrays the index is not presented but here in pandas the index is also presented.
#want to approach a certain index 
obj4["c"]


# In[50]:


#want to approach the first element
obj4[0]


# In[51]:


#want to slice the series
obj4[1:4]


# In[52]:


#want values of multiple index in a certain order.
obj4[["a","c","d"]]


# In[53]:


#want values on specific condtion.
obj3[obj3<2]


# In[54]:


#you can acess the elements with the help of index using loc operator.
obj3.loc[["a","b","c"]]


# In[ ]:


#Remember loc operator is more preffered than other methods because in loc method what is inside the bracket i specifically index while just calling out numbers may give us order of elements.
#want to slice using loc operator use this
obj3.loc[b:c]#this kind of slicing is little bit better than other types of slicing because in this the result includes b.......... to c that means b c and the interval between them.


# In[56]:


#want to change values using loc with the help of slicing you can try
obj3.loc["b":"d"]=5
obj3


# In[57]:


#want to extract a data from the data frame we can proceed as follows
#first of all lets create a data frame.
frame4=pd.DataFrame(np.arange(16).reshape((4,4)),
                   index=["a","b","c","d"],
                   columns=["one","two","three", "four"])
frame4


# In[58]:


#want to extract columns from this given data frame try:
frame4["one"]


# In[3]:


#select multiple?
frame4[["one","two","three"]]


# In[4]:


import pandas as pd
import numpy as np
frame4=pd.DataFrame(np.arange(16).reshape((4,4)),
                   index=["a","b","c","d"],
                   columns=["one","two","three", "four"])
#want to select rows you can do this by slicing, by the way you select the columns you canntot select the 
frame4[2:]


# In[6]:


#you can also select a specific rows by giving a condition but this method is little odd
#lets first create a frame4
frame4


# In[9]:


#lets keep a condition where column three is assigned to output results that is greater than 5
frame4[frame4["three"]>5]


# In[10]:


#want to check values in the form of boolean expression for this you need to proceed as:
frame4<5


# In[12]:


#Want to replace values use this
frame4[frame4<5]=0
frame4


# In[14]:


#Want to select the elements in the data frame using loc and iloc.
frame4.loc["b"]#rows can be selected by this method but remember that columns cannot be selected


# In[15]:


#the answer is the series, having labels as the name of the columns


# In[16]:


#Want to select specific columns and specific rows. 
frame4.loc["a",["one","two"]]


# In[23]:


#want to get the rows usng the integer index method.
frame4.iloc[1]


# In[24]:


#want to get multiple rows using i loc
frame4.iloc[[1,2,3]]


# In[26]:


#want to get columns and rows using iloc
frame4.iloc[[1,2,3],2]


# In[27]:


#want to get multiple columns and multiple rows using iloc
frame4.iloc[[1,2,3],[2,3]]


# In[30]:


#this is really beautiful and helps us to simplify literally everything that is present in the given box.
#the data frame can be sliced using the same method that we used to slice the index
#this process of slidin is unconventional from the general method of sliding. 
frame4.loc[:"c",["three","four"]]


# In[31]:


frame4.iloc[:,:3]


# In[33]:


#you can also specify the condition as 
frame4.iloc[:,:3][frame4.three<5]


# In[ ]:


#here you can see that although we have kept all the rows in the initial slicing the last condition has overtaken the other conditions.


# In[44]:


#try a boolean array in iloc
frame4.iloc[frame4.two<=5]
#boolean expression cannot be used in this scenario. 


# In[49]:


frame4.loc[frame4.one>=4]


# In[51]:


#want to select a single integer value from a dataframe. Specify it like a matrix row and column and thus make it
frame4.at["c","one"]


# In[4]:


#If you have already learnt basics of python like lists and functions we can deal with assigning the values .
import pandas as pd
import numpy as np
sertest=pd.Series(np.arange(3))
#generally if we have to use the condition that is like
sertest[-1]#it is ok in list but in series of pandas it generates error


# In[5]:


#but lets create a series having index as alphabets than this method is completly right
#for example 
seriestest2=pd.Series(np.arange(3),index=["a","b","c"])
seriestest2[-1]


# In[7]:


sertest.iloc[-1]#you can use iloc to get the result. 


# In[8]:


#you can also slice the data, as follows. 
sertest[:2]


# In[21]:


#Construct a frame.
frame4=pd.DataFrame(np.arange(16).reshape((4,4)),
                   index=["a","b","c","d"],
                   columns=["one","two","three", "four"])
frame4.loc[:,"one"]=1
frame4


# In[28]:


frame4.iloc[2]=5
frame4


# In[31]:


frame4.iloc[frame4["four"]>5]=3
frame4


# In[33]:


frame4.loc[frame4.three==5]=6
frame4 #modify the data frame


# In[34]:


#Arithmetic and Data Allignment.


# In[35]:


#Want to add two series. But there is a little catch in this series
s1=pd.Series([1,3,4,5], index=["a","c","d","e"])
s2=pd.Series([1,2,3,5],index=["a","b","c","e"])


# In[36]:


s1+s2


# In[37]:


#See That, those index that are not present in both of them don't induce the result.


# In[43]:


#Want to observe this in case of data frame?
frame5=pd.DataFrame(np.arange(16).reshape(4,4), 
                    index=["a","c","d","f"],
                   columns=["one","two","four","five"])
frame4+frame5


# In[ ]:


#See it treats each column and rows as a seperate index and operates on it. 


# In[ ]:


#Summarization can be done as: If two data frames having no common columns and common rows are added together the resulting data frames contains only nulls. 


# In[48]:


#Arithmetic Methods with fill Values
#Do you Know: There is a sperate method in python that helps you to specify nan values in python
#for this you can work as:
a1=pd.DataFrame(np.arange(12).reshape((3,4)),columns=list("abcd"))
a2=pd.DataFrame(np.arange(20).reshape((4,5)),columns=list("abcde"))


# In[49]:


a1


# In[54]:


a2


# In[55]:


a1.loc[1:3,"b"]=np.nan#to add null fields in the table


# In[56]:


a1


# In[58]:


#now use the fill command to fill the null or empty spaces:
a3=a1+a2


# In[59]:


a3


# In[62]:


a2.add(a1, fill_value=0)


# In[ ]:


#Remember while filling the datas it fills the data in the missing field of the intial matrix and not the final matrix


# In[64]:


#Inverse of the given function and rdiv has same function.
a2.rdiv(1)


# In[70]:


#You can fill up command with reindex
a1.reindex(columns=a2.columns, fill_value=0)


# In[71]:


#for every operation add, mul, div,sub and power there is reverse function which does the opposite task. It brings changes in order which brings change in index values as well as result sometimes 


# In[72]:


#Upto now we have learned about data frame and series. 
#Now is the time to join the operation between these dataframe and series. 


# In[79]:


frame6=pd.DataFrame(np.arange(12).reshape((4,3)),
                   columns=list("end"),
                   index=list("come"))
#i suggest you to look at the advanced numpy course present in wes mickinney book. in there is mentioned how a single line array is subtracted with a multidimensional array in python
series1=frame6.iloc[0]#selects the first row 
#now conduct the operation
#while subtracting the series from the data frame it subtracts every single line from the given dataframe. 


# In[80]:


#first look at the series and data frame
frame6


# In[81]:


series1


# In[82]:


#conduct the operation
frame6-series1


# In[83]:


#You can observe that every line in the data frame is subtracted from the given series
#Since we have taken the series from the same data frame so we don't have the problem of indexing
#Some series may not contain the index that is present in the data frame and sometimes the series may contain index that is not present in the data frame in such a case, null result is given by the python.


# In[90]:


#To see this thing let's reindex the particular series and try to operate with the statements.
series2=series1.reindex(index=["a","b","e","d"])


# In[94]:


#you can see that subtraction is carried out and the elements that are not present in both is actually given a null value. 
#The concept is similar to what we had previously learned. 
#What if we divide.
frame6.div(series1)


# In[96]:


#Each row is divided by coressponding elements of the series. inf means infinite


# In[97]:


#Lets try multiplication
frame6.mul(series1)


# In[98]:


#The same concept applies here


# In[99]:


#Function Application and Mapping


# In[102]:


#Numpy unfuncs method also work while dealing with data frames in pandas
#lets first create a new frame
frame7=pd.DataFrame(np.random.standard_normal((4,3)),
                    columns=list("bce"),
                    index=list("abcd")
                   )
frame7


# In[103]:


#Lets use the absolute function that helps us generate absolute value.
#abs means without negative signs
np.abs(frame7)


# In[104]:


#now we a got a data frame with no negative values in it.


# In[105]:


#Want to create a reusable code <function> to find the difference between minimum and maximum values of a column.
def f1(x):
    return x.max()-x.min()
#we can use apply command to use this function in data frame.
frame7.apply(f1)


# In[110]:


#want to do this on rows?
frame7.apply(f1, axis="columns")#apply across columns will be a helpful synonym here.


# In[113]:


#Want to make the data calculation simple by using the formatted string
def formatdataframe(x):
    return f"{x:.2f}"
frame7.applymap(formatdataframe)#map method is used here because the series has a map method for applying an element wise function


# In[115]:


#this formatting is special type of formatting in python that we use in order to specify the decimals


# In[119]:


#you can chose specific series from a data frame and then map it and use the function
frame7["e"].map(formatdataframe)


# In[120]:


#Sorting and Ranking
sort1=pd.Series(np.arange(4), index=["a","b","d","c"])
sort1.sort_index()


# In[121]:


#in a data frame you can sort using the axis method.
frame8=pd.DataFrame(np.arange(12).reshape((3,4)),
                   index=["four","three","one"],
                   columns=["d","a","c","b"])
frame8


# In[122]:


#want to sort the data frame you can use the command


# In[123]:


frame8.sort_index()


# In[124]:


#when the sorting is not given anything it generally operates in rows


# In[128]:


frame8.sort_index(axis="columns")


# In[129]:


#the data is sorted in ascending order by default but can be also arranged in descending order


# In[130]:


frame8.sort_index(axis="columns",ascending=False)


# In[131]:


#now the data is arranged in ascending order.


# In[132]:


#Sorting the values in the series you can use 
sort2=pd.Series([1,2,5,4,6,9,8])
sort2


# In[133]:


sort2.sort_values()


# In[134]:


#Want to know what happens to the null elements when sorting.
sort3=pd.Series([4,np.nan,7,np.nan,-3,2])
sort3.sort_values()


# In[135]:


#The null values are automatically pushed to the last.


# In[136]:


#If you want to bring the null values at the front you can try using the command
sort3.sort_values(na_position="first")


# In[138]:


#You can also sort th values in the data frames. For doing this lets first create a data frame.
frame9=pd.DataFrame({"b":[1,3,6,2,4,5],"a":[1,2,4,3,5,6]})
frame9


# In[139]:


#want to sort the values using columns you can use the formula
frame9.sort_values("b")


# In[140]:


frame9.sort_values(["a","b"])


# In[141]:


#This sorts the value of both a and b.


# In[142]:


#Want to rank the given elements. I wish i could extract the billion ranks from the previous lessons. But whatever 😂
sort4=pd.Series([7,-3,2,7,-3,1])
sort4.rank()


# In[143]:


#Look how the ranks are assigned for same digits in th series the ranking is done by calucalting the mean.


# In[144]:


#If you want just the rank and not the decimals you can also use the method
sort4.rank(method="first")


# In[146]:


#You can also arrange the ranks on the basis of ascending and descending order
sort4.rank(ascending=False)


# In[147]:


#you can also rank the data frames on the basis of rows and columns.


# In[148]:


frame8.rank(axis="columns")#This means calculate the ranks in the columns.


# In[149]:


#Remember the ranking is done as the highest value is given as lowest rank.


# In[154]:


#f you want to do it in a descending order than you can do as:
frame8.rank(axis="columns",ascending=False) # This looks for arranging the ranks in the columns.


# In[158]:


#If we donot specify the axis it is in rows. The ranking is done by looking at the columns
frame8.rank()
#Compare the results from the previous ones and you will note the difference


# In[159]:


#Axis Indexes with Duplicate Labels
#average: calculates th average of ranks
#min: gives the minimum rank to the function
#max: gives the maximum rank to the function 
#first: Assigns the ranks in the order the values appears in the data
#dense:Like method="min", but ranks always increase by 1 between groups rather than the number of equal elements in a group


# In[160]:


#Axis Indexes with Duplicate Labels:
#To deal with this lets first create a series has copy of indexes.
index1=pd.Series(np.arange(4), index=["a","b","b","c"])
index1


# In[162]:


index1.index.is_unique#to check wether the index is repeated. Answered in boolean expressin


# In[164]:


#when you acces the series with the index names it can give you two labels.
index1["b"]
#you can use iloc to get the required index if you don't want the repeated one.


# In[ ]:


#A data frame can also have multiple indexes.


# In[166]:


frame10 = pd.DataFrame(np.random.standard_normal((5, 3)),
                             index=["a", "a", "b", "b", "c"])
frame10


# In[168]:


#you can use loc to acces the index in data frame
frame10.loc["b"]


# In[169]:


#Summarizing and Computing Descriptive Statistics


# In[170]:


#Want to sum the elements across column in a data frame you can:
frame10.sum()


# In[171]:


#Want to sum the elements across the data frame across the rows
frame10.sum(axis="columns")


# In[ ]:


#If the data frame contains null values than the na value is considered to be 0 while adding.


# In[173]:


#skipna option helps us to determine wether the na values is present in th data frame and it also helps us to print the result as na if there is presence of na in the elements
# frame10.sum(axis="index", skipna=false) if the frame 10 had contained null elements would have given us na elements.
#want to yield mean: 
frame10.mean()
#must have atleast one non NA values in the given series or data frame


# In[174]:


#there is a option called as level that helps to ungroup multiindex we will deal with this in the advanced pandas course.


# In[175]:


#Some methods like idxmax and idxmin are used to get those index which has maximum and minimum values


# In[178]:


frame10.idxmax()


# In[180]:


frame10.idxmin()


# In[181]:


#to calculate the cumulative frequency.
#I think we have discussed about the cumulative in the numpy lesson. 
frame10.cumsum()


# In[182]:


#want many statistical answers at the same time, can apply the describe command. 
frame10.describe()


# In[184]:


# #Here are some of the statistical methods that I have mentioned. You can try this as follows:
# count	Number of non-NA values
# describe	Compute set of summary statistics
# min, max	Compute minimum and maximum values
# argmin, argmax	Compute index locations (integers) at which minimum or maximum value is obtained, respectively; not available on DataFrame objects
# idxmin, idxmax	Compute index labels at which minimum or maximum value is obtained, respectively
# quantile	Compute sample quantile ranging from 0 to 1 (default: 0.5)
# sum	Sum of values
# mean	Mean of values
# median	Arithmetic median (50% quantile) of values
# mad	Mean absolute deviation from mean value
# prod	Product of all values
# var	Sample variance of values
# std	Sample standard deviation of values
# skew	Sample skewness (third moment) of values
# kurt	Sample kurtosis (fourth moment) of values
# cumsum	Cumulative sum of values
# cummin, cummax	Cumulative minimum or maximum of values, respectively
# cumprod	Cumulative product of values
# diff	Compute first arithmetic difference (useful for time series)
# pct_change	Compute percent changes
# #this table is taken from the book data analyst with python by wesmickkiney. 


# In[185]:


#Corelation and Covariance
#Say we want to find a corelation between column a and column b than we can proceed as follows:
#data
# data["a"].corr(data["b"])
#Say we want covariance in the similar way
# data["a"].cov(data["b"])


# In[186]:


#Directly using corr and cov can give us the matrix of correlation and covariance respectively
# data.corr
# data.cov


# In[189]:


#Unique Values, Value Counts, and Membership
#Say we have the repeated series than we can proceed as fllows:
repeatedseries=pd.Series(["c","a","c","a","b"])
uniqueseries=repeatedseries.unique()
uniqueseries


# In[190]:


#you can observe the repeated objects are merged into one from here.


# In[195]:


#value count helps you to count the number of repeated elements in the given Series
repeatedseries.value_counts()
#the answer is automatically in descending order.


# In[196]:


#if you want this in random ways you can try as sort=False, also the value counts is also avilale as a top level pandas method that can be used with Num Py Arrays.
pd.value_counts(repeatedseries.to_numpy(), sort=False)


# In[199]:


#you can use the isin to check the avilability of values.
mask=repeatedseries.isin(["a","c"])
mask


# In[200]:


#The Result gives us the Boolean Expression of the given value.


# In[201]:


repeatedseries[mask]


# In[202]:


#This above expression gives the boolean expression for giving the truth table, to either indicate true and false. 


# In[ ]:


#Some important unique,value counts, and set membership methods are used as follows
#isin: Checks the avilability of the given materials in the list. Answer is in Boolean Expression 
#get_indexer: lets say we have two index that is index1 and index2, and index2 contains the elements of index1 than, if we want to index the values of series index2 with the index of same values of index1 , we use this method.
#unique: Compute an aray of unique values in Series.  
#value_counts: Counts the number of the supplied value in the series.


# In[ ]:


#Finally Guys ⚔️🖤 The journey to our third series ends here. After reading this and previous introductory course to pandas, you will have the solid understanding of the panda library
#Hope seeing you being active in learning about data analysis.
#If you have made this far, guys I want to say you that consistency is the key, keep it up.
#Kudos Fellows
#Love and Peace


# In[ ]:


#Regards
#mechengics
#Ankit Sangroula

