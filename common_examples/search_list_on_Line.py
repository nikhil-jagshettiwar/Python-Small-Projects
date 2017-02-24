import csv
import pdb

OutPut_file = 'out_report_latest.csv'
Input_Feature_List='driver_coverage_param_updated.txt'

Command_list_files = 'Latest_Feature_Test_command_lines.txt'

Feature_List = open(Input_Feature_List, 'r').readlines()
CSV_File = open(OutPut_file, 'w')

#Feature_List = open("driver_coverage_param_updated.txt", 'r').readlines()
#CSV_File = open('Quartz_final_driver.csv', 'w')



header_data = ['Feature_Name','Count_occurs']
csv_DictP = csv.DictWriter(CSV_File ,header_data)
csv_DictP.writeheader()


with open (Command_list_files,'r') as F:
	F_Data = F.read()
	#pdb.set_trace()
	for x in Feature_List:
		Counter = 0
		x = x.replace('\n',' ')
		for line in F_Data.split('\n'):
			if x in line:
				Counter+=1
		
		print 'Feature_Name: ',x, 'Count_occurs: ', Counter
		csv_DictP.writerow({'Feature_Name':x, 'Count_occurs' : Counter})
		
		
		
		
	


