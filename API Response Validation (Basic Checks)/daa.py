import json
import requests
import csv
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

with open('query_DAA.txt') as f:
    content = f.readlines()
content = [str(x.strip()) for x in content]

url = 'https://abz-weekly.southcentralus.cloudapp.azure.com:443/api/mss/advanced-search/v1/list'

headers = {'Authorization': 'Basic Y2FwaXRhbDEyMzpjYXBpdGFsQDEyMw==', 'Content-Type': 'application/json'}

temp = [('QUERY', 'DOC INDEX', 'TITLE', 'DOC ID (DOC NAME)', 'JDOC ID (CORPUS ID)', 'SECTION ID (SNIPPET ID)',\
         'FILE TYPE', 'RELEVANCE SCORE', 'PUBLICATION FROM DATE', 'PUBLICATION TO DATE')]
bugs = [('QUERY', 'STATUS')]

for i in content:
    data = {
            "query": i,
            "request":  {
                        "query_type": "as",
                        "session_id": "c494d392eb7cf63bd59e8bbe44fb8f80250c0dd7",
                        "user_id": "capital123",
                        "search_type": 1
                        },
            "is_nlp": True,
            "source": [],
            "file_type": [],
            "offset": 1,
            "time_filter_value": 0,
            "sort_order": "relevance",
            "apply_filter": True,
            "publication_from_date": "",
            "publication_to_date": "",
            "query_id": 0
    }
    res = requests.post(url, headers=headers, data=json.dumps(data), verify=False)
    json_data = json.loads(res.text)
    flag = False
    try:
        if json_data['status'] == "Success (200)":
            flag = True

        for j in json_data["records"]:
            if len(j["snippets"]) == 1 and flag and j["title"] and j["edam_date"]:
                l = (str(json_data['query']), j['docIndex'], str(j['title']), str(j["doc_id"]), j["jdoc_id"], \
                     str(j["snippets"][0]["section_id"]), str(j['path'][0]['type']), j["score"], \
                     str(json_data['publication_from_date']), str(json_data['publication_to_date']))
                print(l)
                if l:
                    temp.append(l)
                else:
                    k = (json_data['query'], json_data['status'])
                    bugs.append(k)

            else:
                print(json_data['query'], json_data['status'])
                l = (json_data['query'], json_data['status'])
                if l:
                    temp.append(l)
                else:
                    k = (json_data['query'], json_data['status'])
                    bugs.append(k)

    except:
        q = (i, "BUGGY QUERY!!!")
        bugs.append(q)


DAA = open('DAA_out.csv', 'w')
with DAA:
    writer = csv.writer(DAA)
    writer.writerows(temp)


daa_bugs = open('buggy_DAA_out.csv', 'w')
with daa_bugs:
    writer = csv.writer(daa_bugs)
    writer.writerows(bugs)
