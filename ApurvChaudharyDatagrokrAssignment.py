
# coding: utf-8

# Assignment Completed: 1st- Showing Stock prices of Companies from 1st Jan 2017 to 31st Dec 2017 on graph 2nd- Calculating which one was the most volatile in year 2017 and plotted the bar chart of volatality %age 3rd- Calculation of corelative coefficient for finding corelativity and plotted scattering data of both company's closing price Thankyou So much for this challenging oppurtunity i really enjoyed it to the core As a beginner to python and on self learning skills i have completed these tasks Apurv Chaudhary (Master of Computer Application 2016-18) +91-8553743806 +91-7087399763

# In[6]:


from iexfinance import get_historical_data #importing iexfinance library of iex for extracting stock data
import seaborn as sns                      #importing seaborn library for statistical data visualization
from datetime import datetime              #importing datetime for for dealing with date & time 
import matplotlib.pyplot as plt            #importing matplotlib.pyplot for ploting data into graphs
import numpy as np                         #importing numpy library for working on an array datastructure
start = datetime(2017, 1, 1)    #assigned date from datetime library to start variable and likewise for end
end = datetime(2017, 12, 31)


# In[2]:


def dataframe(company,title):       #defining a function with parameter company(for company value to get data) & title(for mentioning on title) 
    start = datetime(2017, 1, 1)    #assigned date from datetime library to start variable and likewise for end
    end = datetime(2017, 12, 31)
    df =get_historical_data(company, start, end, output_format='pandas') #getting data from iexfinance library to df
    c=df['open']  #assigning opening stocks prices to varibale c  likewise for b,d,a                               
    b=df['high']  
    d=df['low']
    a=df['close']
    sns.set()      #showing graph of values passed from the func dataframe from seaborn (hereafter we will be using many func from seaborn library)
    sns.set_style("darkgrid") 
    sns.set(rc={'figure.figsize':(14.7,8.27)}) #setting size of graph
    ax=plt.subplot(111)  #plotting subplot for mentioning legends
    c.plot(label='Opening Price',color='blue') #plotting graph from matplotlib library likewise b,d,a
    b.plot(label='Highest Price',color='g')    
    d.plot(label='Lowest Price',color='r')
    a.plot(label='Closing Price',color='c')
    plt.title('Stock Prices of :'+ title)   #plotting title name and value(argument) is getting from title parameter what we defined in func
    plt.xlabel('Date:1-1-2017 To 31-12-2017') #setting labels x and y names
    plt.ylabel('Price in USD(US Dollars)')
    ax.legend()                             #calling legend to mention in graph
    plt.show()                              #showing plotted graph


# In[3]:


dataframe('AAPL','APPLE')    #calling func and passed argument eg'AAPL' for company parameter and 'APPLE' for title parameter 
dataframe('GOOG','GOOGLE')   #likewise for other companies
dataframe('FB','FACEBOOK')
dataframe('NFLX','NETFLIX')
dataframe('AMZN','AMAZON')

#These Graphs are for each company mentioned in assignment: Apple, Google, Facebook, Netflix, Amazon
#each graph showing stocks(opening, closing, highest, lowest) of Dates from 1st Jan 2017 to 31st Dec 2017


# These set of codes i wrote for calculating volatality %age for each company and plotted a bar chart for values accordingly. I was totally new to these terms volatile, corelation etc. So i have searched on internet formulaes for these calculation. And then i designed programmes for these calculations according to formulae. In case any wrong method i have used kindly ignore if possible. Formula for Volatality i used: daily change %age = ((high_prices-low_prices)/low_prices)100 then created list of all %age mean%age= listsum/lengthoflist volatile%age=meansqrt(no.of days) i found no. of days in year for stocks is 252 but i used the length of my data

# In[8]:


def volatile(high1,low1): #defined func for calculating volatality % by passing parameter high1=high price low1=low price
  lst=[]
  for i in range(len(high1)):
     per=((high1[i]-low1[i])/low[i])*100
     per=round(per,2)
     lst.append(per)
  m=sum(lst)/len(lst)
  vol=m*(len(high1)**(1/2))
  return (round(vol,2))           #will return integeral value wherever called for perticular passed argument
