# 통계청 API를 이용한 데이터 추출

import requests
import json

url = 'https://kosis.kr/openapi/Param/statisticsParameterData(-------------------------)'
req = requests.get(url)

json_file = json.loads(req.text)
for row in json_file:
    print('시기:{0},행정구역별:{1},연령별:{2},\계:{3}'.format(row['PRD_DE'], row['C1_NM'], row['C2_NM'],row['DT']))
