import pkgutil
import sys

def main():
	"""
		This is the script wil be used to execute your solution. Make sure your
		output format is the same as instructed in the GitHub repo.

		Notice that the input format should not be changed. The following commands will be used
		to run your solution:
		$ unzip solution.pyz -d solution/
		$ cd solution/
		$ pip3 install -r requirements.txt
		$ cd ../
		$ python3 solution/ video.mp4 questions.txt

		Only the last line will be monitored by the power meter for efficiency and performance.
	"""
	with open(sys.argv[1]) as video, open(sys.argv[2]) as questions:
		# load resources
		print(pkgutil.get_data(__name__, "resource.txt").decode())

		# do something...

	# write answers and output to answers.txt
	with open("answers.txt", 'w') as f:
		print("EXIT:STAIR 1 STAR 1 ; GTR:a Bort 1 Skyline R34 ; ", file=f)
