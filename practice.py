import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
import datetime as dt
from datetime import timedelta
import time

# df1_ori = pd.read_csv('Aug_25.csv',usecols=['Timestamp'] ,parse_dates=['Timestamp'],engine='python',index_col=None)
# df1 = pd.read_csv('Aug_25.csv',engine='python',index_col=None)
# df2 = pd.read_csv('2020-08-26-17-59_1.csv',engine='python',index_col=None)
# df2_ori = pd.read_csv('Aug_25.csv',usecols=['STATION_1:Freq'] ,engine='python',index_col=None)
# df1_Tpmu = pd.read_csv('11_08.csv',usecols=['Timestamp'],parse_dates=['Timestamp'],engine='python',index_col=None)
# df2_fpmu = pd.read_csv('11_08.csv',usecols=['freq:'] ,engine='python',index_col=None)
# ti_pmu_lis = df1_Tpmu['Timestamp'].astype(str).tolist()
# freq_pmu_lis = df2_fpmu['freq:'].astype(float).tolist()
# ti_ori_lis = df1_ori['Timestamp'].astype(str).tolist()
# freq_ori_lis = df2_ori['STATION_1:Freq'].astype(float).tolist()




df1_ori = (pd.read_csv('Aug_25.csv',usecols=['Timestamp'] ,parse_dates=['Timestamp'],engine='python',index_col=None))
df2_ori = (pd.read_csv('Aug_25.csv',usecols=['STATION_1:Freq'] ,engine='python',index_col=None))
df1_Tpmu = (pd.read_csv('2020-10-26-15-54_645.csv',usecols=['Timestamp'],parse_dates=['Timestamp'],engine='python',index_col=None))
df2_fpmu = (pd.read_csv('2020-10-26-15-54_645.csv',usecols=['freq:'] ,engine='python',index_col=None))
df3_Tpmu = (pd.read_csv('2020-10-26-19-26_666.csv',usecols=['Timestamp'],parse_dates=['Timestamp'],engine='python',index_col=None))
df3_fpmu = (pd.read_csv('2020-10-26-19-26_666.csv',usecols=['freq:'] ,engine='python',index_col=None))

# 2020-10-26-19-26_666.csv


# 2020-10-26-15-54_645.csv
# 2020-10-26-18-26_660.csv == 60Hz
# 2020-10-14-02-03_9.csv

# 2020-10-06-03-03_75.csv
#2020-10-05-23-40_55.csv

#2020-10-05-22-39_49.csv
# '2020-10-05-15-13_5.csv'
#2020-10-05-21-38_43.csv

# df2_ori['diff'] = df2_ori['STATION_1:Freq'] - df2_fpmu['freq:']
# df2_ori['offset'] = df2_fpmu['freq:'] + df2_ori['diff']


def temp(df2_fpmu):

	df2_fpmu['STATION_1:Freq'] = df2_ori['STATION_1:Freq']

	df2_fpmu['SD_PMU'] = df2_fpmu['freq:'].std()

	# df2_fpmu['Std Dev + freq:'] = df2_fpmu['Std Dev'] + df2_fpmu['freq:']

	df2_fpmu['SD_PMU + freq:'] = df2_fpmu['STATION_1:Freq'] - df2_fpmu['SD_PMU']

	df2_fpmu['offset'] = df2_fpmu['STATION_1:Freq'] - df2_fpmu['freq:']

	# print('max offset',max(df2_fpmu['offset']))

	# print('offset Mean: ',df2_fpmu['offset'].mean())

	df2_fpmu['edited_pmu Vals'] = df2_fpmu['offset'].mean() + df2_fpmu['freq:']

	


# temp(df2_fpmu)


f_pmu = df1_Tpmu.iloc[0]
f_ori = df1_ori.iloc[0]
diff = (f_pmu - f_ori).dt
df3=pd.DatetimeIndex(df1_Tpmu['Timestamp'])
dif = df3 - pd.DateOffset(days=int(diff.days),seconds=int(diff.seconds),microseconds=int(diff.microseconds))
df = pd.DataFrame(dif)


