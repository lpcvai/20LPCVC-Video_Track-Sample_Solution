import pkgutil
import sys

def main():
	# open video and questions files
	with open(sys.argv[1]) as video, open(sys.argv[2]) as questions:
		# load resources
		print(pkgutil.get_data(__name__, "resource.txt").decode())

		# do something...

	# write answers
	with open("usr_result.txt", 'w') as f:
		print("EXIT:STAIR 1 STAR 1 ; GTR:a Bort 1 Skyline R34 ; ", file=f)

