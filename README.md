# 2020 CVPR LPCVC Workshop - UAV Video Track Sample Solution
__Welcome to 20LPCVC UAV Video Track!__ Here we provide the submission instruction and sample solutions of the challege described at **[Track Information](https://lpcv.ai/2020CVPR/video-track)**.

## Submission Instruction
_Notice: The names of files or folders are sensitive._

Each team should submit only one file: `solution.pyz`: the zipped package of `solution/`. You should use __[zipapp](https://docs.python.org/3/library/zipapp.html)__ to create the `.pyz` file from your solution folder. 
```bash
├── solution/
│   ├── requirments.txt
│   ├── __main__.py
│   ├── main.py
│   └── other_files
```
* `requirments.txt`: Include all your dependencies. Make sure their versions are compatible on the Rawspberry Pi . 
* `__main__.py`: Used to run `solution/`. DO NOT modify.
* `main.py`: The script that we will use to execute your solution. Details are listed in the comments inside. 
* `other_files`: Any other files that you used to run your solution. 

### Output
Your solution is expected to generate an `answer.txt` under the current directory. 
```bash
├── solution.pyz
└── answer.txt
```

## Sample Solutions
We provide multiple sample solutions with different approaches to help you understand this challenge better. 
* **[Facebook Baseline Solution](https://github.com/sstsai-adl/workshops/tree/master/LPCV_2020/uav_video_challenge)**: This is the basline solution provided by the Sponsor of this track Facebook. 
* `simple_solution/`: a simple solutio we provide to demonstrate the submission structure. A more complicated solution will be updated soon.

