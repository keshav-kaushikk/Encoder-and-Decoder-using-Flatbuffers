import os
import sys

import flatbuffers
import Clnt.Person
import Clnt.Group
import Clnt.Client_Type
import Clnt.Client
import Clnt.Clients

# opening binary file
with open('bin/fb_bytes.bin', mode='rb') as binary_file:
	data = binary_file.read()

# storing data in clients
clients = Clnt.Clients.Clients.GetRootAsClients(data, 0)

for i in range(clients.ClientsLength()):
	
	# Printing Clients
	print('Client number: ',i+1)
	print('Name: ', clients.Clients(i).Name().decode('utf-8')) 
	

	if clients.Clients(i).TypeType() == Clnt.Client_Type.Client_Type().Person: 	
		person = Clnt.Person.Person()
		person.Init(clients.Clients(i).Type().Bytes, clients.Clients(i).Type().Pos)
		print('Age: ', person.Age())
		print('Weight: ', person.Weight())
		print('Gender: ', end='') 
		if person.IsMale() == True: 
			print('Male')
		else:
			print('Female')

	elif clients.Clients(i).TypeType() == Clnt.Client_Type.Client_Type().Group:
		group = Clnt.Group.Group()
		group.Init(clients.Clients(i).Type().Bytes, clients.Clients(i).Type().Pos)
		print('Average age: ', group.AvgAge())
		print('Average weight: ', group.AvgWeight())
		print('Group member names: ')
		for j in range(group.ParticipantNamelistLength()):
			print (group.ParticipantNamelist(j).decode('utf-8'))
	print('')

exit()