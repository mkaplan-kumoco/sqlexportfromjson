#
# This script tested with Python3.
# It uses Json library. Please install the json library before execute.
# The script version is Alfa now.
#
# The Script creates Table DDL's with Foreign Keys.
# So, When you execute the output SQL file, It can give some errors because of foreign keys.
# The table create DDL's has 'IF NOT EXIST' condition. You need to execute DDL's a few times. 
#
# CIM Json files uses some PostgreSQL Reserved words for column names. That's why I remap and added _ char to column names.
#
# LoyaltyAccount table has duplicated column name for "href". After generate DDL file, you need to change column name to one of them.
#
# Mehmet Kaplan
# v0.0.1
# 

import json, os
from datetime import datetime

#directory = './docs'
directory = './CIM-Data-Dictionary-master/docs'
pDate = datetime.today().strftime('%Y%m%d%H%M%S')

def get_type(x):
    return {
        'integer': 'INT',
        'number': 'NUMERIC',
        'boolean': 'BOOLEAN',
        'string': 'VARCHAR(250)',
        'array': 'TEXT []',
        'object' : 'TEXT'        
    }.get(x, 'TEXT') 

def get_table(x):
    return {
        'desc'  : '_desc',
        'limit' : '_limit',
        'group' : '_group',
        'user'  : '_user',
        'unique': '_unique'
    }.get(x,x) 

def parse_column(ptype, pname):
  pResult=''
  if ptype =='$ref':
    pTempName= pname.split('#')[1]
    pResult=' integer  REFERENCES ' + pTempName + ' ( ' + pTempName.lower() +str('_id') +' ) '
  else:
    pResult=get_type(pname)  
  return pResult


def write_file (pLine) :
  with open('CIM-Table-DDL-' + str(pDate) + '.sql', 'a') as f:
    f.write(pLine)
    f.write('\n')
    f.close()   



def main():
  for filename in os.listdir(directory):
    if filename.endswith("json"):
        f = open(directory +"/"+ filename)
        docket_content = f.read()
        schema = json.loads(docket_content)
        pTableName=str(schema['title'])
        #print ('Table Name: ' + pTableName)
        pSQL='CREATE TABLE IF NOT EXISTS ' + pTableName +' ( ' + pTableName.lower() + '_id serial PRIMARY KEY '

        if schema.get('definitions').get(pTableName).get('properties') is not None:
          pTable=schema.get('definitions').get(pTableName).get('properties')
          for dtt in pTable:
             pColumn=pTable.get(dtt)
             drr = get_table(dtt.lower()).replace('-','_')
             if pColumn.get('type') is None:
               pType=pColumn.get('$ref')
               pSQL = pSQL + ' , ' + drr + ' ' + parse_column('$ref',pType)
             else:
               pType=pColumn.get('type')
               pSQL = pSQL + ' , ' + drr + ' ' + parse_column('type',pType)
        elif schema.get('definitions').get(pTableName).get('items') is not None:
          pTable=schema.get('definitions').get(pTableName).get('items').get('properties')
          for dtt in pTable:
             pColumn=pTable.get(dtt)
             drr = get_table(dtt.lower()).replace('-','_')
             if pColumn.get('type') is None:
               pType=pColumn.get('$ref')
               pSQL = pSQL + ' , ' + drr + ' ' + parse_column('$ref',pType) 
             else:
               pType=pColumn.get('type')
               pSQL = pSQL + ' , ' + drr + ' ' + parse_column('type',pType)
        #else:
        #   print (pTableName + '; ; ;')

        pSQL = pSQL + ' ) ;'
        write_file (pSQL)
        #print (pSQL)

if __name__ == "__main__":
    main()


