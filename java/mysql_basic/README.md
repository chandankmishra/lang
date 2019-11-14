Basic program to access mysql from java

Steps:
1. Install java
2. Install mysql
3. download mysql connector 
4. Set classpath to point to mysql connector

----- Steps -----
cd /Users/chnmish/sw/java
export CLASSPATH=${CLASSPATH}:/Users/chnmish/Downloads/mysql-connector.jar
javac JavaMysqlSelectExample.java
java JavaMysqlSelectExample
