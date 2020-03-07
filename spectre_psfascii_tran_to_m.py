#!/usr/bin/python
stage = 1;
tran_result = {}
trace_cat = {}
with open('tran.tran.tran','r') as f:
	content = f.readlines()
	for line in content:
		if(line == "END\n"):
			break;

		if(stage == 1):
			if(line == "TRACE\n"):
				stage = 2;
				continue;
		elif(stage == 2):
			if(line == "VALUE\n"):
				stage = 3;
				continue;

			data = line.split(' ');
			#print(data[0][1:-1],data[1][0:-1])

			key = data[0][1:-1];
			val = data[1][1:-2];
			if(key not in trace_cat):
				trace_cat[key] = val
			else:
				print("ERROR   --> currently not supported: same name but in different type");
				break;

		elif(stage == 3):
			data = line.split(' ');
			#print(data[0][1:-1],data[1][0:-1])

			key = data[0][1:-1];
			val = data[1][0:-1];
			if(key not in tran_result):
				tran_result[key] = list()
			tran_result[key].append(val)
#print(tran_result)
#print(trace_cat)
emoji_list = [];
with open('emoji.txt','rb') as f:
	content = f.readlines();
	for line in content:
		#emoji_list.append(line.decode('utf8'));
		emoji_list.append(line);

with open('tran_result.m','w') as f:
	for key in tran_result:
		f.write(key.replace('.','_').replace(':','_') + " = [");
		for data in tran_result[key]:
			f.write(' '+data+' ');
		f.write("];\n");
print("psfascii format trans result --> matlab format is completed "+emoji_list[0]);
		
