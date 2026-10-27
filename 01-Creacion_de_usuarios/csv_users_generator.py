import os
import json
import csv
from unidecode import unidecode
import secrets
import string

def new_users(file,csvfile):
    email_ext = '@empresa.com'

#### Open json file to read the contents.
    with open(file,'r',encoding='utf-8') as txt:
        content = txt.read()

#### Separate names and last names to work better with complex names.
        new_content = json.loads(content)       
        full_names = []
        for my_list in new_content:
            for k,v in my_list.items():
                if k == 'nombre':
                    names = v.lower().lstrip()
                if k == 'apellidos':
                    surnames = v.lower().lstrip() 
            full = names + '/' + surnames
            full_names.append(full)
        total = len(full_names)

#### Check if folder exists. Create folder and csv file.
        if not os.path.isdir('CSV_Files'):
            os.mkdir('CSV_Files')
        path = os.path.dirname('CSV_Files')
        os.chdir('CSV_Files')
        h = ['Name','Surname','sAMAccountName','Password','Email']
            
    with open(csvfile,'w',newline='',encoding='utf-8') as f:
        data = csv.DictWriter(f,fieldnames = h)
        data.writeheader()
        my_count = {}
    
#### Create variables for names and last names to add them to the csv file.
        for n in full_names:
            sep = n.split('/')
            name = sep[0].strip()
            surname = sep[1].strip()                
#### Usernames.
            username_join = name[0] +'.' + surname.replace(' ','').replace("'",'')
            username = unidecode(username_join)
#### Check if any username is duplicated.
            if username not in my_count:
                my_count[username] = 0
            else:
                my_count[username] += 1
                username = f'{username}{my_count[username]}'
#### Generate secure random passwords using 'secrets' module.
            char = string.ascii_letters + string.digits
            length = 16
            passwd = ''.join(secrets.choice(char) for i in range(length))
#### Generate corporate emails.
            email = username + email_ext

#### Add data to csv file.
            data.writerow({'Name':name,'Surname':surname,'sAMAccountName':username,'Password':passwd,'Email':email}) 

    return f'{total} new employees have been added to {csvfile}.'

print(new_users('employees_list.json','users.csv'))