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



Version : 0.0.1

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



Version : 0.0.2
Table DDL and Constraint SQLs splitted.

    # [sqlexportfromjson]# 
    # [sqlexportfromjson]# ls -lrth
    # total 8.0K
    # drwxr-xr-x 8 root root  138 Apr  9 09:25 CIM-Data-Dictionary-master
    # -rw-r--r-- 1 root root 5.5K Apr 15 16:10 generate_ddl_from_json.py
    # [sqlexportfromjson]# 
    # [sqlexportfromjson]# python3 generate_ddl_from_json.py 
    # [sqlexportfromjson]# 
    # [sqlexportfromjson]# ls -lrth
    # total 648K
    # drwxr-xr-x 8 root root  138 Apr  9 09:25 CIM-Data-Dictionary-master
    # -rw-r--r-- 1 root root 5.5K Apr 15 16:10 generate_ddl_from_json.py
    # -rw-r--r-- 1 root root 164K Apr 15 16:11 CIM-Table-DDL-tbl-20200415161112.sql
    # -rw-r--r-- 1 root root 445K Apr 15 16:11 CIM-Table-DDL-const-20200415161112.sql
    # [sqlexportfromjson]# 
    # [sqlexportfromjson]# wc -l CIM-Table-DDL-tbl-20200415161112.sql 
    # 624 CIM-Table-DDL-tbl-20200415161112.sql
    # [sqlexportfromjson]# 
    # [sqlexportfromjson]# cat CIM-Table-DDL-const-20200415161112.sql |grep "ALTER TABLE" | wc -l
    # 2746
    # [sqlexportfromjson]# 
    # [sqlexportfromjson]# 

