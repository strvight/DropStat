import requests
import time
# url = 'https://api2.dropbase.io/v1/pipeline/run_pipeline'

# data = {
#     "token": "",
#     "fileUrl": ""
# }

# response = requests.post(url, data=data)

# jobID = response.text

# JobResponse = requests.get(url, headers={}, data={"job_id":jobID})
# print(JobResponse.text.encode('utf8'))


# url = "https://query.dropbase.io/dcn6xkbjv2al5fsm2kb7evr/TABLE_NAME"

# payload = {}
# headers = {
#   'Authorization': 'Bearer API TOKEN'
# }

# responseDB = requests.request("GET", url, headers=headers, data = payload)

# print(responseDB.text.encode('utf8'))

TOKEN = "QiNryDNGAFGpdD6wpfjfjp"

def get_status(job_id):
    # Call the server to get the status
    r = requests.get("https://api2.dropbase.io/v1/pipeline/run_pipeline", data={ "job_id":job_id })
    
    # Keep pinging the server until the job is finished
    while(r.status_code == 202):
        print(r.json()) # Prints the message of what is happening
        time.sleep(1)
        r = requests.get("https://api2.dropbase.io/v1/pipeline/run_pipeline", data={ "job_id":job_id})

    # id statys code is not 200 nor 202, then error occured
    if(r.status_code != 200):
        print("There is an error")
        print(r.status_code)
        print(r.json())
    
    else:
        print("Successful!")

def upload_via_url(file_url):
    # 
    r = requests.post("https://api2.dropbase.io/v1/pipeline/run_pipeline", data={'token': TOKEN, 'fileUrl': file_url})
    if(r.status_code != 200): # Something failed
        print(r.status_code)
        print(r.json()) # Detailed error message
    job_id = str(r.json()) # Extract job id
    return job_id

file_url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vRVUyvS42Ve0dj_q4LMrV71ZyO9_ScAm-Ctk_bVbfPD6mpVJkdYw-dY5O5eqo0QGlNI0kAwlbhKRPxt/pub?output=csv'
upload_via_url_id = upload_via_url(file_url)

get_status(upload_via_url_id)