def correlation(df1_ori,df2_ori,df1_Tpmu,df2_fpmu,df):

	print(df2_fpmu)

	corr = df2_ori['STATION_1:Freq'].corr(df2_fpmu['freq:'])
	print('Correlation:	',corr)

	mean_pmu = df2_ori['freq:'].mean()

	std_pmu =  df2_ori['freq:'].std()

	mean_ori = df2_ori['STATION_1:Freq'].mean()

	std_ori = df2_ori['STATION_1:Freq'].std()

	mean_both = mean_ori - mean_pmu

	print('\n The difference between both freq columns \n \n',mean_both,'\n')

	d = {'  ': ['Correlation','mean','std deviation'],'Original File': [corr,mean_ori,std_ori], 'PMU File':[corr,mean_pmu,std_pmu]}

	df =pd.DataFrame(d) 

	print(df)



correlation(df1_ori,df2_ori,df1_Tpmu,df2_fpmu,df)

def scaled_TS(df1_ori,df2_ori,df1_Tpmu,df2_fpmu,offset):
	# print('dataframe type is ',type(df1_Tpmu))
	f_pmu = df1_Tpmu.iloc[0]#first TS value in pmu file
	#print(df1_Tpmu)
	#print('pmu ts first value ',f_pmu)
	f_ori = df1_ori.iloc[0]#first TS value in original file
	#print('ori ts first value ',f_ori)
	diff = (f_pmu - f_ori).dt#.astype(int)

	df3=pd.DatetimeIndex(df1_Tpmu['Timestamp'])
	#print('the difference is ',df3)
	dif = df3 - pd.DateOffset(days=int(diff.days),seconds=int(diff.seconds),microseconds=int(diff.microseconds))
	#print('dif type is ',type(dif)) #type is DatetimeIndex
	df = pd.DataFrame(dif)
	# dfPMU = df.loc[:10876]
	# print(df)
	# print(type(df))

	return df
# scaled_TS(df1_ori,df2_ori,df1_Tpmu,df2_fpmu,offset)
def combined_plots_with_offset(df1_ori,df2_ori,df1_Tpmu,df2_fpmu):
	df = scaled_TS(df1_ori,df2_ori,df1_Tpmu,df2_fpmu,offset)
	# print('scaled timestamp is ',df)
	# plt.plot(df,df2_ori)
	# plt.plot(df,df2_fpmu)
	# plt.show()
	# print('PMU   ',len(df1_Tpmu))
	# print('original   ',len(df1_ori))


	# df2_ori['diff'] = df2_ori['STATION_1:Freq'] - df2_fpmu['freq:']
	
	
	# df2_ori['offset'] = df2_fpmu['freq:'] + df2_ori['diff']
	
	# offset = pd.DataFrame(df2_ori['offset'])

	# print(df2_ori['offset'])
	# print(df2_ori['STATION_1:Freq'])
	fig,ax = plt.subplots()
	# ax.plot(df1_ori,df2_ori['STATION_1:Freq'],label='Original')
	# ax.plot(df1_Tpmu,df2_fpmu,label='PMU')
	ax.plot(df,df2_ori['STATION_1:Freq'],label='Original')
	ax.plot(df,offset,label='PMU')
	ax.tick_params(rotation=30)
	handles, labels = ax.get_legend_handles_labels()
	fig.legend(handles, labels, loc='upper right')
	plt.title('With an offset Calc')
	plt.grid()
	plt.show()	
# combined_plots_with_offset(df1_ori,df2_ori,df1_Tpmu,df2_fpmu)


def combined_plots(df1_ori,df2_ori,df1_Tpmu,df2_fpmu,df):
	fig,ax = plt.subplots()
	ax.plot(df.head(10000),df2_ori['STATION_1:Freq'].head(10000),label='Original')
	ax.plot(df.head(10000),df2_fpmu['freq:'].head(10000),label='PMU',alpha=0.5)
	# ax.plot(df,df2_fpmu['SD_PMU + freq:'],label='offset_values',alpha=0.5)
	# ax.plot(df,df2_fpmu['edited_pmu Vals'],label='edited_pmu VALS',alpha=0.3)
	ax.tick_params(rotation=30)

	handles, labels = ax.get_legend_handles_labels()
	fig.legend(handles, labels, loc='upper right')
	plt.title('Original and PMU Freq Data')
	plt.grid()
	plt.show()	
