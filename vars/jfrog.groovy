def call()
{
	pythonScript = 'vars/jfrog.py' // Replace with the path to your Python script
	processBuilder = new ProcessBuilder(['python3', pythonScript])

	try {
    		Process process = processBuilder.start()
    		process.waitFor()
    		println "Python script executed successfully."
	} catch (IOException | InterruptedException e) {
    		println "Error running Python script: ${e.message}"
	}

}
