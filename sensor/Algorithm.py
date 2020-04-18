import communication_module
import sensor
print('Algorithm1')

for val in communication_module.Sersor_Stream('temperature'):
	print (val)