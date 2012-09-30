import json
import sys
import calendar
import matplotlib.pyplot as plt
from matplotlib import rc, rcParams
import numpy as np
import random

dataset_file = "yelp_academic_dataset.json"

def returnDay(date):
	"""
	Returns the day of the week given a date as an integer (where Monday = 0, Tuesday = 1, ..., Sunday = 7)
	"""
	days = {0:"Monday", 1:"Tuesday", 2:"Wednesday", 3:"Thursday", 4:"Friday", 5:"Saturday", 6:"Sunday"}
	d = date.split('-')
	dY = int(d[0])
	dM = int(d[1])
	dD = int(d[2])
	dateObject = calendar.datetime.date(year = dY, month = dM, day = dD)
	dayOfWeek = dateObject.weekday()
	return days[dayOfWeek]

def get_counts(sequence):
	"""
	Returns a dictionary given a list where the dictionary's values are counts of keys
	"""
	counts = {}
	for x in sequence:
		if x in counts:
			counts[x] += 1
		else:
			counts[x] = 1
	return counts

def convertDatesToDays(dates):
	"""
	Returns a list of days of the week given a list of dates
	"""
	days = []
	for d in dates:
		dayOfReview = returnDay(d)
		days.append(dayOfReview)
	return days

def importJSON(dataset):
	yelp_data = open(dataset)
	r = []
	b = []
	u = []
	for line in yelp_data:
		try:
			data = json.loads(line)
		except ValueError:
			print "Oops!"
		if data["type"] == "user":
			u.append(data)
		elif data["type"] == "business":
			b.append(data)
		elif data["type"] == "review":
			r.append(data)
	return r, b, u

def autolabel(rects):
	"""
	Attach text labels to rectangles
	"""
	for rect in rects:
		height = rect.get_height()
		plt.text(rect.get_x()+rect.get_width()/2., 1.01*height, '%d'%int(height), ha='center', va='bottom')

def randomSample(r, sizeOfSample):
	"""
	Returns a random sample from list r
	"""
	sampleSet = []
	for i in range(sizeOfSample):
		rInt = random.randint(0,len(r)-1)
		sampleSet.append(r[rInt])
	return sampleSet

