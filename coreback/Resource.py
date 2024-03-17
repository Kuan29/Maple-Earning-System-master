import falcon, json
from falcon import Request, Response
from coreback import Const, DbConnector as dbconn
from coreback.MapleApi import Character, Test

conn = dbconn.connect(Const.DB_HOST, Const.DB_PORT, Const.DB_USER, Const.DB_PW, Const.DB_NAME)
maChar = Character()
test = Test()

# falcon Resource zip
class dumy:
    def __init__(self):
        pass

    async def on_get(self, req, resp):
        temp = dbconn.execute(conn, 'select * from BACK_T')
        resp.status = falcon.HTTP_200  # This is the default status
        resp.text = json.dumps(temp)

    async def on_post(self, req, resp):
        pass

class search:
    def __init__(self):
        self.utils = DB_Utils()

    # 나중에 post 방식으로 바꿔야 하는지 검토
    async def on_get(self, req:Request, resp:Response):
        # sql 따로 정리 할건지 검토

        ocid = maChar.getUserOcid(req.params)
        test.increase_trend(ocid)

        # crawl.crawlMaple(req.params.get('character_name'))
        temp = dbconn.execute(conn, f'SELECT ocid FROM MAPLE_ID_T where {self.utils.selectCondition(req.params)}')
        if(len(temp) != 0):
            resp.text = json.dumps(*temp)
        else:
            r = maChar.getUserOcid(req.params)
            # ocid = data['ocid']
            # sql = f"INSERT INTO MAPLE_ID_T (character_name,ocid) VALUES (%s,%s)"
            # dbconn.insert(self.conn,sql,(f'{param_value}', f'{ocid}'))
            resp.text = json.dumps(r)


class DB_Utils:
    def selectCondition(self, params):

        tempArr = []
        for (k, v) in params.items():
            tempArr.append(f'{k} = "{v}"')
        return ' and '.join(tempArr)

    def insertFormat(self, params):
        # tuple로 key, value 나눠서 배열
        # ex) [(key, value)]
        pass
    def updateFormat(self):
        pass
    def deleteFormat(self):
        pass

