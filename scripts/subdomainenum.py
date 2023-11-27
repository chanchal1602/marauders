import subprocess

domain_name = input("Enter domain name: ")
command = ["amass", "enum", "-passive", "-d", domain_name]

process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = process.communicate()

if stderr:
    print("Error:", stderr.decode("utf-8"))
else:
    print(stdout.decode("utf-8"))
