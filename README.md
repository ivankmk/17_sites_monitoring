# Sites Monitoring Utility

Script will check web sites from your txt file and revert two results: Is the server reply status 200 and is the domain prepaid for at least one month from the current date.

# How to Install

Python 3 should be already installed. Then use pip (or pip3 if there is a conflict with old Python 2 setup) to install dependencies:

```bash
pip install -r requirements.txt # alternatively try pip3
```



# How to launch

```bash

$ python check_sites_health.py list.txt # possibly requires call of python3 executive instead of just python
----------------------------------------
Web site: http://devman.org
Is server return status 200 ?: Yes
If domain prepaid for the next month?: Yes
----------------------------------------
Web site: http://lenta.ru
Is server return status 200 ?: Yes
If domain prepaid for the next month?: Yes
----------------------------------------
Web site: http://le23524nta.ru
Is server return status 200 ?: No
If domain prepaid for the next month?: No
```

The same with Windows environment;




# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
