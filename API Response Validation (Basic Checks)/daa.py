import json
import requests

with open('query_DAA.txt') as f:
    content = f.readlines()
content = [str(x.strip()) for x in content]

url = 'https://abz-weekly.southcentralus.cloudapp.azure.com:443/api/mss/advanced-search/v1/list'

headers = {'Authorization': 'Basic Y2FwaXRhbDEyMzpjYXBpdGFsQDEyMw==', 'Content-Type': 'application/json'}

temp = []
bugs = []

for i in content:
    data = {
        'query': i,
        "request": {
            "query_type": "as",
            "session_id": "c494d392eb7cf63bd59e8bbe44fb8f80250c0dd7",
            "user_id": "capital123",
            "search_type": 1
        },
        "is_nlp": "true",
        "source": [],
        "file_type": [],
        "offset": 1,
        "time_filter_value": 0,
        "sort_order": "relevance",
        "apply_filter": "false",
        "publication_from_date": "2015-12-22",
        "publication_to_date": "2018-12-20"

    }

    res = requests.post(url, headers=headers, data=json.dumps(data), verify=False)
    json_data = json.loads(res.text)
    flag = False
    try:
        if json_data['status'] == "Success (200)":
            flag = True

        for j in json_data["records"]:
            if len(j["snippets"]) == 1 and flag and j["title"] and j["edam_date"]:
                print(json_data['query'], j["docIndex"], True)
                l = (json_data['query'], j["docIndex"], True)
                if l:
                    temp.append(l)
                else:
                    k = (json_data['query'], "ATTENTION!!!! BUG", False)
                    bugs.append(k)

            else:
                print(json_data['query'], j["docIndex"], False)
                l = (json_data['query'], j["docIndex"], False)
                if l:
                    temp.append(l)
                else:
                    k = (json_data['query'], "ATTENTION!!!! BUG", False)
                    bugs.append(k)
    #                        	temp.append("\n\r")
    except:
        q = (i, False)
        bugs.append(q)


with open('DAA_out.txt', 'w') as f:
    for i in temp:
        print >> f, i
with open('buggy_DAA_out.txt', 'w') as f:
    for i in bugs:
        print >> f, i
