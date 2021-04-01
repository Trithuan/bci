import key
import json
from cortex import Cortex
import matplotlib.pyplot as plt
import numpy as np
from liveplot import MyPlotClass, MyDataFetchClass, MyDataClass
import bci_workshop_tools as BCIw



print("licence :", key.licence)
print("client_id :", key.client_id)
print("client_secret :", key.client_secret)


user = {
	"license" : key.licence,
	"client_id" : key.client_id,
	"client_secret" : key.client_secret,
	"debit" : 10
}


cortex = Cortex(user, debug_mode=True)
cortex.do_prepare_steps()




streams = ['eeg']

print('subscribe request --------------------------------')


sub_request_json = {
	"jsonrpc": "2.0", 
	"method": "subscribe", 
	"params": { 
		"cortexToken": cortex.auth,
		"session": cortex.session_id,
		"streams": streams
	}, 
	"id": key.SUB_REQUEST_ID
}




cortex.ws.send(json.dumps(sub_request_json))


data = MyDataClass()
plotter = MyPlotClass(data)
fetcher = MyDataFetchClass(data, cortex)

fetcher.start()
plt.show()


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