# combined_plots(df1_ori,df2_ori,df1_Tpmu,df2_fpmu,df)

def real_time(df1_ori,df2_ori,df1_Tpmu,df2_fpmu,df,df3_Tpmu,df3_fpmu):
	# fig,ax = plt.subplots()
	x1 = df2_ori['STATION_1:Freq']
	x2 = df2_fpmu['freq:']
	# x3 = df3_fpmu['freq:']
	# y3 = [dt.datetime.now() + dt.timedelta(microseconds=i) for i in range(len(x1))]
	y1 = [dt.datetime.now() + dt.timedelta(microseconds=i) for i in range(len(x1))]
	y2 = [dt.datetime.now() + dt.timedelta(microseconds=i) for i in range(len(x2))]
	plt.plot(y1,x1,label="Original Data")
	plt.plot(y1,x2,label="PMU Data")
	# plt.plot(y1,x3,label="PMU Data")
	plt.title('2020-09-29-11-45_2.csv')
	plt.legend()
	plt.grid()
	plt.gcf().autofmt_xdate()
	plt.show()
real_time(df1_ori,df2_ori,df1_Tpmu,df2_fpmu,df,df3_Tpmu,df3_fpmu)

def scatter_plot(df1_ori,df2_ori,df1_Tpmu,df2_fpmu,df):
	# fig,ax = plt.subplots()
	x1 = df2_ori['STATION_1:Freq']
	x2 = df2_fpmu['freq:']
	y1 = [dt.datetime.now() + dt.timedelta(microseconds=i) for i in range(len(x1))]
	y2 = [dt.datetime.now() + dt.timedelta(microseconds=i) for i in range(len(x2))]
	plt.scatter(y1,x1, alpha=0.5)
	# plt.plot(y1,x2, s=area, c=colors, alpha=0.5)
	plt.title('2020-09-29-11-45_2.csv')
	plt.grid()
	plt.gcf().autofmt_xdate()
	plt.show()
# scatter_plot(df1_ori,df2_ori,df1_Tpmu,df2_fpmu,df)


# y_del = []
# x_del = [i for i in range(18000)]
# #real_time(df1_ori,df2_ori,df1_Tpmu,df2_fpmu,df)
# for i,j in zip(df2_ori.iterrows(),df2_fpmu.iterrows()):
# 	y_del.append(float(i[1])- float(j[1]))
# plt.plot(x_del,y_del)
# plt.show()
def combined_plots_formatted_xaxis(df1_ori,df2_ori,df1_Tpmu,df2_fpmu,df):

	df = mdates.date2num(df)
	fig,ax = plt.subplots()
	ax.plot(df,df2_ori['STATION_1:Freq'],label='Original')
	ax.plot(df,df2_fpmu['freq:'],label='PMU',alpha=0.5)
	hfmt = mdates.DateFormatter('%Y-%m-%d %H:%M:%S.%f')
	ax.xaxis.set_major_formatter(hfmt)
	# ax.plot(df,df2_fpmu['SD_PMU + freq:'],label='offset_values',alpha=0.5)
	ax.plot(df,df2_fpmu['edited_pmu Vals'],label='edited_pmu VALS',alpha=0.3)
	ax.tick_params(rotation=90)

	handles, labels = ax.get_legend_handles_labels()
	fig.legend(handles, labels, loc='upper right')
	plt.title('Original and PMU Freq Data')
	plt.grid()
	plt.show()	
# combined_plots_formatted_xaxis(df1_ori,df2_ori,df1_Tpmu,df2_fpmu,df)

def test(df1_ori,df2_ori,df1_Tpmu,df2_fpmu,df):

	# df = mdates.date2num(df)
	fig,ax = plt.subplots()
	# ax.plot(df1_ori['Timestamp'],df2_ori['STATION_1:Freq'],label='Original')
	ax.plot(df1_Tpmu['Timestamp'],df2_fpmu['freq:'],label='PMU',alpha=0.5)
	hfmt = mdates.DateFormatter('%Y-%m-%d %H:%M:%S.%f')
	ax.xaxis.set_major_formatter(hfmt)
	ax.tick_params(rotation=90)

	handles, labels = ax.get_legend_handles_labels()
	fig.legend(handles, labels, loc='upper right')
	plt.title('Original and PMU Freq Data')
	plt.grid()
	plt.show()	

