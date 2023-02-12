"""

input parameters:
spark session object  as the session and temp view of 14 tables would already
be created in map_to_in_memory_tables function

this function will read the 14 in memory tables
and master tables data
, perform  etl/join mapping required for 14 ods tables required

the created ods tables object needs to be written parallely to ods database with truncate and insert
also in same ods historical data do just insert
need to keep same data in adls gen2 storage


"""
