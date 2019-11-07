*** Settings ***
Library   /home/asm/projects/python/robot/conn_ua_ser.py
*** Variables ***
${base_url}=   "https://13.127.198.209:5000/services/api/v0/"
${server_ip}=  13.127.198.209
${i}
*** Test Cases ***
Testcase1
   ${cal}=  get method   nodes

Testcase2
   ${cal}=  post method  apikeys	
 
Testcase3
   ${cal}=  get method for files   certificate	
	Log To Console   ${cal}

*** Keywords ***
get method 
	[Arguments]  ${end_point}
	${cal_result}=  nodes_get  ${server_ip}  ${end_point}
	Log To Console   ${cal_result}
	Should Be Equal  ${cal_result}   success
	[return]  ${cal_result}  
	
post method
	[Arguments]  ${end_point}
	${cal_result}=  tags_post  ${server_ip}  ${end_point}
	Log To Console   ${cal_result}
	Should Be Equal  ${cal_result}   success
	[return]  ${cal_result}  

get method for files
	[Arguments]  ${end_point}
	${cal_result}=  certi   ${server_ip}   ${end_point}
	[return]  ${cal_result}
	
 		  