# test(df1_ori,df2_ori,df1_Tpmu,df2_fpmu,df)



def subplot(df1_ori,df2_ori,df1_Tpmu,df2_fpmu):
	# df,dfPMU = scaled_TS(df1_ori,df2_ori,df1_Tpmu,df2_fpmu)
	
	print(df2_fpmu.head(34))
	# fig = plt.figure(dpi=100,figsize=(13.3,8.2))
	fig, (ax,ax1) = plt.subplots(2,1)

	line_labels = ["Original File","PMU File"]

	ax.plot(df1_ori['Timestamp'].loc[1:],df2_ori['STATION_1:Freq'].loc[1:],color='r')

	ax.tick_params(rotation=30)

	ax.grid(True)

	ax.set_xlabel('freq')

	ax.set_ylabel('Timestamp')

	ax1.plot(df1_Tpmu.loc[34:],df2_fpmu.loc[34:])

	ax1.tick_params(rotation=30)

	ax1.set_xlabel('freq')

	ax1.set_ylabel('Timestamp')

	ax1.grid(True)

	fig.tight_layout()

	fig.legend([ax,ax1],labels = line_labels,loc = "upper right",borderaxespad=0.1)

	plt.suptitle('Original and PMU Freq Data')

	plt.show()
# subplot(df1_ori,df2_ori,df1_Tpmu,df2_fpmu)

'''
time = []
freq_o = []

with open("F_resp.csv") as csv_file:
	csv_reader = csv.DictReader(csv_file, delimiter=',')
	for rows in csv_reader:
		x = rows['Timestamp']
		y = rows['STATION_1:Freq']
		time.append(str(x))
		freq_o.append(float(y))
	# print('min value in original value is ',min(freq_o))
	# print('max value in original value is ',max(freq_o))
'''
def original_file(df1_ori,df2_ori):
	# df1_ori = pd.read_csv('F_resp.csv',usecols=['Timestamp'] ,engine='python',index_col=None)
	# df2_ori = pd.read_csv('F_resp.csv',usecols=['STATION_1:Freq'] ,engine='python',index_col=None)
	ti_ori = df1_ori['Timestamp'].astype(str).tolist()
	freq_ori = df2_ori['STATION_1:Freq'].astype(float).tolist()
	plt.figure(dpi=100,figsize=(13.3,8.2)) #(width,length)
	plt.plot(ti_ori,freq_ori)
	ax = plt.gca()
	ax.set_xticks(ax.get_xticks()[::250])
	plt.xticks(rotation=90)
	plt.grid()
	plt.title('Original file (samples 250)')
	plt.xlabel('Timestamp')
	plt.ylabel('Freq')
	return plt

#original_file(df1_ori,df2_ori)
# x = original_file(df1_ori,df2_ori)
# x.show()
def nan_issue(df1_Tpmu,df2_fpmu):
	df2_fpmu.replace('#NaN',float(np.nan),inplace=True)
	ti = df1_Tpmu['Timestamp'].astype(str).tolist()
	freq = df2_fpmu['freq:'].astype(float).tolist()
	plt.figure(dpi=100,figsize=(13.3,8.2)) #(width,length)
	plt.plot(ti,freq)
	ax = plt.gca()
	ax.set_xticks(ax.get_xticks()[::250])
	plt.xticks(rotation=90)
	plt.grid()
	plt.title('PMU file samples 100')
	plt.xlabel('Timestamp')
	plt.ylabel('Freq')
	plt.show()
# nan_issue(df1_Tpmu,df2_fpmu)
# original_file()

def subplots(df1_ori,df2_ori,df1_Tpmu,df2_fpmu):
	ti_ori = df1_ori['Timestamp'].astype(str).tolist()
	freq_ori = df2_ori['STATION_1:Freq'].astype(float).tolist()
	df2_fpmu.replace('#NaN',float(np.nan),inplace=True)
	ti = df1_Tpmu.loc[6510:12000,'Timestamp'].astype(str).tolist()
	freq = df2_fpmu.loc[6510:12000,'freq:'].astype(float).tolist()
# subplot(df1_ori,df2_ori,df1_Tpmu,df2_fpmu)

