input_file = 'query_DAA.txt'
url = 'https://abz-weekly.southcentralus.cloudapp.azure.com:443/api/mss/advanced-search/v1/list'
headers = {'Authorization': 'Basic Y2FwaXRhbDEyMzpjYXBpdGFsQDEyMw==', 'Content-Type': 'application/json'}
root_path = '/home/abzooba/PycharmProjects/CG_Phase_4_Automation/common_config.ini'

#----------------------------------------------------------------------------------------------------#

query_id = 58155
request = {
    "query_type": "as",
    "session_id": "c494d392eb7cf63bd59e8bbe44fb8f80250c0dd7",
    "user_id": "capital123",
    "search_type": 1
}
is_nlp = "true"
source = ["galileo", "edam"]
file_type = []
offset = 1
time_filter_value = 0
sort_order = "relevance"
apply_filter = "true"
publication_from_date = "2015-12-22"
publication_to_date = "2018-12-20"

#----------------------------------------------------------------------------------------------------#

query = "select * from CognitiveLearningDaa_4.dbo.SearchQueryEntry order by QueryID desc"
