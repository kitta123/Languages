import requests,json

#base_url="https://13.127.198.209:5000/services/api/v0/"

def get_token(server_ip):
	base_url="https://"+server_ip+":5000/services/api/v0/"
	data={
		"username":"admin",
		"password":"admin"
	}
	r = requests.post(base_url+"login",data=json.dumps(data),verify=False)
	
	#print(r.text)
	r=json.loads(r.text)
	#print(r["token"])
	return(r["token"])

def nodes_get(server_ip,end_point):
	q={}
	base_url= "https://"+server_ip+":5000/services/api/v0/"
	r=get_token(server_ip)
	q["x-access-token"]=r
	#return(q)
	r = requestdata={  
		"host_identifier":"4C4C4544-004B-4D10-804E-CAC04F354253",
		"tags":"dhanyashree"
	}
	r = requests.get(base_url+end_point,headers=q,verify=False)
	if r.status_code==200:
		r=json.loads(r.text)
		if r['status']=='success':return  'success'
	
	return('fail')
a=[]

'''def nodes_get(server_ip,end_point):
	q={}data={  
		"host_identifier":"4C4C4544-004B-4D10-804E-CAC04F354253",
		"tags":"dhanyashree"
	}

	base_url= "https://"+server_ip+":5000/services/api/v0/"
	r=get_token(server_ip)
	q["x-access-token"]=r
	#return(q)
	r = requests.get(base_url+end_point,headers=q,verify=False)
	if r.status_code==200:
		r=json.loads(r.text)
	for data in r['data']:
		print(data)
		for key in data:
			print(type(data[key]))
			if type(data[key])==int:
				if data[key]!='None':
					print('succ')
			
			elif type(data[key])==str:
				if data[key]!='None':
					#print(data[key])
					print('succ')
									
			elif type(data[key])==list:
				for j in data[key]:
					#print(type(j))
					#print(j)
					if type(j)==str:
						if data[key]!='None':
							print('succ')
					elif type(j)==dict:
						for value in j:
							#print(j[value])
							if j[value]!='None':
								print('not None')
			elif type(data[key])==dict:
				for key,value in data.items():
					print(value)
					if type(value)==str:
						if value!='None':
							print('succ')
					elif type(value)==dict:
						for j in value:
							#print(value[j])
							if value[j]!='None':
								print('not None')
					elif type(data[key])==list:
						for j in data[key]:
						#print(type(j))
						#print(j)
							if type(j)==str:
								if data[key]!='None':
									print('succ')
							elif type(j)==dict:
								for value in j:
									#print(j[value])
									if j[value]!='None':
										print('not None')'''
			
			
	
	
	


def query_get():
	q={}
	r=get_token()
	q["x-access-token"]=r
	#return(q)
	r = requests.get(base_url+"quaries",headers=q,verify=False)
	if r.status_code==200:
		r=json.loads(r.text)
		if r['status']=='success':return  'success'
	return('fail')

#for i in data[key]:
	#print(i)

def packs_get():
	q={}
	r=get_token()
	q["x-access-token"]=r
	#return(q)
	r = requests.get(base_url+"packs",headers=q,verify=False)
	return(r)


def tags_post(server_ip,end_point):
	q={}
	base_url= "https://"+server_ip+":5000/services/api/v0/"
	r=get_token(server_ip)
	q["x-access-token"]=r
	data={  
		"host_identifier":"4C4C4544-004B-4D10-804E-CAC04F354253",
		"tags":"dhanyashree"
	}
	r = requests.post(base_url+end_point,data=json.dumps(data),headers=q,verify=False)
	if r.status_code==200:
		r=json.loads(r.text)
		if r['status']=='success':return  'success'
	return('fail')
	

def carves_post():
	q={}
	r=get_token()
	q["x-access-token"]=r
	data={
		"host_identifier":"4C4C4544-004B-4D10-804E-CAC04F354253"
	}
	r = requests.post(base_url+"carves",data=data,headers=q,verify=False)
	return(r)

def hunt_post():
	q={}
	r=get_token()
	q["x-access-token"]=r
	#f_md = open("/home/asm/Dhanya/doc_com.md5","rb")
	data={
		
		"file" : open("/home/asm/Related to polylogyx/sample.md5","r+"),
		"type" : "md5"
	}
	r = requests.post(base_url+"hunt-upload",files=data,data=data,headers=q,verify=False)
	#texts = json.loads(r.text)
	return (r)
def carves_get():
	q={}
	r=get_token()
	q["x-access-token"]=r
	data={
		"host_identifier":"4C4C4544-004B-4D10-804E-CAC04F354253"
	}
	r = requests.get(base_url+"carves/download/OE5R2J1MZT",data=data,headers=q,verify=False)
	return(r)


def change_pass():
	q={}
	r=get_token()
	q["x-access-token"]=r
	data={
		"old_password":"admin",
		"new_password":"admin123",
		"confirm_new_password":"admin123"
	}
	r = requests.post(base_url+"changepw",data=data,headers=q,verify=False)
	return(r)
def log_out():
	q={}
	r=get_token()
	q["x-access-token"]=r
	r = requests.post(base_url+"logout",headers=q,verify=False)
	return(r)

def api_keys_get():
	q={}
	r=get_token()
	q["x-access-token"]=r
	r = requests.get(base_url+"apikeys",headers=q,verify=False)
	return(r)

def certi(server_ip,end_point):
	q={}
	base_url= "https://"+server_ip+":5000/services/api/v0/"
	r=get_token(server_ip)
	q["x-access-token"]=r
	r = requests.get(base_url+end_point,headers=q,verify=False)
	if r.status_code==200:
		print(r.content)
		with open('/home/asm/sim1.txt', 'wb') as f:
			f.write(r.content)
		with open('/home/asm/sim1.txt', 'r') as f:
			lines = f.readlines()
		return(lines)

	
def cpt_get():
	q={}
	r=get_token()
	q["x-access-token"]=r
	r = requests.get(base_url+"cpt/ubuntu",headers=q,verify=False)
	with open('/home/asm/sim1.txt', 'wb') as f:
		f.write(r.content)
	with open('/home/asm/sim1.txt', 'r') as f:
		lines = f.readlines()
	return(lines)

def car_get():
	q={}
	r=get_token()
	q["x-access-token"]=r
	r = requests.get(base_url+"carves/download/XMB0UD1HGC",headers=q,verify=False)
	
	return(r)



#n=nodes_get("13.127.198.209","nodes")
#print('nodes information', n)
#print("query information",r.text)
#p=packs_get()
#print("packs information",p.text)
#t=tags_post("13.127.198.209","tags/add")
#print("tags information" ,t)
#c=carves_post()
#print("carves information" ,c.text)
#h=hunt_post()
#print("Hunt information" ,h.text)
#c=carves_get()
#print("carves information" ,c.text)
#passw=change_pass()
#print("password ",passw)

#l=log_out()
#print("logout",l)
#A=api_keys_get()
#A=json.loads(A.text)
#print("file",A)

#cer=certi("13.127.198.209","certificate")
#for data in cer:
#	print(data)
#cer=cpt_get("13.127.198.209","nodes")
#for data in cer:
#print(cer)
#car=car_get()
#print(car)
	