def scaled_TS(df1_ori,df2_ori,df1_Tpmu,df2_fpmu):
	print('dataframe type is ',type(df1_Tpmu))
	f_pmu = df1_Tpmu.iloc[0]#first TS value in pmu file
	#print(df1_Tpmu)
	#print('pmu ts first value ',f_pmu)
	f_ori = df1_ori.iloc[0]#first TS value in original file
	#print('ori ts first value ',f_ori)
	diff = (f_pmu - f_ori).dt#.astype(int)

	df3=pd.DatetimeIndex(df1_Tpmu['Timestamp'])
	#print('the difference is ',df3)
	dif = df3 - pd.DateOffset(days=int(diff.days),seconds=int(diff.seconds),microseconds=int(diff.microseconds))
	#print('dif type is ',type(dif)) #type is DatetimeIndex
	df = pd.DataFrame(dif)
	dfPMU = df.loc[:10876]
	print(df)
	print(type(df))

	return df,dfPMU
	#dif = dif.to_series()
	# print(array)
	# print(len(array))

	# print(dif,type(dif))
	# ti = dif.astype(str).tolist()
	# print(len(ti[2:]))
	# for i,j in zip(dif, df1_Tori['Timestamp']):
	# 	print(i,j)


	# for i,j in zip(dif, df1_Tori['Timestamp']):
	# 	j, i = (str(j).split(':')[1:],str(i).split(':')[1:])
	# 	print('orig: {} -- new: {}'.format(j,i))
	# 	md = int(i[0])-int(j[0])
	# 	mmd = float(j[1])-float(i[1])
	# 	print(' NEW - OLD',md,' min ', mmd, ' secs')
		  
	#print(df1_Tori.Timestamp)
	# print(dif,type(dif))
	# dif = diff - f_ori
	# print(dif)
	# print(type(diff),diff)
	# print('the difference between pmu and original value ',diff)
	# i = 3
	# while i < 4:#len(df1_Tori):
	# 	ti_orig = df1_Tpmu.iloc[i]
	# 	# print(type(ti_orig))
	# 	# m = diff - ti_orig
	# 	# print(m)
	# 	i = i + 1



	# 	time_diff.append(x)
	# 	i = i + 1
	# print(time_diff)
		 
	# ti = df1_Tpmu['Timestamp'].values.astype(float)

	# print(type(ti))
	# for x,y in zip(ti_ori,ti):
	# 	print(x-y)


	# df1_Tori = pd.to_datetime(df1_Tori["Timestamp"])
	# df1_Tori=pd.Series([val.time() for val in df1_Tori])
	# df1_Tori = df1_Tori.astype(float)
	# print(df1_Tori)
	# df1_Tori['Timestamp'] = pd.to_datetime(df1_Tori["Timestamp"].dt.strftime("%S.%f"))
	# print(df1_Tori)

# scaled_TS(df1_ori,df2_ori,df1_Tpmu,df2_fpmu)

def pmu17_Aug(df1_Tpmu,df2_fpmu,df1_ori,df2_ori,ti_pmu_lis,freq_pmu_lis,ti_ori_lis,freq_ori_lis):
	print('pmu_freq',len(df2_fpmu))
	print('pmu_Timstamp',len(df1_Tpmu))
	print('Ori Timestamp',len(df1_ori))
	print('Ori freq',len(df2_ori))

	# ti_pmu = df1_Tpmu['Timestamp'].astype(str).tolist()
	# freq_pmu = df2_fpmu['freq:'].astype(float).tolist()

	# plt.figure(dpi=100,figsize=(13.3,8.2)) #(width,length)
	# plt.plot(ti_pmu_lis,freq_pmu_lis,label='PMU FILE')
	# # plt.plot(ti_ori_lis,freq_ori_lis,label='ORIGINAL FILE')
	# plt.legend(loc='upper right')
	# ax = plt.gca()
	# ax.set_xticks(ax.get_xticks()[::250])
	# plt.xticks(rotation=90)
	# plt.grid()
	# plt.title('pmu file (samples 250)')
	# plt.xlabel('Timestamp')
	# plt.ylabel('Freq')
	# plt.show()

# pmu17_Aug(df1_Tpmu,df2_fpmu,df1_ori,df2_ori,ti_pmu_lis,freq_pmu_lis,ti_ori_lis,freq_ori_lis)

