# Purpose
The main way of using the Git library from python is using [the pygit2 package](https://github.com/libgit2/pygit2). Unfortunately, `pygit2` has some annoyingly specific requirements in regards to the version of `libgit2` installed, and despite saying that it bundles itself with the correct library in the doc, does not seem to do so.  
At least this is my observation when attempting to install `pygit2` on a Raspberry Pi 4 model B+.

This repo is a very simplistic wrapper around launching the git commands by executing commands on the CMD, making it basically git-version independent.

# Requirements and Installation
This repo has no python requirements, however some version of Git must be install on the host in order for it to work.

Install with:  
`python -m pip install git+https://github.com/zaltu/pygitcmd.git`