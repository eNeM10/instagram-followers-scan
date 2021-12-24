
# Instagram Followers Scan

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](https://github.com/eNeM10/instagram-followers-scan/blob/main/LICENSE) [![Last Commit](https://img.shields.io/github/last-commit/eNeM10/instagram-followers-scan?style=for-the-badge)](https://github.com/eNeM10/instagram-followers-scan/commits/main) [![PyVersion](https://img.shields.io/pypi/pyversions/instaloader.svg?style=for-the-badge)](https://www.python.org/) [![PyPIVersion](https://img.shields.io/pypi/v/instaloader.svg?style=for-the-badge)](https://pypi.org/project/instaloader/)

A Python Script to scan through an Instagram account to find all the followers and followings.
You can also get filtered list of users that are your:

* friends (followers that you follow back)
* fans (followers that you don't follow back)
* stars ;) (celebrities that you follow dreaming of getting that follow back)
(The script also allows you to save all the lists to a file)

## Prerequisite

* Must have Python installed
* Ensure that you have Python, at least version 3.6, and pip installed.
  Install Instaloader

    ```bash
    pip3 install instaloader
    ```

## How To Use

* Run ``igs.py``

    ```bash
    py igs.py
    ```

* Enter your *instagram username*

    ```text
    Enter your Instagram username: abc123
    ```

* If will try to find a saved session for the entered user. If not found it will ask you to enter your password to login

    ```text
    Enter Instagram password for abc123:
    ```

* After successful login you can choose to save the login information locally for ease

    ```text
    Save login information locally? (y/n): y
    ```

    This will save your current session to a file that would be saved in ``C:\Users\your_username\AppData\Local\Instaloader``.
* Enter the username of the account you want to scan.It must be a public account. Incase of a private account it must be followed by you. If you want to scan your own account then enter your username.

    ```text
    Target account must be public. Data of private accounts can be fetched if you follow them.
    Enter target account username: abc123
    ```

* The followers and followings of the account will be fetched. You can choose to them to files.

    ```text
    Fetching followers...
    Followers list obtained!

    Fetching followees...
    Followees list obtained!

    Save followers and followings to file? (y/n): y
    Followers list saved!
    Followees list saved!
    ```

* You will get the following menu after followers and followings are fetched

    ```text
    MENU:
    1. Get friends (followers that you follow back)
    2. Get fans (followers that you don't follow back)
    3. Get stars ;) (followees that don't follow you back)
    0. Exit

    Enter your choice:
    ```

* Choose any option, We guess you are looking for the stars ;).

## Acknowledgements

* [Instaloader](https://github.com/instaloader/instaloader)