def two_plots(df1_Tpmu,df2_fpmu,df1_ori,df2_ori,ti_pmu_lis,freq_pmu_lis,ti_ori_lis,freq_ori_lis):

	fig = plt.figure(dpi=100,figsize=(13.3,8.2))
	ax1 = fig.add_subplot(111)
	ax2 = ax1.twiny()
	pm = ax1.plot(ti_pmu_lis,freq_pmu_lis,label='PMU FILE',color='r')
	ori = ax2.plot(ti_ori_lis,freq_ori_lis,label='ORIGINAL FILE')
	ax2 = plt.gca()
	ax2.set_xticks(ax2.get_xticks()[::350])
	#plt.xticks(rotation=90)
	#ax2.xaxis.set_ticks_position('top')
	# plt.legend(loc='upper right')
	# ax1 = plt.gca()
	ax1.set_xticks(ax1.get_xticks()[::350])
	# plt.xticks(rotation=90)
	plt.setp(ax1.get_xticklabels(), rotation=90)
	plt.setp(ax2.get_xticklabels(), rotation=90)
	handles, labels = ax1.get_legend_handles_labels()
	fig.legend(handles, labels, loc='lower right')
	handles, labels = ax2.get_legend_handles_labels()
	fig.legend(handles, labels, loc='upper right')
	# ax1.xaxis.set_ticks_position('bottom')
	plt.grid()
	plt.title('pmu file (samples 250)')
	plt.xlabel('Timestamp')
	plt.ylabel('Freq')

	plt.show()


# two_plots(df1_Tpmu,df2_fpmu,df1_ori,df2_ori,ti_pmu_lis,freq_pmu_lis,ti_ori_lis,freq_ori_lis)

def real_time(df1_Tpmu,df2_fpmu,df1_ori,df2_ori,ti_pmu_lis,freq_pmu_lis,ti_ori_lis,freq_ori_lis):
	# print(len(df2_fpmu))
	df,dfPMU = scaled_TS(df1_ori,df2_ori,df1_Tpmu,df2_fpmu)

	# print(df.loc[:10876])
	# print(df[df['Timestamp'] == '2019-09-19 02:06:46.9154'])
	#"2019-09-19 02:06:46.9154"
	
	# df1_Tpmu = mdates.date2num(df1_Tpmu)
	# df1_ori = mdates.date2num(df1_ori)
	df = mdates.date2num(df)
	dfPMU = mdates.date2num(dfPMU)
	fig = plt.figure(dpi=100,figsize=(13.3,8.2))
	ax = fig.subplots()
#	hfmt = mdates.DateFormatter('%H:%M:%S.%f')
	hfmt = mdates.DateFormatter('%Y-%m-%d %H:%M:%S.%f')
	ax.xaxis.set_major_formatter(hfmt)
	_=plt.xticks(rotation=90)
	# ax.plot(df1_ori,df2_fpmu)
	# ax.plot(df1_ori,df2_ori)
# ti = df1_Tpmu.loc[6510:12000,'Timestamp']

	ax.plot(dfPMU,df2_fpmu.loc[:10876],label='PMU')
	ax.plot(df,df2_ori,label='Original')
	handles, labels = ax.get_legend_handles_labels()
	fig.legend(handles, labels, loc='lower right')
	plt.grid()
	plt.title('Scaled x-axis')
	plt.xlabel('Timestamp')
	plt.ylabel('Freq')
	plt.show()


# real_time(df1_Tpmu,df2_fpmu,df1_ori,df2_ori,ti_pmu_lis,freq_pmu_lis,ti_ori_lis,freq_ori_lis)

