import requests
import json
import argparse

class OrangeAPI:

    BASE_API = "https://contact-everyone.orange-business.com/api/v1.2/"
    URL_TOKEN = BASE_API + "oauth/token"
    URL_GROUPS = BASE_API + "groups"
    URL_DIFFUSION = BASE_API + "groups/%s/diffusion-requests"
    
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.authorization_header = {}
    
    def login(self):
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        params  = {'username': self.username, 'password': self.password}

        rq = requests.post(self.URL_TOKEN, data=params, headers=headers)
        if rq.status_code == 200:
            response_json = json.loads(rq.text)
            if 'access_token' in response_json:
                self.authorization_header = {
                    'authorization': "Bearer %s" % response_json['access_token']
                }
            else:
                raise requests.RequestException('Orange API: Access token not found')
        else:
            raise requests.RequestException('Orange API: Bad username or password (%s)', rq.status_code)
    
    def group_id_from_name(self, group_name):
        rq = requests.get(self.URL_GROUPS, headers=self.authorization_header)
        if rq.status_code == 200:
            groups = json.loads(rq.text)
            for group in groups:
                if group["name"] == group_name:
                    return group["id"]
        
        raise requests.RequestException("Group name not found: " + group_name)
       
    def send(self, group_name, destinations, message):
        self.login()
        group_id = self.group_id_from_name(group_name)

        headers = {"content-type": "application/json"}
        headers.update(self.authorization_header)
    
        payload = json.dumps(
            {
                "name":"Send a SMS from passerelle",
                "msisdns":destinations,
                "smsParam":{
                    "encoding": "GSM7",
                    "body": message
                }
            })
        
        rq = requests.post(self.URL_DIFFUSION % group_id, data=payload, headers=headers)
        if rq.status_code == 201:
            return json.loads(rq.text)
        
        raise Exception("Send SMS failed %s, %s" % (rq.status_code, rq.text))
       
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--username")
    parser.add_argument("--password")
    parser.add_argument("--groupname")
    parser.add_argument("--mobile")
    parser.add_argument("--message")
    args = parser.parse_args()

    api = OrangeAPI(args.username, args.password)
    api.send(args.groupname, [args.mobile], args.message)
