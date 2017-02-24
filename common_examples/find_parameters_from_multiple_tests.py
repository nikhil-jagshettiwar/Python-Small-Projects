import os
import csv
import pdb
import argparse 

class TestEngine:
	def __init__(self,args):
		self.Main_List = {}
		self.Test_count = 0

		self.Test_Name_File_Path = args['Test_Name_File_Path']
		self.Out_Report_Name = args['Out_Report_Name']
 
		
	def csv_create(self,):
		header_data = ['Parameter_Name','Count_occurs', 'Percentage', 'Param_Range', 'missing_values', 'Values']
		self.CSV_File = open(self.Out_Report_Name, 'w')
		self.csv_DictP = csv.DictWriter(self.CSV_File ,header_data)
		self.csv_DictP.writeheader()
	def csv_write(self,):
	
		#ordering the dictonary as per Percentage 
		from collections import OrderedDict
		OrderedDict(sorted(self.Main_List.iteritems(), key=lambda x:x[1]['param_count']))

		for param_name in OrderedDict(sorted(self.Main_List.iteritems(), key=lambda x:x[1]['param_count'])):
			self.csv_DictP.writerow({'Parameter_Name':param_name, 'Count_occurs' : self.Main_List[param_name]['param_count'],'Percentage':self.Main_List[param_name]['param_per'], 'Param_Range':self.Main_List[param_name]['Param_Range'], 'missing_values':self.Main_List[param_name]['Param_missing_vals'], 'Values': self.Main_List[param_name]['param_value']})
		
	def csv_close(self,):
		self.CSV_File.close()

	def Get_percentage_n_Param_Range(self):
		execption = ['encbitrate','binflex','binlimit','src_w','src_h','bitlimit','srccropright','cabac_bin_flex_over','vcm_target_hyst','vcm_target_const','req_priority_decr','maxslicesize','CSCMaxClip','scaler_coeff_regs', 'ssqe_gamma_lo','sahd_gamma_lo','mmuStride','vcm_target_block_size','req_priority_thresh', 'enc_w','enc_h','startframe','src_stride','recon_gamma_lo','sad_beta_lo','recon_beta_hi','ssqe_gamma_hi','sahd_beta_hi','ssqe_beta_lo','ssqe_beta_hi','sad_beta_hi','recon_beta_lo','sahd_gamma_hi','sahd_beta_lo','ssqe_gamma_vlow','sahd_gamma_lo','sad_gamma_lo','sad_gamma_hi','recon_gamma_hi', 'ssqe_beta_vlow','maxsliceCTUs']  
		for param_name in self.Main_List:
			param_percentage=( float(self.Main_List[param_name]['param_count'])/self.Test_count)*100
			self.Main_List[param_name]['param_per'] = param_percentage

			length = len(self.Main_List[param_name]['param_value'])
			self.Main_List[param_name]['Param_Range'].append(self.Main_List[param_name]['param_value'][0])
			self.Main_List[param_name]['Param_Range'].append(self.Main_List[param_name]['param_value'][length-1])
			
			from_num = self.Main_List[param_name]['Param_Range'][0]
			to_num = self.Main_List[param_name]['Param_Range'][1]
			temp_param = self.Main_List[param_name]['param_value']
			self.missing_list = []
			#if isinstance(from_num, int) and isinstance(to_num, int) and (param_name != "encbitrate") and (param_name != "binflex") and (param_name != "binlimit") and (param_name != "src_w") and (param_name != "src_h") and (param_name != "bitlimit")  and (param_name != "srccropright") and (param_name != "cabac_bin_flex_over") and (param_name != "vcm_target_hyst") and (param_name != "vcm_target_const") and (param_name != "req_priority_decr") and (param_name != "maxslicesize") and (param_name != "startframe"):
			 
			if isinstance(from_num, int) and param_name not in execption:
				#print param_name
				#print 'from_num',from_num
				#print 'to_num',to_num
				for param_val in range(from_num, to_num):
					if param_val not in temp_param:
						self.missing_list.append(param_val)
			self.Main_List[param_name]['Param_missing_vals'].extend(self.missing_list)
			
			
	def test(self,):
		with open (self.Test_Name_File_Path, 'r') as F:
			F_data = F.read()
			for line in F_data.split('\n'):
				if 'srcyuv' in  line:
					self.process_line(line)	
					self.Test_count += 1
					
	
			self.Get_percentage_n_Param_Range()
			self.csv_create()
			self.csv_write()
			self.csv_close()
			
			
	def process_line(self,line):
		i = 0
		param_data = line.split(' ')

		while i < len(param_data):
			if param_data[i].startswith('-'):
				param_name = param_data[i][1:] # Will be getting the parameter name

				i+=1	#Will be getting the value of the parameter now #H264, -36, 34523434, 
				param_value = None
				if param_data[i].startswith('-'):
					if param_data[i][1:].isdigit():
						param_value = param_data[i]
				
				elif param_data[i].isdigit() or param_data[i].isalnum():
					param_value = param_data[i]
				
				elif param_data[i].startswith('-'):
					if param_data[i][1:].isalnum():
						param_value = None
						continue
						#i = i - 1 # we got the  second parameter 
				else:
					param_value = param_data[i]
				
				#print line
				self.Update_dict(param_name,param_value)
				
			i += 1
				
				

	def Update_dict(self,param_name,param_value):
		
		if param_value and (param_value.startswith('-')  or param_value.isdigit()):
			param_value = int(param_value)

		if not self.Main_List.has_key(param_name):
			self.Main_List.update({param_name: {'param_value':[param_value], 'param_count': 0, 'param_per':None, 'Param_Range':[], 'Param_missing_vals':[]}})

		else:
			if not param_value in self.Main_List[param_name]['param_value']:
				self.Main_List[param_name]['param_value'].append(param_value)

				if isinstance(param_value, int):
					#print 'param_name', self.Main_List[param_name]
					#print 'param_value:', self.Main_List[param_name]['param_value']
					self.Main_List[param_name]['param_value'].sort(key=int)
						
						

		self.Main_List[param_name]['param_count']+=1



	

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description = "Script is used to Generate the report of  the parameter status which goes in for the Random Test")
	parser.add_argument("--Test_Name_File_Path"	, dest = "Test_Name_File_Path"	, required = True, help = "Give the Test name set file path")
	parser.add_argument("--Out_Report_Name"	, dest = "Out_Report_Name"	, required = True, help = "Set the out Report path")


	
	args = vars(parser.parse_args())
	
	print args['Test_Name_File_Path']
	if not os.path.exists(args['Test_Name_File_Path']):
		print "Test_Name_File_Path path doesn't exist"
		exit()
	

	A = TestEngine(args)
	A.test()
	
	
