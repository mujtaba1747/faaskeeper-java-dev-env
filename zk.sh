# To tail live logs:
tail -f log_file_name
# To check open ports
sudo lsof -PiTCP -sTCP:LISTEN

# To build zk 3.8.5
cd dev
# Start docker on your machine
./run.sh # Opens into docker
mvn clean install
# Now copy the bin.tar.gz file from zookeeper-assembly/target
tar -xvf bin-tar-gz-file-path

# Use the zoo.cfg that I used

# To start ZK:
cd bin
./zkServer.sh start
./zkServer.sh start-foreground
./zkServer.sh stop
./zkServer.sh status

# To install the jar files in zk lib dir to local maven (Useful for obtaining locally built zk client lib)
# Run the jar installer python script
# The script also attempts to add those JARs in the pom.xml file of any project. Just give it the path to pom file

# To create a simple Java project to use the ZK client lib
mvn archetype:generate -DgroupId=com.localzkclient -DartifactId=zkclient-0 -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false
mvn clean compile
mvn exec:java -Dexec.mainClass="com.localzkclient.App"
# Paste the Java classes from the repo