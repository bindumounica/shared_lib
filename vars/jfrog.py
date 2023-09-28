import requests
import subprocess

# Define the curl command as a list of strings
curl_command = [
    "curl",
    "-X","PUT","-u","admin:Mounica@60","-T","/home/ubuntu/Java_app_3.0/target/kubernetes-configmap-reload-0.0.1-SNAPSHOT.jar","http://54.144.144.191:8082/artifactory/example-repo-local/" 
]

# Define the URL you want to check
url_to_check = "http://54.144.144.191:8082/"  # Replace with the URL you want to test

try:
    # Send an HTTP GET request to the URL
    response = requests.get(url_to_check)

    # Check the HTTP status code
    if response.status_code == 200:
        print(f"The URL {url_to_check} is serving the request with status code 200 (OK).")
#        curl -X PUT -u admin -T target/kubernetes-configgap-reload-0.0.1-SNAPSHOT.jar http://54.144.144.191:8082/artifactory/example-repo-local/
    else:
        print(f"The URL {url_to_check} returned status code {response.status_code}.")
    # Execute the curl command
    result = subprocess.run(curl_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Check the return code
    if result.returncode == 0:
        # Successful execution
        print("Curl command executed successfully.")
        # Print the command output
        print("Command Output:")
        print(result.stdout)
    else:
        # Error during execution
        print(f"Error executing curl command. Return code: {result.returncode}")
        # Print the error output
        print("Error Output:")
        print(result.stderr)
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")

