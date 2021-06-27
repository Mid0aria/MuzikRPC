import rpc
import time
import requests
import json

with open('userid.json') as f:
    data = json.load(f)
userid = data['userclientid']

print("RPC Bağlanılıyor")
client_id = 'clientid'  
rpc_obj = rpc.DiscordIpcClient.for_platform(client_id)
print("RPC Bağlantısı Başarılı.")

while True:
 url1 = f"gizliapilink" + userid
 f = requests.get(url1)
 rpcdetails = f.text.split('["')[1].split('"],')[0]
 rpcstate = f.text.split('müziksüresi":["')[1].split('"],')[0]
 rpcsmallimage = f.text.split('altlogo":"')[1].split('"}')[0]
 activity = {
            "details": rpcdetails,
            "state": rpcstate, 
            "assets": {
                "small_text": "Müzik RPC",  # anything you like
                "small_image": rpcsmallimage,  # must match the image key
                "large_text": "Müzik RPC",  # anything you like
                "large_image": "music"  # must match the image key
            }
        }
 rpc_obj.set_activity(activity)
 time.sleep(5)
