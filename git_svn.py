import subprocess
import sys

commit_message = sys.argv[1]

print(subprocess.check_output(['git','pull']))
print(subprocess.check_output(['svn', 'add', '.', '--force']))
print(subprocess.check_output(['svn', 'commit', '-m', commit_message]))
