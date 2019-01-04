import json
import pyodbc
import requests
import configparser
import utils
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

root_path = utils.root_path

common_config = configparser.ConfigParser()
common_config.read(root_path)

DB_CONX_STRING = """
    DRIVER={{ODBC Driver 17 for SQL Server}};
    SERVER={ip},{port};
    DATABASE={name};
    UID={user};
    PWD={passwd};
    """.format(
    ip=common_config['DEFAULT']['DB_IP'],
    port=common_config['DEFAULT']['DB_PORT'].replace(':', ''),
    name=common_config['DEFAULT']['DB_NAME'],
    user=common_config['DEFAULT']['DB_USER'],
    passwd=common_config['DEFAULT']['DB_PASS']
).replace("\n", "").strip()


def with_connection(f):
    def with_connection_(*args, **kwargs):

        con = pyodbc.connect(DB_CONX_STRING)
        cur = con.cursor()
        try:
            ret_val = f(cur, *args, **kwargs)
        except:
            con.rollback()
            raise
        else:
            con.commit()  # or maybe not
        finally:
            cur.close()
            con.close()
        return ret_val

    return with_connection_


input_file = utils.input_file

with open(input_file) as f:
    content = f.readlines()
content = [str(x.strip()) for x in content]

url = utils.url

headers = utils.headers

query_id = utils.query_id
request = utils.request
is_nlp = utils.is_nlp
source = utils.source
file_type = utils.file_type
offset = utils.offset
time_filter_value = utils.time_filter_value
sort_order = utils.sort_order
apply_filter = utils.apply_filter
publication_from_date = utils.publication_from_date
publication_to_date = utils.publication_to_date


def scenario_testing():
    # noinspection PyBroadException
    @with_connection
    def _scenario_testing(cur):
        try:
            cur.execute(utils.query)
            result = cur.fetchone()
            print(result)
            check1 = (query_id == 0 and result[0] != 0) and (publication_to_date == str(result[17])) \
                     and (publication_from_date == str(result[16])) and \
                     ((not source and not result[14]) or (str(source) == result[14])) and \
                     ((not file_type and not result[15]) or (str(file_type) == result[15]))
            check2 = (query_id != 0 and result[0] != 0 and apply_filter) and (result[1] == query_id) and \
                     (query_id != result[0]) and (publication_to_date == str(result[17])) and \
                     (publication_from_date == str(result[16])) and \
                     ((not source and not result[14]) or (source == result[14].split(','))) and \
                     ((not file_type and not result[15]) or (file_type == result[15].split(',')))

            if check1 or check2:
                return True
            else:
                return False

        except:
            print("Execution of the query failed")

    return _scenario_testing()


for i in content:
    data = {
        "query": i,
        "query_id": query_id,
        "request": request,
        "is_nlp": is_nlp,
        "source": source,
        "file_type": file_type,
        "offset": offset,
        "time_filter_value": time_filter_value,
        "sort_order": sort_order,
        "apply_filter": apply_filter,
        "publication_from_date": publication_from_date,
        "publication_to_date": publication_to_date
    }
    res = requests.post(url, headers=headers, data=json.dumps(data), verify=False)
    json_data = json.loads(res.text)
    check = scenario_testing()
    print('(', i, ',', check, ')')

"""
INDEXES OF COLUMNS IN SearchQueryEntry TABLE: 

 0 : QueryID
 1 : OldQueryID
 2 : UserID
 3 : SessionID
 4 : UserQuery
 5 : InputResultCount
 6 : SearchResultCount
 7 : SearchResponseTime
 8 : IsNlp
 9 : ModelUsed
10 : SearchOutputOrigin
11 : CreateDatetime
12 : GuiId
13 : TFBitMapDocID
14 : UISourceFilter
15 : UIFileTypeFilter
16 : UIPublicationFromDate
17 : UIPublicationToDate
18 : RasaPublicationFromDate
19 : RasaPublicationToDate

"""
