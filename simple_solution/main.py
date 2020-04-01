import pkgutil
import sys

def main():
	"""
		This is the script wil be used to execute your solution. Make sure your
		ourput format is the same as instructed in the GitHub repo.

		Notice that the input format should not be changed. The following command will be used
		to run your solution (after unzip your solution.pyz):
		$ python solution/ video.mp4 questions.txt
	"""
	with open(sys.argv[1]) as video, open(sys.argv[2]) as questions:
		# load resources
		print(pkgutil.get_data(__name__, "resource.txt").decode())

		# do something...

	# write answers and output to answers.txt
	with open("answers.txt", 'w') as f:
		print("EXIT:STAIR 1 STAR 1 ; GTR:a Bort 1 Skyline R34 ; ", file=f)
