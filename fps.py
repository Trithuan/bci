import key
import json
from cortex import Cortex
import matplotlib.pyplot as plt
import numpy as np
from liveplot import MyPlotClass, MyDataFetchClass, MyDataClass
import bci_workshop_tools as BCIw
from IPython.core.pylabtools import figsize
import time


print("licence :", key.licence)
print("client_id :", key.client_id)
print("client_secret :", key.client_secret)


cortex = Cortex(key.user, debug_mode=True)
cortex.do_prepare_steps()
streams = ['eeg']
print('subscribe request --------------------------------')
cortex.ws.send(json.dumps(key.sub_request_json))



while True:
	start_time = time.time()
	new_data = cortex.ws.recv()
	flux = json.loads(new_data)
	if 'eeg' in flux.keys():
		print("FPS: ", 1.0 / (time.time() - start_time))



#affichage

# data = MyDataClass()
# plt.figure(figsize=(12,8))
# plotter = MyPlotClass(data)
# fetcher = MyDataFetchClass(data, cortex)

# fetcher.start()
# plt.show()
















# save = []


# if 'sys' in streams:
# 	new_data = cortex.ws.recv()
# 	# print(json.dumps(new_data, indent=4))
# 	# print('\n')
# else:
# 	while True:
# 		new_data = cortex.ws.recv()        
# 		#print(new_data)
# 		flux = json.loads(new_data)
# 		if 'eeg' in flux.keys():
# 			save.append(flux['eeg'][2:16])
# 			print(flux['eeg'])