def buildBarDayPlot(dayDictionary, title = "Count versus Day", order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']):
	"""
	Returns a bar plot given an input of days (in dictionary form)
	"""
	N = len(dayDictionary)
	x = np.arange(N)
	y = []
	fig = plt.figure(facecolor='w', figsize=(8,6))
	ax = fig.add_subplot(111)
	for o in order:
		try:
			y.append(dayDictionary[o])
		except KeyError:
			y.append(0)
	rects = plt.bar(x+0.25, y, width=0.5, align='edge', color='#A3A3A3', edgecolor='w')
	plt.ylabel('Counts')
	plt.title(title)
	plt.xticks(x+0.25, order, rotation=25)
	plt.grid(axis='y', color='w', linestyle='-', linewidth=2)
	for i, line in enumerate(ax.get_xticklines() + ax.get_yticklines()):
		line.set_visible(False)
	ax.axes.get_yaxis().set_visible(True)
	params = {'axes.linewidth' : 0}
	plt.rcParams.update(params)
	plt.savefig('%s.png' % title, bbox_inches=0, dpi=75)
	plt.show()

def buildHistogramPlot(dataList, title="Histogram Counts", bins = 10):
	"""
	Returns a histogram plot given an input of data
	"""
	frequencyOfData = get_counts(dataList)
	fig = plt.figure(facecolor='w', figsize=(8,6))
	ax = fig.add_subplot(111)
	h = plt.hist(frequencyOfData.values(), bins, color='#A3A3A3', edgecolor="w")
	plt.ylabel("Number of Users")
	plt.xlabel("Total Number of Reviews")
	plt.grid(axis='y', color='w', linestyle='-', linewidth=2)
	for i, line in enumerate(ax.get_xticklines() + ax.get_yticklines()):
		line.set_visible(False)
	ax.axes.get_yaxis().set_visible(True)
	params = {'axes.linewidth' : 0}
	plt.xlim(0,450)
	plt.rcParams.update(params)
	plt.title(title)
	plt.savefig('%s.png' % title, bbox_inches=0, dpi=75)
	plt.show()

def buildDoubleLogPlot(dataList, title="Log Plot"):
	"""
	Returns a double log plot, useful for power distributions
	"""
	frequencyOfData = get_counts(dataList)
	fig = plt.figure(facecolor='w', figsize=(8,6))
	ax = fig.add_subplot(111)
	ll = plt.plot(frequencyOfData.values(), "o", color="#A3A3A3")
	plt.ylabel("Number of Users")
	plt.xlabel("Number of Reviews per User")
	for i, line in enumerate(ax.get_xticklines() + ax.get_yticklines()):
		line.set_visible(False)
	ax.axes.get_yaxis().set_visible(True)
	params = {'axes.linewidth' : 1}
	plt.rcParams.update(params)
	plt.title(title)
	plt.xscale('log')
	plt.yscale('log')
	plt.savefig('%s.png' % title, bbox_inches=0, dpi=75)
	plt.show()

def build3BarDayPlot(dayDictionary1, dayDictionary2, dayDictionary3, title="Count versus Day"):
	"""
	Returns a two bar plot given three inputs of days (in dictionary form)
	"""
	N = len(dayDictionary1)
	M = len(dayDictionary2)
	O = len(dayDictionary3)
	if N != M or N != O:
		print("Data is not equal length")
		sys.exit()
	x = np.arange(N)
	y1 = []
	y2 = []
	y3 = []
	fig = plt.figure(facecolor='w', figsize=(8,6))
	ax = fig.add_subplot(111)
	for day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']:
		y1.append(dayDictionary1[day])
		y2.append(dayDictionary2[day])
		y3.append(dayDictionary3[day])
	rects1 = plt.bar(x+0.1, y1, width=0.25, align='edge', color='#BA9D19', edgecolor='w')
	rects2 = plt.bar(x+0.35, y2, width=0.25, align='edge', color='#576B54', edgecolor='w')
	rects3 = plt.bar(x+0.6, y3, width=0.25, align='edge', color='#BC5D58', edgecolor='w')
	plt.ylabel('Counts')
	plt.title(title)
	plt.xticks(x+0.50, ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'), rotation=25)
	plt.grid(axis='y', color='w', linestyle='-', linewidth=2)
	for i, line in enumerate(ax.get_xticklines() + ax.get_yticklines()):
		line.set_visible(False)
	ax.axes.get_yaxis().set_visible(True)
	leg = ax.legend( (rects1[0], rects2[0], rects3[0]), ('Occasional', 'Moderate', 'Power'), loc= 'upper right')
	leg.draw_frame(False)
	params = {'axes.linewidth' : 0}
	plt.rcParams.update(params)
	plt.savefig('%s.png' % title, bbox_inches=0, dpi=75)
	plt.show()

def build2BarDayPlot(dayDictionary1, dayDictionary2, title="Count versus Day"):
	"""
	Returns a two bar plot given two inputs of days (in dictionary form)
	"""
	N = len(dayDictionary1)
	M = len(dayDictionary2)
	if N != M:
		print("Data is not equal length")
		sys.exit()
	x = np.arange(N)
	y1 = []
	y2 = []
	fig = plt.figure(facecolor='w', figsize=(8,6))
	ax = fig.add_subplot(111)
	for day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']:
		y1.append(dayDictionary1[day])
		y2.append(dayDictionary2[day])
	rects1 = plt.bar(x+0.25, y1, width=0.4, align='edge', color='#BA9D19', edgecolor='w')
	rects2 = plt.bar(x+0.65, y2, width=0.4, align='edge', color='#576B54', edgecolor='w')
	plt.ylabel('Counts')
	#plt.xlabel('Day of the Week')
	plt.title(title)
	plt.xticks(x+0.50, ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'), rotation=25)
	plt.grid(axis='y', color='w', linestyle='-', linewidth=2)
	#autolabel(rects)
	for i, line in enumerate(ax.get_xticklines() + ax.get_yticklines()):
		line.set_visible(False)
	plt.ylim(0,18000)
	ax.axes.get_yaxis().set_visible(True)
	leg = ax.legend( (rects1[0], rects2[0]), ('Restaurants', 'Non-Restaurants'), loc= 'upper right')
	leg.draw_frame(False)
	params = {'axes.linewidth' : 0}
	plt.rcParams.update(params)
	plt.savefig('%s.png' % title, bbox_inches=0, dpi=75)
	plt.show()

def sampleSize(population, E=1, CV=1.96):
	"""
	Returns an integer of what a sample size should be to satisfy a critical value (CV) and margin-of-error (E). Input is a list.
	"""
	popSTD = np.std(population)
	almostThere = (CV*popSTD)/E
	ssize = almostThere**2
	return int(ssize)