df =get_historical_data('AAPL', start, end, output_format='pandas')
high=df['high']
low=df['low']
apple=volatile(high,low) #called func volatile and assigned to apple variable just for remembring purpose i used cmpny names
df =get_historical_data('GOOG', start, end, output_format='pandas') #extracting stock data of google and assigned to df
high=df['high']      #setting high prices of df to variable high likewise for low 
low=df['low']
google=volatile(high,low)
df =get_historical_data('FB', start, end, output_format='pandas')
high=df['high']
low=df['low']
facebook=volatile(high,low)
df =get_historical_data('NFLX', start, end, output_format='pandas')
high=df['high']
low=df['low']
netflix=volatile(high,low)
df =get_historical_data('AMZN', start, end, output_format='pandas')
high=df['high']
low=df['low']
amazon=volatile(high,low)
label=['Apple', 'Google', 'Facebook', 'Netflix', 'Amazon']  #just a list of company names with string type
dataframe=[apple, google, facebook, netflix, amazon]        #dataframe variable will be having list of all returned funcs values 
print("These are the respective Stock Volatality %age for Companies in Year 2017 :"+str(dataframe)) #just for printing %age
def plot_bar_x():                                           #defined func for ploting bar chart of volatality
    index= np.arange(len(label))#from numpy library intialized an array of size(equal to length of labels-i.e.5(0-4) in our case)
    plt.bar(index, dataframe)   #plotting bar of values indexes on x-axis to dataframe values y-axis becomes the % from dataframe
    plt.xlabel('Companies', fontsize=12)                   #setting xlabels name and fontsize
    plt.ylabel('Percentage % of Volatality', fontsize=12)  #setting ylabel name and fontsize
    plt.xticks(index, label, fontsize=12, rotation=20)     #setting xticks with perticular values
    plt.title('Volatality of Stocks of mentioned companies in year 2017')              #setting title
    plt.text(0,30,r'Netflix has most volatile Stock in 2017 i.e:34.39%', fontsize=15)  #setting text on x,y location on chart
    plt.show()                                                                         #calling show for display
plot_bar_x()                                                                           #calling func for bar

#Final Impression::Out of all companies Netflix has most volatile Stock in 2017 i.e:34.39%


# In this cell i have calculated the corelation coefficient and scatter plot of closing price of both companies data formula for corelation coefficient i referred from wikihow in which i have implemented all calculations here is the url url for formulation: https://www.wikihow.com/Find-the-Correlation-Coefficient then i plotted the scattering Stocks data of two companies as it is going positively corelated

# In[9]:


df =get_historical_data('GOOG', start, end, output_format='pandas')  #retrived data from iex library assigned to df variable
gcls=df['close']                                                     #closing price of stocks setted to variables
datax=df['close']
df =get_historical_data('AMZN', start, end, output_format='pandas')
acls=df['close']
datay=df['close']
def coefficient(argx,argy):                                         #defined func for finding coefficient
  mux=sum(argx)/len(argx)                                           #finding mean of x and y
  muy=sum(argy)/len(argy)
  lstx=[]                                              
  lsty=[]
  for valuex in argx:
    xm=((valuex-mux)**2)
    lstx.append(xm)
  for valuey in argy:
    ym=((valuey-muy)**2)
    lsty.append(ym)
  sx=(sum(lstx)/(len(argx)-1))**(1/2)                              #sigmax for standard daviation in x
  sy=(sum(lsty)/(len(argy)-1))**(1/2)                              #sigmay for standard daviation in y
  lstx1=[]
  lsty1=[]
  for valuex in argx:
    cx=(valuex-mux)/sx
    lstx1.append(cx)
  for valuey in argy:
    cy=(valuey-muy)/sy
    lsty1.append(cy)
  x=np.array(lstx1)       #created array because multiplication in list is not allowed and very easy in array
  y=np.array(lsty1)    
  mul=np.multiply(x,y)    #multiplied both array 
  apurv=list(mul)         #explicitly changed to list for doing roundof values to two decimal point
  return round((sum(apurv)/len(apurv)),2)   #done rounding off and retuned value where func called
if coefficient(gcls,acls)>0.5:
    print("Corelation coefficient for Stocks of Google and Amazon is: "+str(coefficient(gcls,acls))+" and i.e Strongly Corelated")
elif coefficient(gcls,acls)>0:
    print("Positively Corelated")    #i studied and searched for corelation:
elif coefficient(gcls,acls)==0:      #corelation coefficient lies b/w ((-1)-0-(1))
    print("Equals to Zero")          #>0 is positively corelated and near +1 is strongly corelated
elif coefficient(gcls,acls)<-0.5:    #<0 is negatively corelated and near -1 is strongly uncorelated
    print("Strongly Uncorelated")    #in this case(Google & Amazon) we have gotten 0.95 i.e strongly corelated data
elif coefficient(gcls,acls)<0:       #these if-elif i just used to print corealtive coefficient & strings for claryfying purpose
    print("Negatively Corelated")


# In[10]:


plt.scatter(datax, datay)       #scatter plotting of data in datax and datay
plt.title('Scatter plot of Corelation between Google & Amazon') #setting title
plt.xlabel('Google') #setting lables x & y
plt.ylabel('Amazon')
plt.text(800,1100,r'Stocks of Google and Amazon has corelation coefficient 0.95 hence strongly Corelated',fontsize=11)
plt.show() #shows the scatter plotting of closing prices of Google & Amazon
#with this formula we can find any corelation bw two set of data just by passing values of both

#Final impression::Corelation Coefficient of Stocks of Google and Amazon is 0.95 and this means both data is strongly corelated

