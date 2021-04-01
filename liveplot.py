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
		self.YData0 = [4320]
		self.YData1 = [4320]
		self.YData2 = [4320]
		self.YData3 = [4320]
		self.YData4 = [4320]
		self.YData5 = [4320]
		self.YData6 = [4320]
		self.YData7 = [4320]
		self.YData8 = [4320]
		self.YData9 = [4320]
		self.YData10 = [4320]
		self.YData11 = [4320]
		self.YData12 = [4320]
		self.YData13 = [4320]


class MyPlotClass():

	def __init__(self, dataClass):

		self._dataClass = dataClass

		# self.hLine, = plt.plot(0, 0)

		self.ani = FuncAnimation(plt.gcf(), self.run, interval = 50, repeat=True)


	def run(self, i):
		# print(self._dataClass.XData)
		# print("data =",len(self._dataClass.YData[0]))
		# self.hLine.set_data(self._dataClass.XData, self._dataClass.YData3)
		# self.hLine.axes.relim()
		# self.hLine.axes.autoscale_view()
		plt.cla()
		plt.plot(self._dataClass.XData, self._dataClass.YData0)
		plt.plot(self._dataClass.XData, self._dataClass.YData1)
		plt.plot(self._dataClass.XData, self._dataClass.YData2)
		plt.plot(self._dataClass.XData, self._dataClass.YData3)
		plt.plot(self._dataClass.XData, self._dataClass.YData4)
		plt.plot(self._dataClass.XData, self._dataClass.YData5)
		plt.plot(self._dataClass.XData, self._dataClass.YData6)
		plt.plot(self._dataClass.XData, self._dataClass.YData7)
		plt.plot(self._dataClass.XData, self._dataClass.YData8)
		plt.plot(self._dataClass.XData, self._dataClass.YData9)
		plt.plot(self._dataClass.XData, self._dataClass.YData10)
		plt.plot(self._dataClass.XData, self._dataClass.YData11)
		plt.plot(self._dataClass.XData, self._dataClass.YData12)
		plt.plot(self._dataClass.XData, self._dataClass.YData13)


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