# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 14:16:57 2019

@author: kisho_lhokk3h
"""


import json
import requests
import config
import pandas as pd
from pandas.io.json import json_normalize
import matplotlib.pyplot as plt


api_url_base = 'https://www.pivotaltracker.com'
api_token = 'TestToken'
project_id='2346358'

project_id=   '2239994' #PM 
pivotal_users = {}

    


  
  
def get_token() :  
 
      #https://www.pivotaltracker.com/n/projects/2239994/stories/163787033
      #/projects/$PROJECT_ID/stories/559"
      
    auth_url =  'https://www.pivotaltracker.com/services/v5/me'
    
    response = requests.get(auth_url, auth=(config.username,config.password ))
    if  (response.status_code == 200 ) :
        api_token = json.loads(response.text)['api_token']
#        print('\napi_token: ' + api_token)
#        print('\n\n')
        data = response.content.decode('utf-8')
        json_data = json.loads(data)
        pivotal_users.update({json_data.get('id'):json_data.get('name')})
        return api_token
    else:
        return None

 


# To find the values. 

def get_users():
    #api_token= get_token()  
    url = 'https://www.pivotaltracker.com/services/v5/my/people?project_id='
    url = url + project_id
    print(url)

    
    headers = {"X-TrackerToken": api_token}
   
    response = requests.get(url, headers=headers)
    print('\n\n *** response.status_code : ' + str(response.status_code))
    if response.status_code == 200:
        
       
        data = response.content.decode('utf-8')
        json_data = json.loads(data)
        for account in json_data: 
            print( str(account.get('person').get('id')) + " , " +account.get('person').get('name'))
            pivotal_users.update({account.get('person').get('id'):account.get('person').get('name')})
        return "OK"
    else:
        return None  


def call():
    api_token= get_token()  
    url = 'https://www.pivotaltracker.com/services/v5/projects/2346358'
    url = 'https://www.pivotaltracker.com/services/v5/projects/2346358/stories/165907368'
    #url = 'https://www.pivotaltracker.com/services/v5/projects/2346358/stories'
    
    
    headers = {"X-TrackerToken": api_token}
    #headers = {'X-TrackerToken:'  + api_token + " . Content-Type": "application/json"}
    response = requests.get(url, headers=headers)
    print('\n\n *** response.status_code : ' + str(response.status_code))
    if response.status_code == 200:
        
       
      
        
        print('\n\n')
        json_data = json.loads( response.content.decode('utf-8'))
        print(json_data)
        print(type(json_data))
        #len = json_data.len()
        keys = json_data.keys()
        
        print(len)
        print('\n\n')
        for keyVal in keys: 
            print(keyVal + " : " + str(json_data[keyVal]))
            #print(key + " : ")
        
        
        
        #print('\n\n kind ' + response.kind)
       
        
        return "OK"
    else:
        return None
    
    
def get_story(story_id):
    api_token= get_token()  
#    url = 'https://www.pivotaltracker.com/services/v5/projects/2346358/stories/'
 #   url = 'https://www.pivotaltracker.com/services/v5/my/people?project_id='
    url = 'https://www.pivotaltracker.com/services/v5/projects/'
    url = url + project_id + '/stories/'
    project_id
    url =  url + str(story_id)
   
    
    
    headers = {"X-TrackerToken": api_token}
    #headers = {'X-TrackerToken:'  + api_token + " . Content-Type": "application/json"}
    response = requests.get(url, headers=headers)
    print('\n\n *** response.status_code : ' + str(response.status_code))
    if response.status_code == 200:
        
       
      
        
        print('\n\n')
        json_data = json.loads( response.content.decode('utf-8'))
        print(json_data)
        print(type(json_data))
        #len = json_data.len()
        keys = json_data.keys()
        
        print(len)
        print('\n\n')
        for keyVal in keys: 
            print(keyVal + " : " + str(json_data[keyVal]))
            #print(key + " : ")
        
        
        
        #print('\n\n kind ' + response.kind)
       
        
        return "OK"
    else:
        return None
    
def get_stories():
    api_token= get_token()  
#    url = 'https://www.pivotaltracker.com/services/v5/projects/2346358/stories'
    url = 'https://www.pivotaltracker.com/services/v5/projects/'
    url = url + project_id + '/stories/'
    story_list = []
    
    
    headers = {"X-TrackerToken": api_token}
   
    response = requests.get(url, headers=headers)
    print('\n\n *** response.status_code : ' + str(response.status_code))
    if response.status_code == 200:
        
       
        data = response.content.decode('utf-8')
        json_data = json.loads(data)
        
        print('Developer   Story Name      points       Labels ')
        print('------------------------------------------------')
        for story in json_data: 
            story_item =[]
#            print(story['name'] + " , " + str(story['owner_ids']) + " , " + str(story['story_type']) ) 
            if ( str(story['story_type']) == 'feature') :
#                 print(story['estimate'] )
                 # print owner name
                 ids = story['owner_ids']
#                 print(len(ids))
                 if (len(ids)) >1 :
                     id = story['owner_ids'][len(ids)-1]
                 elif (len(ids)) == 1 :
                     id = story['owner_ids'][0]
#                 print('\n id ' + str(id))
#                 print(pivotal_users.get((id)))
                 
                 labels = story['labels']
                 labels_string = '  '
                 labels_List =[]
                 sprint_label =''
                 for label in labels:
                     labels_string = labels_string + label.get('name') + ' ' 
                     
                     
                 if 'estimate' in story:
#                     print(str(pivotal_users.get(id))  + " " + str((story['name'])) + "   " + str((story['estimate'])) +labels_string)
                     story_item = [pivotal_users.get(id),story['name'], story['estimate'  ]]
#                     for label in labels:
#                         story_item.append( label.get('name')  )
#                     story_item.append(labels_List)
                     story_list.append(story_item)
                     print(story_list)
                 else :
                     print(pivotal_users.get(id)) 
                     
        
        df = pd.DataFrame(story_list, columns =['Developer', ' Story', 'Points'])
            
#            print(story['name'] + " , " + str(story['owner_ids']) + " , "  ) 
        print(df)    
        return df
    else:
        return None
    
#165907368
#https://www.pivotaltracker.com/services/v5/my/people?project_id=2346358
    

#print(get_story(165907368))
#print(get_stories())
# get token
api_token= get_token()          
get_users()
df = get_stories()
plot_data = df["Points"].groupby(df["Developer"]).sum()
#plot_data.sort_values()[-10:].plot(kind='bar')
plot_data.plot(kind='bar')
plt.title('Story Points summary')
plt.ylabel('Point')
plt.xticks(rotation=401)
plt.grid(True)
plt.Axes.invert_yaxis(self) 
plt.show()
#print(api_token)
#print(pivotal_users.get(2968151))

   