def comp_vals(df1_Tpmu,df2_fpmu,df1_ori,df2_ori,df1,df2):

	df,dfPMU = scaled_TS(df1_ori,df2_ori,df1_Tpmu,df2_fpmu)
	
	# df2_ori['diff'] = np.where(df2_ori['STATION_1:Freq'] != df2_fpmu['freq:'],0,df2_ori['STATION_1:Freq'] - df2_fpmu['freq:'])	
	

	df2_ori['diff'] = df2_ori['STATION_1:Freq'] - df2_fpmu['freq:']
	
	print('the difference is',df2_ori['diff'])	
	
	df2_ori['offset'] = df2_ori['STATION_1:Freq'] - df2_ori['diff']
	
	# df2_ori['offset'] = np.where(df2_ori['STATION_1:Freq'] == df2_fpmu['freq:'],0,df2_ori['STATION_1:Freq'] - df2_ori['diff'])
	
	print('frequency values after scaling are ',df2_ori['offset'])
	
	# df2_ori['offset'] = df2_ori['STATION_1:Freq'] - df2_ori['diff']
	
	df2_ori['offset'] = df2_ori['offset'].replace(0,np.nan)

	offset = pd.DataFrame(df2_ori['offset'])
	print(offset)

	print('offset   ',type(offset))
	# print(df2_ori)
	df = mdates.date2num(df)
	dfPMU = mdates.date2num(dfPMU)	
	fig = plt.figure(dpi=100,figsize=(13.3,8.2))
	ax = fig.subplots()
	hfmt = mdates.DateFormatter('%Y-%m-%d %H:%M:%S.%f')
	ax.xaxis.set_major_formatter(hfmt)
	_=plt.xticks(rotation=90)



	# print(df2_ori['offset'])

	ax.plot(df,offset,color='blue',label='Original',alpha=0.15)
	ax.plot(df,df2_fpmu,color='black',label='pmu',alpha=0.2)
	plt.grid()
	plt.title('Scaled x-axis w/ offset')
	plt.xlabel('Timestamp')
	plt.ylabel('Freq')
	# plt.show()
	# i = 0
	# for rows in df2_ori['offset']:#.iterrows():
	# 	i = i + 1
	# 	if rows == 0:
			# print(rows)
			# print(i)


# comp_vals(df1_Tpmu,df2_fpmu,df1_ori,df2_ori,df1,df2)
def subplots(df1_Tpmu,df2_fpmu,df1_ori,df2_ori,df1,df2):

	df,dfPMU = scaled_TS(df1_ori,df2_ori,df1_Tpmu,df2_fpmu)
	
	# df2_ori['diff'] = np.where(df2_ori['STATION_1:Freq'] != df2_fpmu['freq:'],0,df2_ori['STATION_1:Freq'] - df2_fpmu['freq:'])	
	

	df2_ori['diff'] = df2_ori['STATION_1:Freq'] - df2_fpmu['freq:']
	
	print('the difference is',df2_ori['diff'])	
	
	df2_ori['offset'] = df2_ori['STATION_1:Freq'] - df2_ori['diff']
	
	# df2_ori['offset'] = np.where(df2_ori['STATION_1:Freq'] == df2_fpmu['freq:'],0,df2_ori['STATION_1:Freq'] - df2_ori['diff'])
	
	print('frequency values after scaling are ',df2_ori['offset'])
	
	# df2_ori['offset'] = df2_ori['STATION_1:Freq'] - df2_ori['diff']
	
	df2_ori['offset'] = df2_ori['offset'].replace(0,np.nan)

	offset = pd.DataFrame(df2_ori['offset'])

	print('offset   ',type(offset))
	# print(df2_ori)
	df = mdates.date2num(df)
	dfPMU = mdates.date2num(dfPMU)	

	fig = plt.figure(dpi=100,figsize=(13.3,8.2))
	ax = plt.subplots(2,1)
	ax1 = plt.subplots(2,2)
	ax.plot(df,offset,color='blue',label='Original',alpha=0.15)
	ax1.plot(df,df2_fpmu,color='black',label='pmu',alpha=0.2)	
	hfmt = mdates.DateFormatter('%H:%M:%S.%f')
	ax1.xaxis.set_major_formatter(hfmt)
	_=plt.xticks(rotation=90)


	ax.get_shared_x_axes().join(ax, ax1)
	ax.set_xticklabels([])


	# ax.plot(df,offset,color='blue',label='Original',alpha=0.15)
	# ax1.plot(df,df2_fpmu,color='black',label='pmu',alpha=0.2)
	plt.grid()
	plt.title('Scaled x-axis w/ offset')
	plt.xlabel('Timestamp')
	plt.ylabel('Freq')
	fig.tight_layout()
	plt.show()


# subplots(df1_Tpmu,df2_fpmu,df1_ori,df2_ori,df1,df2)