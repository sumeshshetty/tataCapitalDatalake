"""
accept list of file name
and use multiprocessing to perfrom validation

read file in saprk tables in multi-threaded/processed mode
each validation should be seperate function
--check date inside the file
--check all columns present in file (maintain master to validate)
--schema check (datatype)
--RLV (Row level validation)


if any of check fails update file table db and alert
file validation process should run parallelly for each file, so an error in one file should not stop other
"""
