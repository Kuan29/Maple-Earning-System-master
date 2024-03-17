import requests, datetime
from coreback import Const, DbConnector as dbconn
from urllib.parse import quote_plus, unquote_plus

HOST = 'https://open.api.nexon.com'
HEADERS = { 'x-nxopen-api-key': Const.NEXON_TOKEN}

class REST:
    def __init__(self):
        pass

    def get(self, url, params:dict):
        for key in params.keys():
            params.update({key: unquote_plus(quote_plus(params[key]))})

        res = requests.get(
            f"{HOST}/{url}",
            params = params,
            headers = HEADERS,
        )

        # error trace in the future
        if res.status_code == 200:
            return res.json()

    def post(self):
        pass

    #따로 빼야되나?
    def popularget(self,url,params,date):
        params['date'] = date

        res = requests.get(
            f"{HOST}/{url}",
            params = params,
            headers = HEADERS,
        )


        if res.status_code == 200:
            return res.json()

    def skillget(self,url,params,date,character_skill_grade):
        params['date'] = date
        params['character_skill_grade'] = character_skill_grade

        res = requests.get(
            f"{HOST}/{url}",
            params = params,
            headers = HEADERS,
        )

        if res.status_code == 200:
            return res.json()

class Character:
    def __init__(self, *args):
        self.rest = REST()

    # 캐릭터 식별자(ocid)조회
    def getUserOcid(self, params):
        return self.rest.get('maplestory/v1/id', params)

    # 기본 정보 조회
    def getCharBasic(self,params,date):
        return self.rest.popularget('maplestory/v1/character/basic',params,date)

    # 인기도 정보 조회
    def getCharPopul(self,params,date):
        return self.rest.popularget('maplestory/v1/character/popularity',params,date)

    # 종합 능력치 정보 조회
    def getCharStat(self,params,date):
        return self.rest.popularget('maplestory/v1/character/stat',params,date)

    # 하이퍼 스탯 정보 조회
    def getCharHyperst(self,params,date):
        return self.rest.popularget('maplestory/v1/character/hyper-stat',params,date)

    # 성향 정보 조회
    def getCharPropens(self,params,date):
        return self.rest.popularget('maplestory/v1/character/propensity',params,date)

    # 어빌리티 정보 조회
    def getCharAbil(self,params,date):
        return self.rest.popularget('maplestory/v1/character/ability',params,date)

    # 장착 장비 정보 조회 (캐쉬 장비 제외)
    def getCharItem(self,params,date):
        return self.rest.popularget('maplestory/v1/character/item-equipment',params,date)

    # 장착 캐쉬 정보 조회
    def getCharCash(self,params,date):
        return self.rest.popularget('maplestory/v1/character/cashitem-equipment',params,date)

    # 장착 심볼 정보 조회
    def getCharSymbol(self,params,date):
        return self.rest.popularget('maplestory/v1/character/symbol-equipment',params,date)

    # 장착 세트 효과 정보 조회
    def getCharSeteff(self,params,date):
        return self.rest.popularget('maplestory/v1/character/set-effect',params,date)

    # 장착 헤어, 성형, 피부 정보 조회
    def getCharBeauty(self,params,date):
        return self.rest.popularget('maplestory/v1/character/beauty-equipment',params,date)

    # 장착 안드로이드 정보 조회
    def getCharAndroid(self,params,date):
        return self.rest.popularget('maplestory/v1/character/android-equipment',params,date)

    # 장착 펫 정보 조회
    def getCharPet(self,params,date):
        return self.rest.popularget('maplestory/v1/character/pet-equipment',params,date)

    # 스킬 정보 조회
    # 0~6: 0~6차 스킬, 제로 공용스킬은 0차 알파/베타 스킬은 4차,
    # hyperpassive: 하이퍼 패시브 스킬, hyperactive: 하이퍼 액티브 스킬
    def getCharSkill(self,params,date,character_skill_grade):
        return self.rest.skillget('maplestory/v1/character/skill',params,date,character_skill_grade)

    # 장착 링크 스킬 정보 조회
    def getCharLink(self,params,date):
        return self.rest.popularget('maplestory/v1/character/link-skill',params,date)

    # V매트릭스 정보 조회
    def getCharVmatr(self,params,date):
        return self.rest.popularget('maplestory/v1/character/vmatrix',params,date)

    # HEXA 코어 정보 조회
    def getCharHexacore(self,params,date):
        return self.rest.popularget('maplestory/v1/character/hexamatrix',params,date)

    # HEXA 매트릭스 설정, HEXA 스탯 정보 조회
    def getCharHexamatr(self,params,date):
        return self.rest.popularget('maplestory/v1/character/hexamatrix-stat',params,date)

    # 무릉도장 최고 기록 정보 조회
    def getCharDojang(self,params,date):
        return self.rest.popularget('maplestory/v1/character/dojang',params,date)

class Union:

    def __init__(self):
        self.rest = REST()

    # 유니온 정보 조회
    def getUserUnion(self,params,date):
        return self.rest.popularget('maplestory/v1/user/union',params,date)

    # 유니온 공격대 정보 조회
    def getUserUnionraid(self,params,date):
        return self.rest.popularget('maplestory/v1/user/union-raider',params,date)

    # 유니온 아티팩트 정보 조회
    def getUserUnionarti(self,params,date):
        return self.rest.popularget('maplestory/v1/user/union-artifact',params,date)


class Guild:

    def __init__(self):
        pass
    # 길드 식별자(oguild_id) 정보 조회
    def getGuildId():
        pass
    # 길드 기본 정보 조회
    def getGuildBasic():
        pass


class Test:

    def __init__(self):
        pass

    def increase_trend(self,params):
        result_li =[]
        result_dic = {}
        last_wek=0

        conn = dbconn.connect(Const.DB_HOST, Const.DB_PORT, Const.DB_USER, Const.DB_PW, Const.DB_NAME)

        current_time = datetime.datetime.now().time().strftime("%H%M")
        dt = datetime.date.today()

        if(current_time <= '0100'):
            dt+=datetime.timedelta(days=-3)

        else:
            dt+=datetime.timedelta(days=-2)

        for i in range(7):
            dt+=datetime.timedelta(days=-1)
            date = str(dt)
            r = Character().getCharBasic(params,date)
            result_dic = {"lv":r['character_level'],"exp":int(r['character_exp'])}
            result_li.append(result_dic)
        print(result_li)
        # exp = dbconn.execute(conn,f'SELECT EXP FROM MAPLE_EXP_T where lv={result_li[i]["lv"]}')
        # print(result_li[i]["lv"])
        # print(exp[0]['EXP'])

        for i in range(0,6):

            if(result_li[i]['lv'] != result_li[i+1]['lv']):
                exp = dbconn.execute(conn,f'SELECT EXP FROM MAPLE_EXP_T where lv={result_li[i+1]["lv"]}')
                s= round((result_li[i]['exp']+exp[0]['EXP']) - result_li[i+1]['exp'])
                # print(result_li[i]['exp']+exp[0]['EXP'])
                # print(result_li[i+1]['exp'])
                print(s)
                last_wek+=s

            else :
                pass
                s= round((result_li[i]['exp']) - result_li[i+1]['exp'])
                print(s)
                last_wek+=s

        print(last_wek/6)
