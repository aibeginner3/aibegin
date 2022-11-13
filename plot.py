#import pandas as pd
import matplotlib.pyplot as plt
import csv

##################################################
def plot_dos(infile, figname, xmin, xmax, y1min, y1max, y2min, y2max):

	with open(infile, "r", encoding="shift-jis", newline="") as f:
		# 読み込み（リーダーを取得）
		lines = csv.reader(f, delimiter="\t")

		data=[]
		for line in lines:
			if '#' in line[0]:
				line_split = [s for s in line[0].split(' ') if s != '']
				xlabel  = line_split[1] + line_split[2]
				y1label = line_split[3]
				y2label = line_split[4] + '_' + line_split[5]
				continue
			data.append([float(s) for s in line[0].split(' ') if s != ''])

		E=[]
		dosE=[]
		Int_dosE=[]
		for line in data:
			E.append(line[0])
			dosE.append(line[1])
			Int_dosE.append(line[2])

	#-------------------------------------------------
	fig = plt.figure()
	ax1 = fig.add_subplot(111)
	ln1 = ax1.plot(E, dosE,'C0',label=y1label)

	ax2 = ax1.twinx()
	ln2 = ax2.plot(E, Int_dosE,'C1',label=y2label)

	h1, l1 = ax1.get_legend_handles_labels()
	h2, l2 = ax2.get_legend_handles_labels()
	ax1.legend(h1+h2, l1+l2, loc='upper left')

	ax1.set_title("density of status")
	ax1.set_xlabel(xlabel)
	ax1.set_ylabel(y1label)
	ax1.set_xlim(xmin, xmax)
	ax1.set_ylim(y1min, y1max)
	ax1.grid(True)
	ax2.set_ylabel(y2label)
	ax2.set_ylim(y2min, y2max)

	plt.savefig(figname)
	plt.close()

def plot_band(infile, figname, xmin, xmax, ymin, ymax):

	with open(infile, "r", encoding="shift-jis", newline="") as f:
		# 読み込み（リーダーを取得）
		lines = csv.reader(f, delimiter="\t")

		data=[]
		for line in lines:
			if line==[]:
				data.append([])
			else:
				data.append([float(s) for s in line[0].split(' ') if s != ''])

		tmp1=[]
		tmp2=[]
		wavenum=[]
		E=[]
		for line in data:
			if line==[]:
				wavenum.append(tmp1)
				E.append(tmp2)
				tmp1=[]
				tmp2=[]
			else:
				tmp1.append(line[0])
				tmp2.append(line[1])

	nline = len(wavenum)

	for i in range(nline):
		plt.plot(wavenum[i], E[i])

	if xmin!=xmax:	plt.xlim(xmin, xmax)
	if ymin!=ymax:	plt.ylim(ymin, ymax)
	plt.xlabel('wave number')
	plt.ylabel('E')
	plt.title("band structure")
	plt.grid()
	plt.savefig(figname)
	plt.close()

def plot_charge(infile, figname, xmin, xmax, ymin, ymax):

	import numpy as np

	with open(infile, "r", encoding="shift-jis", newline="") as f:
		# 読み込み（リーダーを取得）
		lines = csv.reader(f, delimiter="\t")

		data=[]
		for line in lines:
			if line==[]:
				data.append([])
			else:
				data.append([float(s) for s in line[0].split(' ') if s != ''])

		tmp1=[]
		tmp2=[]
		tmp3=[]
		xdata=[]
		ydata=[]
		value=[]
		for line in data:
			if line==[]:
				xdata.append(tmp1)
				ydata.append(tmp2)
				value.append(tmp3)
				tmp1=[]
				tmp2=[]
				tmp3=[]
			else:
				tmp1.append(line[0])
				tmp2.append(line[1])
				tmp3.append(line[2])

	nline = len(value)

	x=[]
	for xvalue in xdata:
		x.append(xvalue[0])
	y = ydata[0]
	X, Y = np.meshgrid(x, y)
	Z = np.array(value).T

	fig = plt.figure()

	# 等高線を作成する。
	ax1 = fig.add_subplot(111)
	ax1.set_title("charge density")
	cont = ax1.contourf(X, Y, Z, cmap="jet")
	plt.colorbar(cont)

	#ax1.set_xlabel(xlabel)
	#ax1.set_ylabel(ylabel)
	if xmin!=xmax:	ax1.set_xlim(xmin, xmax)
	if ymin!=ymax:	ax1.set_ylim(ymin, ymax)

	# 3D グラフを作成する。
	#ax2 = fig.add_subplot(122, projection="3d")
	#ax2.set_title("surface")
	#ax2.plot_surface(X, Y, Z)

	plt.savefig(figname)
	plt.close()


##################################################

def run():

	dirname = 'plotdata\\'

	# charge density
	if 1:
		# 入力ファイル
		infile = dirname + 'charge.dat'

		# グラフ設定
		figname = 'test_charge.png'
		xmin, xmax = 0, 0
		ymin, ymax = 0, 0

		plot_charge(infile, figname, xmin, xmax, ymin, ymax)

	# band structure
	if 1:
		# 入力ファイル
		infile = dirname + 'graphene.band.gnu'

		# グラフ設定
		figname = 'test_band.png'
		xmin, xmax = 0, 0
		ymin, ymax = -20, 5

		plot_band(infile, figname, xmin, xmax, ymin, ymax)

	# density of status
	if 1:
		# 入力ファイル
		infile = dirname + 'graphene.dos'
		
		# グラフ設定
		figname = 'test_dos.png'
		xmin, xmax = -5, 5
		y1min, y1max = 0, 1.2
		y2min, y2max = 6, 10

		plot_dos(infile, figname, xmin, xmax, y1min, y1max, y2min, y2max)
		

if __name__ == "__main__":
    run()

