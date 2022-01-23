
# Anti Procrastinator Script
---

### What does this thing do?
	
Set this script up in Crontab on Linux and it will run to check if any of these tabs on Mozilla Firefox are running:

	banned = ["instagram", "facebook", "netflix", "hotstar", "r/PewdiepieSubmissions", "hbo", "9gag", "gogoanime", "crunchyroll", "9anime", "funimation"]

If it finds one, it terminates the browser :)
<br>

#### Requirements

Install the  `lz4`  package

	pip install lz4


One key detail about the code

	file = open(f"{home}/.mozilla/firefox/tt5rz730.default-release/sessionstore-backups/recovery.jsonlz4", "rb")

Note that your  `.mozilla/firefox/`  may have a different folder name depending on the version you are using, so just browse through the directory and change it :)

Finally, add it to cron

	crontab -e

	* * * * * python3 /home/username/path/to/apfirefox.py


