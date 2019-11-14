Basic program to access mysql from java

Steps:
1. Install java
2. Install mysql
3. download mysql connector 
4. Set classpath to point to mysql connector
5. create database/tables/entries
6. Takebackup of database:

Commands:
- cd /Users/chnmish/sw/java
- export CLASSPATH=${CLASSPATH}:/Users/chnmish/Downloads/mysql-connector.jar
- javac JavaMysqlSelectExample.java
- java JavaMysqlSelectExample
- mysqldump --databases testdb -u root -p > ~/sw/java/db.sql

