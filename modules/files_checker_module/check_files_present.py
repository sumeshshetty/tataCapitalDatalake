"""
no input for this module

this module check count of copied files in adls gen2 for current date
it would use the master json to check if mandatory files are present or not

if mandatory files are not present then
--update db and increment retry count, send alert
else:
--update db with sucess

a sperate db flag checker funciton would check if all mandatory files flag is True
then only call file validation function



"""
