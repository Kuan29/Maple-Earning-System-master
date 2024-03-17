MapleApi.py 정리

charName = 캐릭터 이름
ocid = 캐릭터 식별자 (ocid)
date = 검색 할 날짜
character_skill_grade = 검색 할 스킬 차수
↳ 0~6: 0~6차 스킬, 제로 공용스킬은 0차 알파/베타 스킬은 4차, hyperpassive: 하이퍼 패시브 스킬, hyperactive: 하이퍼 액티브 스킬

- 캐릭터 식별자(ocid)조회
    --getUserOcid(charName)
- 기본 정보 조회
    getCharBasic(ocid,date)

- 인기도 정보 조회
    getCharPopul(ocid,date)
    
- 종합 능력치 정보 조회
    getCharStat(ocid,date)

- 하이퍼 스탯 정보 조회
    getCharHyperst(ocid,date)

- 성향 정보 조회
    getCharPropens(ocid,date)

- 어빌리티 정보 조회
    getCharAbil(ocid,date)

- 장착 장비 정보 조회 (캐쉬 장비 제외)
    getCharItem(ocid,date)

- 장착 캐쉬 정보 조회
    getCharCash(ocid,date)

- 장착 심볼 정보 조회
    getCharSymbol(ocid,date)
  
- 장착 세트 효과 정보 조회
    getCharSeteff(ocid,date)

- 장착 헤어, 성형, 피부 정보 조회
    getCharBeauty(ocid,date)

- 장착 안드로이드 정보 조회
    getCharAndroid(ocid,date)

- 장착 펫 정보 조회
    getCharPet(ocid,date)

- 스킬 정보 조회
    getCharSkill(ocid,date,character_skill_grade)

- 장착 링크 스킬 정보 조회
    getCharLink(ocid,date)

- V매트릭스 정보 조회
    getCharVmatr(ocid,date)

- HEXA 코어 정보 조회
    getCharHexacore(ocid,date)

- HEXA 매트릭스 설정, HEXA 스탯 정보 조회
    getCharHexamatr(ocid,date)

- 무릉도장 최고 기록 정보 조회
    getCharDojang(ocid,date)
