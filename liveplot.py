import threading
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time
import json
import numpy as np


# format de ce qui sort de flux['eeg']
# [
#     "COUNTER",
#     "INTERPOLATED",
#     "AF3","F7","F3","FC5","T7","P7","O1","O2","P8","T8","FC6","F4","F8","AF4",
#     "RAW_CQ",
#     "MARKER_HARDWARE",
#     "MARKERS"
# ]


lst_channels = ["AF3","F7","F3","FC5","T7","P7","O1","O2","P8","T8","FC6","F4","F8","AF4"]

class MyDataClass():

	def __init__(self):

		self.XData = [0]
		self.YData0 = [0]
		self.YData1 = [0]
		self.YData2 = [0]
		self.YData3 = [0]
		self.YData4 = [0]
		self.YData5 = [0]
		self.YData6 = [0]
		self.YData7 = [0]
		self.YData8 = [0]
		self.YData9 = [0]
		self.YData10 = [0]
		self.YData11 = [0]
		self.YData12 = [0]
		self.YData13 = [0]


class MyPlotClass():

	def __init__(self, dataClass):

		self._dataClass = dataClass

		# self.hLine, = plt.plot(0, 0)

		self.ani = FuncAnimation(plt.gcf(), self.run, interval = 50, repeat=True)
		self.ax0 = plt.subplot2grid((14,1), (0, 0), rowspan=1, colspan=1)
		self.ax1 = plt.subplot2grid((14,1), (1, 0), rowspan=1, colspan=1)
		self.ax2 = plt.subplot2grid((14,1), (2, 0), rowspan=1, colspan=1)
		self.ax3 = plt.subplot2grid((14,1), (3, 0), rowspan=1, colspan=1)
		self.ax4 = plt.subplot2grid((14,1), (4, 0), rowspan=1, colspan=1)
		self.ax5 = plt.subplot2grid((14,1), (5, 0), rowspan=1, colspan=1)
		self.ax6 = plt.subplot2grid((14,1), (6, 0), rowspan=1, colspan=1)
		self.ax7 = plt.subplot2grid((14,1), (7, 0), rowspan=1, colspan=1)
		self.ax8 = plt.subplot2grid((14,1), (8, 0), rowspan=1, colspan=1)
		self.ax9 = plt.subplot2grid((14,1), (9, 0), rowspan=1, colspan=1)
		self.ax10 = plt.subplot2grid((14,1), (10, 0), rowspan=1, colspan=1)
		self.ax11 = plt.subplot2grid((14,1), (11, 0), rowspan=1, colspan=1)
		self.ax12 = plt.subplot2grid((14,1), (12, 0), rowspan=1, colspan=1)
		self.ax13 = plt.subplot2grid((14,1), (13, 0), rowspan=1, colspan=1)

	def run(self, i):
		# print(self._dataClass.XData)
		# print("data =",len(self._dataClass.YData[0]))
		# self.hLine.set_data(self._dataClass.XData, self._dataClass.YData3)
		# self.hLine.axes.relim()
		# self.hLine.axes.autoscale_view()
		self.ax0.clear()
		self.ax1.clear()
		self.ax2.clear()
		self.ax3.clear()
		self.ax4.clear()
		self.ax5.clear()
		self.ax6.clear()
		self.ax7.clear()
		self.ax8.clear()
		self.ax9.clear()
		self.ax10.clear()
		self.ax11.clear()
		self.ax12.clear()
		self.ax13.clear()
		self.ax0.plot(self._dataClass.XData, self._dataClass.YData0)
		self.ax1.plot(self._dataClass.XData, self._dataClass.YData1)
		self.ax2.plot(self._dataClass.XData, self._dataClass.YData2)
		self.ax3.plot(self._dataClass.XData, self._dataClass.YData3)
		self.ax4.plot(self._dataClass.XData, self._dataClass.YData4)
		self.ax5.plot(self._dataClass.XData, self._dataClass.YData5)
		self.ax6.plot(self._dataClass.XData, self._dataClass.YData6)
		self.ax7.plot(self._dataClass.XData, self._dataClass.YData7)
		self.ax8.plot(self._dataClass.XData, self._dataClass.YData8)
		self.ax9.plot(self._dataClass.XData, self._dataClass.YData9)
		self.ax10.plot(self._dataClass.XData, self._dataClass.YData10)
		self.ax11.plot(self._dataClass.XData, self._dataClass.YData11)
		self.ax12.plot(self._dataClass.XData, self._dataClass.YData12)
		self.ax13.plot(self._dataClass.XData, self._dataClass.YData13)


class MyDataFetchClass(threading.Thread):

	def __init__(self, dataClass, cortex):

		threading.Thread.__init__(self)
		self._dataClass = dataClass
		self._period = 0.05
		self._nextCall = time.time()
		self._cortex = cortex


	def run(self):
		NbDotMax = 100
		while True:
			new_data = self._cortex.ws.recv()        
			#print(new_data)
			flux = json.loads(new_data)
			if 'eeg' in flux.keys():
				chan = np.array(flux['eeg'][2:16])
				chan = chan.T
				chan.reshape(14,1)
				print(chan.shape)
				if len(self._dataClass.XData) > 100:
					self._dataClass.YData0.pop(0)
					self._dataClass.YData1.pop(0)
					self._dataClass.YData2.pop(0)
					self._dataClass.YData3.pop(0)
					self._dataClass.YData4.pop(0)
					self._dataClass.YData5.pop(0)
					self._dataClass.YData6.pop(0)
					self._dataClass.YData7.pop(0)
					self._dataClass.YData8.pop(0)
					self._dataClass.YData9.pop(0)
					self._dataClass.YData10.pop(0)
					self._dataClass.YData11.pop(0)
					self._dataClass.YData12.pop(0)
					self._dataClass.YData13.pop(0)
				else:
					self._dataClass.XData.append(self._dataClass.XData[-1] + 1)
				self._dataClass.YData0.append(chan[0])
				self._dataClass.YData1.append(chan[1])
				self._dataClass.YData2.append(chan[2])
				self._dataClass.YData3.append(chan[3])
				self._dataClass.YData4.append(chan[4])
				self._dataClass.YData5.append(chan[5])
				self._dataClass.YData6.append(chan[6])
				self._dataClass.YData7.append(chan[7])
				self._dataClass.YData8.append(chan[8])
				self._dataClass.YData9.append(chan[9])
				self._dataClass.YData10.append(chan[10])
				self._dataClass.YData11.append(chan[11])
				self._dataClass.YData12.append(chan[12])
				self._dataClass.YData13.append(chan[13])
				self._nextCall = self._nextCall + self._period;
				time.sleep(self._nextCall - time.time())
			# print(".")