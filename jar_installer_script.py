import os
import subprocess

# Specify the directory containing the JAR files
directory = '/Users/syed/Desktop/gsoc/zk-custom-3.8.5/apache-zookeeper-3.10.0-SNAPSHOT-bin/lib/'

def run_maven_command_for_jars(directory):
    # List all files in the directory
    files = os.listdir(directory)
    
    # Filter out JAR files
    jar_files = [file for file in files if file.endswith('.jar')]
    
    for jar in jar_files:
        jar_path = os.path.join(directory, jar)
        artifact_id = os.path.splitext(jar)[0]  # Extract artifactId from the JAR file name
        
        # Construct the Maven command
        maven_command = [
            'mvn', 'install:install-file',
            f'-Dfile={jar_path}',
            '-DgroupId=com.zklocal',    # Change this as needed
            f'-DartifactId={artifact_id}',  # Use the JAR file name as the artifactId
            '-Dversion=1.0.1',            # Change this as needed
            '-Dpackaging=jar'
        ]

        # print(maven_command)
        # print(artifact_id)
        
        try:
            # Run the Maven command
            result = subprocess.run(maven_command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print(f"Successfully installed {jar}:")
            print(result.stdout.decode())
        except subprocess.CalledProcessError as e:
            print(f"Failed to install {jar}:")
            print(e.stderr.decode())

def add_dependencies_to_pom(pom_path, jar_directory):
    dependencies = ""
    files = os.listdir(jar_directory)
    
    jar_files = [file for file in files if file.endswith('.jar')]
    
    for jar in jar_files:
        artifact_id = os.path.splitext(jar)[0]
        dependency = f"""
        <dependency>
            <groupId>com.zklocal</groupId>
            <artifactId>{artifact_id}</artifactId>
            <version>1.0.1</version>
        </dependency>"""
        dependencies += dependency
    
    with open(pom_path, 'r') as file:
        pom_content = file.read()
    
    new_pom_content = pom_content.replace("<!-- Local JAR dependencies -->", f"<!-- Local JAR dependencies -->\n{dependencies}")
    
    with open(pom_path, 'w') as file:
        file.write(new_pom_content)

# Path to the pom.xml file
pom_path = '/Users/syed/Desktop/gsoc/zk3.8.5/zk-client-proj/zkclient-0/pom.xml'

run_maven_command_for_jars(directory)
add_dependencies_to_pom(pom_path, directory)
