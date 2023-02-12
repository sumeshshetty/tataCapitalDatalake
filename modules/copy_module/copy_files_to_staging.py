# before this function will check type of file monthly or daily

# read the database master for files -- can be done in later stage
# this script will copy all files from source to azure adls gen2
"""
input params: file names list
using multiprcessing copy files to adls gen2 location

raw_files/date/file.csv or excel
update db file table after each file copy susccess
log error if any while copying

output no need : True or raise error for specific file


"""
