# Table DDL Export From CIM Json Files
Pyton script creates postgresql table ddl from cim



This script tested with Python3.
It uses Json library. Please install the json library before execute.
The script version is Alfa now.

The Script creates Table DDL's with Foreign Keys.
So, When you execute the output SQL file, It can give some errors because of foreign keys.
The table create DDL's has 'IF NOT EXIST' condition. You need to execute DDL's a few times.

CIM Json files uses some PostgreSQL Reserved words for column names. That's why I remap and added _ char to column names.

LoyaltyAccount table has duplicated column name for "href". After generate DDL file, you need to change column name to one of them.



    # [parseDDL]#
    # [parseDDL]#
    # [parseDDL]# ls -lrth
    # drwxr-xr-x 8 root root  138 Mar 20 06:29 CIM-Data-Dictionary-master
    # -rw-r--r-- 1 root root 3.4K Apr  1 04:34 generate_ddl_from_json.py
    # [parseDDL]#
    # [parseDDL]#
    # [parseDDL]# ls CIM-Data-Dictionary-master/docs/*json | wc -l
    # 624
    # [parseDDL]#
    # [parseDDL]# python3 generate_ddl_from_json.py
    # [parseDDL]#
    # [parseDDL]# ls -lrth
    # total 452K
    # drwxr-xr-x 8 root root  138 Mar 20 06:29 CIM-Data-Dictionary-master
    # -rw-r--r-- 1 root root 3.4K Apr  1 04:34 generate_ddl_from_json.py
    # -rw-r--r-- 1 root root 235K Apr  1 04:41 CIM-Table-DDL-20200401044129.sql
    # [parseDDL]#
    # [parseDDL]# wc -l CIM-Table-DDL-20200401044129.sql
    # 624 CIM-Table-DDL-20200401044129.sql
    # [parseDDL]#
    # [parseDDL]#


