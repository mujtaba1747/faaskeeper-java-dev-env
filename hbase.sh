# Step 1 install hadoop 3.4.0
# Link: https://levelup.gitconnected.com/install-hadoop-on-macos-efe7c860c3ed
# Link: https://stackoverflow.com/questions/48978480/hadoop-permission-denied-publickey-password-keyboard-interactive-warning/49960886
brew install hadoop
# Find location of installation
brew info hadoop
cd /opt/homebrew/Cellar/hadoop/3.4.0/
# Add JAVA_HOME to hadoop-env.sh
echo $JAVA_HOME
# Copy paste the contents of .xml config files from repo
# Go to MacOS settings and enable remote login
# Add an ed25519 key to authorized key. It should be passwordless:
ssh-keygen -t ed25519 -f ~/.ssh/id_ed25519
cat ~/.ssh/id_ed25519.pub  >> ~/.ssh/authorized_keys\n
# If this doesn't work, try rsa
# Format the namenode
hadoop namenode -format
./sbin/start-all.sh
hadoop fs -mkdir /user
hadoop fs -ls /
# To stop
./sbin/stop-all.sh
# Web UI: localhost:9870

# Step 2 install and start hbase 2.5.8
# Link: https://hbase.apache.org/book.html
# Use config hbase-site.xml file from repo

# Add this to hbase-env.sh
export HBASE_MANAGES_ZK=false
./bin/start-hbase.sh
# Must verify from logs of regionserver and master if it started successfully
# Start REST server (Optional if you wanna use REST API to communicate with Hbase)
./hbase rest start -p 9999 -i 10000 # i starts a webui on 10000 p is the rest api server (no ui)
# Start thrift server to use happybase python client
./hbase thrift start
# To stop
./bin/hbase-daemon.sh stop regionServer
./bin/hbase-daemon.sh stop master


# Step 3: Use happybase python script to create hbase tables
python3 -m venv hbase_py
cd hbase_py
source ./bin/activate
python3 -m pip install happybase
python3 -m pip install setuptools
# Copy and run the script.py from repo.
# Record audit logs of ZK for different operations