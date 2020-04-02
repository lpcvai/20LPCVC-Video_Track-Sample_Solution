# 2020 CVPR LPCVC Workshop - UAV Video Track Sample Solution
__Welcome to 20LPCVC UAV Video Track!__ Here we provide the submission instruction and sample solutions of the challenge described at **[Track Information](https://lpcv.ai/2020CVPR/video-track)**.

## Submission Instruction
_Notice: The names of files or folders are sensitive._

Each team should submit only one file: `solution.pyz`: the zipped package of `solution/`. You should use __[zipapp](https://docs.python.org/3/library/zipapp.html)__ to create the `.pyz` file from your solution folder.
```
├── solution/
│   ├── requirements.txt
│   ├── __main__.py
│   ├── main.py
│   └── other modules and resources
```
* `requirements.txt`: Include all your dependencies. Make sure their versions are compatible on the Raspberry Pi .
* `__main__.py`: Used to run `solution/`. DO NOT modify.
* `main.py`: The script that we will use to execute your solution. Details are listed in the comments inside.
* `other modules and resources` (optional): Any other modules that `main.py` needs to import and any other files that you use in your solution.

### Creating `.pyz` files
We recommend zipping your solution using the following command. It adds a shebang line that we are able to use to identify what version of Python you are using.
```
python3 -m zipapp solution -p='/usr/bin/env python3.7'
```
The valid versions of Python for the challenge are the latest patch versions of Python 3.7. The command above specifies the shebang of your solution. 

### Output
Your solution is expected to generate an `answer.txt` under the current directory when run. See comments in [`main.py`](simple_solution/main.py) to see how the solution will be run.
```
├── solution.pyz
└── answers.txt
```

## Sample Solutions
We provide multiple sample solutions with different approaches to help you understand this challenge better.
* **[Facebook Baseline Solution](https://github.com/sstsai-adl/workshops/tree/master/LPCV_2020/uav_video_challenge)**: This is the baseline solution provided by the Sponsor of this track Facebook.
* `simple_solution/`: a simple skeleton solution we provide to demonstrate the submission structure. A more complicated solution will be updated soon.
