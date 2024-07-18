from scholarly import scholarly
import jsonpickle
import json
from datetime import datetime
import os

author_id = '1W24GsQAAAAJ' 
author = scholarly.search_author_id(author_id)
scholarly.fill(author, sections=['basics', 'indices', 'counts', 'publications'])
author['updated'] = str(datetime.now())
author['publications'] = {v['author_pub_id']: v for v in author['publications']}


os.makedirs('results', exist_ok=True)
with open(f'results/gs_data_{author_id}.json', 'w') as outfile:
    json.dump(author, outfile, ensure_ascii=False)


shieldio_data = {
  "schemaVersion": 1,
  "label": "citations",
  "message": f"{author['citedby']}",
}
with open(f'results/gs_data_shieldsio_{author_id}.json', 'w') as outfile:
    json.dump(shieldio_data, outfile, ensure_ascii=False)
