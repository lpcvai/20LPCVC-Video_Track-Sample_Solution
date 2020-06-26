# 2020 CVPR LPCVC Workshop - UAV Video Track Sample Solution
__Welcome to 20LPCVC UAV Video Track!__

Here we provide the sample solutions and submission instruction of the challenge described at **[Track Information](https://lpcv.ai/2020CVPR/video-track)**.
Please always check the updates in this repo for any changes. Join our [Slack workspace](lpcvc.slack.com) for any questions! 

## Sample Solutions
We provide multiple sample solutions with different approaches to help you understand this challenge better.
* **[Facebook Baseline Solution](https://github.com/sstsai-adl/workshops/tree/master/LPCV_2020/uav_video_challenge)**: This is the baseline solution provided by the Sponsor of this track Facebook. From this solution, there are two versions called `fb_sol_v1` and `fb_sol_v2` provided in this repo. The latest version will be used as basline solution for evaluation.
* `simple_solution/`: a simple skeleton solution we provide to demonstrate the submission structure. A more complicated solution will be updated soon.


## Submission Instruction
_Notice: The names of files or folders are sensitive._

Each team should submit only one file: `solution.pyz`: the zipped package of `solution/`. You should use __[zipapp](https://docs.python.org/3/library/zipapp.html)__ to create the `.pyz` file from your solution folder.
```
└── solution/
    ├── requirements.txt
    ├── __main__.py
    ├── main.py
    └── other modules and resources
```
* `requirements.txt`: Include all your dependencies. Make sure their versions are compatible on the Raspberry Pi .
* `__main__.py`: Used to run `solution/`. DO NOT modify.
* `main.py`: The script that we will use to execute your solution. Details are listed in the comments inside.
* `other modules and resources` (optional): Any other modules that `main.py` needs to import and any other files that you use in your solution.

### Creating `.pyz` files
We recommend zipping your solution using the following command. It adds a shebang line that we are able to use to identify what version of Python you are using.
```
python3 -m zipapp solution -p='/usr/bin/env python3.8'
```
The valid version of Python for the challenge is the latest patch version of CPython 3.8 for the AArch64 architecture. The command above specifies the shebang of your solution.
If you intend on using a different version of Python, please contact the organizers as soon as possible via Slack.

### Output
Your solution is expected to generate an `answer.txt` under the current directory when run. See comments in [`main.py`](simple_solution/main.py) to see how the solution will be run.
```
├── solution.pyz
└── answers.txt
```

## Evaluation Environment

* OS (updated):
```
NAME=Fedora
VERSION="32 (Thirty Two)"
ID=fedora
VERSION_ID=32
VERSION_CODENAME=""
PLATFORM_ID="platform:f32"
PRETTY_NAME="Fedora 32 (Thirty Two)"
ANSI_COLOR="0;34"
LOGO=fedora-logo-icon
CPE_NAME="cpe:/o:fedoraproject:fedora:32"
HOME_URL="https://fedoraproject.org/"
DOCUMENTATION_URL="https://docs.fedoraproject.org/en-US/fedora/f32/system-administrators-guide/"
SUPPORT_URL="https://fedoraproject.org/wiki/Communicating_and_getting_help"
BUG_REPORT_URL="https://bugzilla.redhat.com/"
REDHAT_BUGZILLA_PRODUCT="Fedora"
REDHAT_BUGZILLA_PRODUCT_VERSION=32
REDHAT_SUPPORT_PRODUCT="Fedora"
REDHAT_SUPPORT_PRODUCT_VERSION=32
PRIVACY_POLICY_URL="https://fedoraproject.org/wiki/Legal:PrivacyPolicy"
```
* CPython 3.8 (64-bit)
* Notice that you need to make sure you have pytorch built correctly when testing your own solution. Here we provide the pre-built wheel of `torch-1.6` on `linux_aarch64`. You can find the file **[`torch-1.6.0a0+503be4e-cp38-cp38-linux_aarch64.whl`](https://github.com/lpcvai/20LPCVC-Video_Track-Sample_Solution/blob/master/torch-1.6.0a0+503be4e-cp38-cp38-linux_aarch64.whl)** in this repo. More recent PyTorch builds than the one used by our sample solution are built daily by [OpenLab](https://openlabtesting.org/) and can be downloaded [here](https://status.openlabtesting.org/builds/builds?project=pytorch%2Fpytorch&job_name=pytorch-arm64-build-daily-master-py38).
* The script that will be used to calculate the score of your submission file is under `evaluation/`. Please check [Evaluation Workflow](https://github.com/lpcvai/20LPCVC-Video_Track-Sample_Solution/wiki/Evaluation-Workflow) on the Wiki for details.
