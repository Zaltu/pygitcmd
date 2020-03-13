"""
Define standard operations used by any normal intelligent person when using git.
"""
import os
import subprocess

class GitRepo:
    """
    Represents a git repository, and all functionality (that I've implemented) related to it.
    Takes two parameters: local and remote locations of the repo.

    :param str local: path to where the local git repo should either exist or be cloned
    :param str remote: remote url where the git repo exists
    """
    def __init__(self, local, remote):
        self._local = local
        self._dir = os.path.split(os.path.abspath(local))[0]
        self._remote = remote


    @property
    def local(self):
        """
        The local property represents the local path on disk to the cloned git repository.

        :raises MissingLocalException: if the local path is not a git repo
        :returns: the local path
        :rtype: str
        """
        # Check that self._local is a real location containing a .git
        if not os.path.exists(self._local) or\
           not os.path.isdir(self._local) or\
           not os.path.exists(os.path.join(self._local, ".git")):
                raise MissingLocalException("No local path %s" % self._local)
        return self._local

    @property
    def remote(self):
        """
        The remote repo URL.
        TODO validate remote repo.

        :returns: the remote repo
        :rtype: str
        """
        return self._remote

    def clone(self):
        """
        Clone the remote repository to the local dir if it is not already there.
        """
        try:
            self.local
        except MissingLocalException:
            self.__exec_cmd(f"git clone {self.remote} {self._local}", self._dir)

    def pull(self):
        """
        Perform a git pull on the local repo.
        """
        self.__exec_cmd("git pull", self.local)

    def push(self):
        """
        Perform a git push on the local repo to the remote repo.
        """
        self.__exec_cmd("git push", self.local)  # TODO handle missing branches in remote.

    def fetch(self):
        """
        Perform a git fetch from the remote repo to the local repo.
        """
        self.__exec_cmd("git fetch", self.local)

    def add(self, file_match):
        """
        Perform git add on file or file match.
        Accepts arguments as file_match too (eg -u)
        DEFAULTS TO `-u`!

        :param str file_match: files to add or command args
        """
        self.__exec_cmd(f"git add {file_match or '-u'}", self.local)

    def commit(self, message):
        """
        Commit changes with a message.

        :param str message: commit message. Required you lazy bum.

        :raises AttributeError: if message is invalid (None, empty str, etc...)
        """
        if not message:
            raise AttributeError("\"Message\" parameter must be passed.")
        self.__exec_cmd(f"git commit -m \"{message}\"", self.local)

    def checkout(self, branch, new=False):
        """
        Checkout a branch. Can also checkout to a new branch.
        This is how branch creation is handled because fuck you.

        :param str branch: branch name to checkout
        :param bool new: whether to create a new branch, defaults to False
        """
        # Some weird string spacing here for the .split required by subprocess.check_output
        self.__exec_cmd(f"git checkout{' -b' if new else ''} {branch}", self.local)

    @staticmethod
    def __exec_cmd(cmd, workdir):
        """
        Execute a command from a location.

        :param str cmd: command to execute
        :param str workdir: path to location from which to execute
        """
        subprocess.check_output(cmd.split(" "), cwd=workdir)


class MissingLocalException(Exception):
    """
    Local repo does not exist.
    """

class MissingRemoteException(Exception):
    """
    Remote repo does not exist or can't be reached.
    """
