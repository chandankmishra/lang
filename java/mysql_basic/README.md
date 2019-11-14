Basic program to access mysql from java

Steps:
1. Install java jdk
2. Install mysql
3. Download mysql connector 
- download the jar file mysql-connector.jar
- https://www.javatpoint.com/example-to-connect-to-the-mysql-database
4. Set classpath to point to mysql connector
5. Create database/tables/entries
6. Takebackup of database:
- mysqldump --databases testdb -u root -p > ~/sw/java/db.sql

Commands to Run:
- cd /Users/chnmish/sw/java
- export CLASSPATH=${CLASSPATH}:/Users/chnmish/Downloads/mysql-connector.jar
- javac JavaMysqlSelectExample.java
- java JavaMysqlSelectExample


bash-3.2$ mysql -u root -p

mysql> use testdb;

mysql> select * from users;
+----+------------+-----------+---------------------+----------+------------+
| id | first_name | last_name | date_created        | is_admin | num_points |
+----+------------+-----------+---------------------+----------+------------+
|  1 | Fred       | Flinstone | 2019-11-13 22:08:12 |        0 |      10000 |
|  2 | Chandan    | Mishra    | 2019-11-13 23:24:03 |        0 |      20000 |
|  3 | Veena      | Mishra    | 2019-11-13 23:24:31 |        1 |      20000 |
+----+------------+-----------+---------------------+----------+------------+
