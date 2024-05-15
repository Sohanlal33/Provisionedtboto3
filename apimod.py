#HTTP Req and HTTP Response 
#pip install request--import that module in file 


import requests 

response = requests.get("URL")  #Base URL of gitlab or git/users/ :user_id/projects
my_projects =response.json()  #we can use text or json --convert json to to python data type

for project in my-project:
    print(f"Project Name: {project['name']}\nProject url: {project['web_url']}\n") #dictionaries accessing object in dictionary