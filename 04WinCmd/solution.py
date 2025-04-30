
from subprocess import check_output


result = check_output("dir C:", shell=True).decode()
print(result)

