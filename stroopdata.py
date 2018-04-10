
# coding: utf-8

# __Question 1. What is our independent variable? What is our dependent variable?
# <br>Answer:-__  
# > Independent Variable : Incongruent or Congruent word condition.<br>
# Dependent Variable : Response time to name the ink colours.

# __Question 2. What is an appropriate set of hypotheses for this task? What kind of statistical test do you expect to perform? Justify your choices <br>
# Answer:-__ 
# >In psychology, the Stroop effect is a demonstration of interference in the reaction time of a task. When the name of a colour is printed in a colour that is not denoted by the name (Incongruent word condition), naming the colour of the word takes longer and is more prone to errors than when the color of the ink matches the name of the colour (Congruent word condition) therefore our,<br>
#     __• H0 (Null Hypothesis)__ : The Incongruent word condition will either have no significant difference or decrease in the response time to recognize the colour.<br>
#     __• HA (Alternative Hypothesis)__ : The Incongruent word condition will increase the the response time to recognize the colour.<br>
# As we have mentioned here,<br>
# our  Null Hypothesis would be    __H0 : μi ≤ μc__ <br>
# and  Alternative Hypothesis       __HA  : μi > μc__ <br>
#     whereas  “ μi ” is the population mean of time taken for the Incongruent words condition and  “μc” is the  population mean of time taken for the Congruent words condition.  <br>                                                    As we do not know about the population parameters and each participant of our sample set measured response time twice under the different (Congruent and  Incongruent) conditions .Hence we will use the depedent t-test for paired samples and considering our hypotheses our t-test will be __one-tailed t-test__  that the mean of participant’s Incongruent words condition sample will be significantly greater than it’s Congruent words condition mean .
# <br>
# <br>
# 

# __Question 3. Report some descriptive statistics regarding this dataset. Include at least one measure of central tendency and at least one measure of variability.<br>
# Answer:-__         
# >_Measure of Central Tendency_<br>
# __Mean : __ we calculate the sample mean for both our conditions (Congruent & Incongruent) and having dependent samples we will also calculate it for their absolute difference with the formula “ x̄ = ( Σ xi ) / n “ the values be as follows:<br>
# - Mean of Congruent = 14.05<br>
# - Mean of Incongruent = 22.02<br>
# - Mean of Differences(point estimate for μi-μc) = 7.96<br>
# 

# In[8]:


cong,inco = stroop('./stroopdata.csv')


# > but as you go through the these histograms of our both the conditions data seems slightly positively skewed, thus the __Median__ we will be the better measure of central tendency and the calculations are given below : <br>
# - Median of Congruent = 14.36 <br>
# - Median of Incongruent = 21.02 <br>
# - Median of  Differences = 7.66 <br>

# > _Measure of Variability_<br>
# __Sample Standard Deviation :__and now we will calculate the sample standard deviation for both our conditions (Congruent & Incongruent) and having dependent samples we will also calculate it for their absolute difference with the formula “S= √[ ∑((x - x̄)^2)/ (N-1) ] “ and the results are as follows :<br>
# - Sample Standard Deviation of Congruent = 3.56<br>
# - Sample Standard Deviation of Incongruent = 4.80<br>
# - Sample Standard Deviation of Differences = 4.86<br>
# and by considering our these Sample Standard Deviations our __Variance__ will be as follows:<br>
# - Variance of Congruent = 12.67<br>
# - Variance of Incongruent = 23.01<br>
# - Variance of Differences = 23.66<br>
# And we also calculated the __Standard Error__ by dividing the Sample Standard Deviation by the Square root of our sample size and values are as follows :<br>
# - Standard Error of  Congruent =  0.73<br>
# - Standard Error of  Incongruent = 0.98<br>
# - Standard Error of Differences = 0.99<br>
# these all calculations are done in Google Spreadsheet and the link to the spreadsheet is given below:<br>
# __[Google Spreadsheet](https://docs.google.com/spreadsheets/d/1HWKRlJVVdR13A_wA-SC2qLv-5U9LUMCqSdd2AZDy3o0/edit#gid=1299780014)__<br>
# and also calculations are verified and recalculated by using python library modules as follows :

# In[9]:


import csv # read and write csv files
import pandas as se # load library
get_ipython().run_line_magic('matplotlib', 'inline')


# In[10]:


stref = se.read_csv("stroopdata.csv")


# In[11]:


round((stref['Congruent']).mean(),2)


# In[12]:


round((stref['Incongruent']).mean(),2)


# In[13]:


round((stref['Congruent']).median(),2)


# In[14]:


round((stref['Incongruent']).median(),2)


# In[15]:


round((stref['Congruent']).std(),2)


# In[16]:


round((stref['Incongruent']).std(),2)


# In[17]:


stref.describe()


# __Question 4. Provide one or two visualizations that show the distribution of the sample data. Write one or two sentences noting what you observe about the plot or plots.<br>
# Answer: __

# In[18]:


import matplotlib.pyplot as plt # load library


# In[19]:


