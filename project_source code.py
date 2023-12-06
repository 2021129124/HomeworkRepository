import pandas as pd
file = 'data_final.csv'
df = pd.read_csv(file)
#import pandas package first, and make an object for csv file

column_name = 'top genre' #find the specific column, which is 'top genre'
column_mode = df[column_name].mode()
if not column_mode.empty:
     most_popular_item = column_mode.iloc[0] #find the item that appear most times
     print('The most popular music genre is:',most_popular_item)

def mean_bpm():
     column_name1 = 'bpm'
     bpm_values = pd.to_numeric(df[column_name1], errors='coerce')
     #caculate the column value
     mean_bpm=bpm_values.mean()#find the mean value of 'bpm' factor
     return mean_bpm
result_bpm=mean_bpm()
print('The average value of bpm is:',format(result_bpm,'.2f'))

def mean_nrgy():
     column_name2 = 'nrgy'
     nrgy_values = pd.to_numeric(df[column_name2], errors='coerce')
     mean_nrgy=nrgy_values.mean()#find the mean value of 'nrgr' factor
     return mean_nrgy
result_nrgy=mean_nrgy()
print('The average value of nrgy is:',format(result_nrgy,'.2f'))

def mean_dnce():
     column_name3 = 'dnce'
     dnce_values = pd.to_numeric(df[column_name3], errors='coerce')
     mean_dnce=dnce_values.mean()#find the mean value of 'dnce' factor
     return mean_dnce
result_dnce=mean_dnce()
print('The average value of dnce is:',format(result_dnce,'.2f'))

def mean_dB():
     column_name4 = 'dB'
     dB_values = pd.to_numeric(df[column_name4], errors='coerce')
     mean_dB=dB_values.mean()#find the mean value of 'dB' factor
     return mean_dB
result_dB=mean_dB()
print('The average value of dB is:',format(result_dB,'.2f'))

def mean_live():
     column_name5 = 'live'
     live_values = pd.to_numeric(df[column_name5], errors='coerce')
     mean_live=live_values.mean()#find the mean value of 'live' factor
     return mean_live
result_live=mean_live()
print('The average value of live is:',format(result_live,'.2f'))

def mean_dur():
     column_name6 = 'dur'
     dur_values = pd.to_numeric(df[column_name6], errors='coerce')
     mean_dur=dur_values.mean()#find the mean value of 'dur' factor
     return mean_dur
result_dur=mean_dur()
print('The average value of dur is:',format(result_dur,'.2f'))

def mean_acous():
     column_name7 = 'acous'
     acous_values = pd.to_numeric(df[column_name7], errors='coerce')
     mean_acous=acous_values.mean()#find the mean value of 'acous' factor
     return mean_acous
result_acous=mean_acous()
print('The average value of acous is:',format(result_acous,'.2f'))

def mean_spch():
     column_name8 = 'spch'
     spch_values = pd.to_numeric(df[column_name8], errors='coerce')
     mean_spch=spch_values.mean()#find the mean value of 'spch' factor
     return mean_spch
result_spch=mean_spch()
print('The average value of spch is:',format(result_spch,'.2f'))

def pop_top10():
     column_name8 = 'pop' # specify the 'pop' column 
     largest_10 = df.nlargest(10, column_name8)# find the top10 largest pop value
     return largest_10
result_pop=pop_top10()
print('The Top10 popular songs from 2010 to 2019:')
print(result_pop)
output_file = 'top_10_output.txt'
with open(output_file, 'w') as txt_file:
     #make a txt file for the top10 song, make it easier to analyze
    txt_file.write(result_pop.to_string(index=False))

import matplotlib.pyplot as plt
import matplotlib as mpl
#For analyzing each factor, import library and draw scatter plot
top_genres = df['top genre']
bpm=df['bpm']
acous=df['acous']
pop=df['pop']
dnce=df['dnce']
nrgy=df['nrgy']
dB=df['dB']
live=df['live']
spch=df['spch']
dur=df['dur']

fig,ax1=plt.subplots()#Create a figure containing a single axes
ax1.scatter(nrgy,pop)#ax1 means the first scatter plot, which is about nrgy
ax1.set_xlabel('energy')#Add an x-label
ax1.set_ylabel('popularity')#Add an y-label
ax1.set_title("Energy&Pop") #add a title to the axes
plt.show
##Process each factors one by one
fig,ax2=plt.subplots()
ax2.scatter(bpm,pop)
ax2.set_xlabel('dance')
ax2.set_ylabel('popularity')
ax2.set_title("dnce&Pop")
plt.show
fig,ax3=plt.subplots()
ax3.scatter(bpm,pop)
ax3.scatter(acous,pop)
#in ax3, based on our hypothesis, I put 'bpm' and 'acous' together
ax3.set_xlabel('acous&tempo')
ax3.set_ylabel('popularity')
ax3.set_title("bpm&acous&Pop")
plt.show
fig,ax4=plt.subplots()
ax4.scatter(dB,pop)
ax4.set_xlabel('dB')
ax4.set_ylabel('popularity')
ax4.set_title("dB&Pop")
plt.show
fig,ax5=plt.subplots()
ax5.scatter(live,pop)
ax5.scatter(spch,pop)
ax5.set_xlabel('spch&live')
ax5.set_ylabel('popularity')
ax5.set_title("spch&dB&Pop")
plt.show
fig,ax6=plt.subplots()
ax6.scatter(dur,pop)
ax6.set_xlabel('dur')
ax6.set_ylabel('popularity')
ax6.set_title("dur&Pop")
plt.show
##Next step is for making the most popular music genre visualizable
plt.figure(figsize=(12, 6))#set up the figure size
top_genres.value_counts().plot(kind='bar')
# Uses the value_counts() function to get the counts of unique values
plt.title('Distribution of Items in "Top Genre" Column')
plt.xlabel('Top Genre')
plt.ylabel('Count')
plt.tight_layout()
plt.show()











