import os, json

def init_aws_creds():
    creds = json.load("aws.json")
    os.environ["AWS_ACCESS_KEY_ID"] = creds["accesskey"]
    os.environ["AWS_SECRET_ACCESS_KEY"] = creds["secretkey"]
    
    