def stroop(datafile) :
    
    """
    This function reads the stroopdata file which is having the data about response time taken to name the 
    ink colours by each participant in both of the Congruent and Incongruent words conditions and and 
    creates a histogram respectively.
    """
    
    with open(datafile,'r') as f_in:
        csv_reader = csv.DictReader(f_in)
        cong = []
        inco = []
        
        for row in csv_reader :
            cong.append(float(row['Congruent']))
            inco.append(float(row['Incongruent']))
    cong.sort()
    inco.sort()
    
    plt.hist(cong,bins=range(int(min(cong)), int(max(cong))+1,1),label='Congruent condition')
    plt.title('Stroop effect')
    plt.xlabel('response_time')
    plt.legend(loc='upper right')
    plt.show()
    
    plt.hist(inco,bins=range(int(min(inco)), int(max(inco))+1,1),label='Incongruent condition')
    plt.title('Stroop effect')
    plt.xlabel('response_time')
    plt.legend(loc='upper right')
    plt.show()
    return (cong,inco)


# In[20]:


cong,inco = stroop('./stroopdata.csv')


# As you notice these histograms they seems bit of positively skewed distributions, which is pulling the mean to positive side but as you look upon our Mean values they are much closer to the peak which would indicate to the Normal Distribution.  

# In[26]:


stref.index


# In[27]:


stref['Participant']=stref.index+1


# In[28]:


import numpy as np
def scatterp(i,j):
    """
    This function reads the stroopdata file as per the arguments are passed which
    are the partipant and the respective words condition and creates a scatter plot according 
    to given arguments.
    """
    x,y = stref[i],stref[j]
    colors = 'green'
    area = np.pi*15
    #colors = np.random.rand(N)
    ##area = np.pi * (15 * np.random.rand(N))**2
    fig = plt.figure()

    condition = 'Response Time ('+j+')'
    plt.xticks(np.arange(min(x), max(x)+1, 1))
    plt.yticks(np.arange(0, 35, 2))
    plt.scatter(x, y,s=area,c=colors, alpha=0.5)
    plt.title('Stroop effect')
    plt.xlabel(i)
    plt.ylabel(condition)
    plt.ylim([0,max(y)+1])
    plt.xlim([0,max(x)+1])
    plt.show()


# In[29]:


scatterp('Participant','Congruent')
scatterp('Participant','Incongruent')


# As you look through these scatterplots, In Congruent word condition's scatterplot the distribution is about between 8 to 22 and in the second Incongruent word condition's scatterplot has most of the distribution between like 15 to 26 and has two outliers around 35 that would possibly skew our distribution's mean value in order to make it less representative of our data.thus we can clearly see that the mean of the Participant's Response time to recognize the colour in Incongruent word condition is much greater than the Congruent word condition one.
# <br>
# <br>

# __Question 5. Now, perform the statistical test and report your results. What is your confidence level and your critical statistic value? Do you reject the null hypothesis or fail to reject it? Come to a conclusion in terms of the experiment task. Did the results match up with your expectations?<br>Answer:__ We have done all the related calculations in the spreadsheet and link to the spreadsheet is here :
#  > __[Google Spreadsheet](https://docs.google.com/spreadsheets/d/1HWKRlJVVdR13A_wA-SC2qLv-5U9LUMCqSdd2AZDy3o0/edit#gid=1299780014)__<br>
# We first calculated the Mean of the Differences of sample set which is basically the __Point Estimate for μi-μc__ which turns out to be = 7.964 whereas sample size is 24,<br>
# __Sample Standard Deviation of Differences__ = 4.865<br>
# __Standard Error of the Differences__=0.9930286348<br>
# __t-statistic__ is calculated by Mean of Differences minus the expected difference which is zero and dividing it by the Standard Error of the Differences which is equal to =  8.0207 whereas our<br>
# __t-critical__ value is 1.714 for one tailed t-test at _α-level= 0.05_ and for our _degrees of freedom = 23_.<br>
# As we can see here our t-statistic is much greater than our t-critical value in one tailed test at α=0.05 thus it is falling in the __critical region__ and the p-value is very much less than p-value of 0.05 hence we will <br>__Reject the Null Hypothesis (Ho)__ this means the Participants took  significantly more amount of time to Response in the Incongruent words condition compared to the Congruent words Condition.<br>Since it was an experimental design we can make a causal statement like different word conditions have the causal effect on the  participant's responce time to recognise the colour.<br>
# And Yes, the results are pretty much matched up with my expectations.
# <br>
# <br>

# __Question 6. Optional: What do you think is responsible for the effects observed? Can you think of an alternative or similar task that would result in a similar effect? Some research about the problem will be helpful for thinking about these two questions!<br>
# Answer:-__ 
# >We Humans as habitual readers,we perform reading effortlessly whereas declaration of a colour requires more cognitive effort,and When there is a conflict between these two information(word & colour) our cognitive load is increased and our brain needs to concentrate on these differences which will eventually slow down our response time to recognise the colour.<br>
# kind of task that would result in similar effect is like if we write a name of perticular animal in a bit larger font and in one condition(Congruent) we will put pictures of that animal on the word font that describes animal and in another condition(Incongruent) we will put a different animal's pictures on that word which is referring to another animal regardless of pictures having on the word itself.<br>
# and here also my expectation is Incongruent condition will take more time to response to recognize the correct animal picture than the Congrgruent condition.
