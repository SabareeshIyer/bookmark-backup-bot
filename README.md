# Automated Bookmark Backup

A Python bot to backup your Chrome bookmarks and email them to an email ID of your choice. 

Setup as cron job to have it run periodically.

## Usage

- Download repository
- Substitute fields such as sender's email ID, receiver's email ID and sender's password with valid details
- Go [here](https://www.google.com/settings/security/lesssecureapps) to allow less secure apps on your account. This is essential to be able to connect to your account from the script.
- Replace 'username' in the `filepath` variable with your username.
- Alter `subject` to suit your needs.
- Run `emailDaemon.bat`

## Cron job setup

Use Windows task Scheduler to run the batch file periodically. Refer to [this guide](http://www.thewindowsclub.com/how-to-schedule-batch-file-run-automatically-windows-7) in case you need assistance.
