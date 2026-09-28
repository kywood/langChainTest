from langchain.chat_models import init_chat_model
from pydantic import BaseModel, Field

from chain_test.llm_def import llm


class CodeReview(BaseModel):
    """코드 리뷰 결과"""
    summary: str = Field(description="코드 기능 요약")
    score: int = Field(description="1-10점 품질 점수")
    issues: list[str] = Field(description="발견된 문제점 목록")
    suggestions: list[str] = Field(description="개선 제안 목록")

# llm = init_chat_model("gpt-4o-mini")
structured_llm = llm.with_structured_output(CodeReview)

result = structured_llm.invoke("""
다음 코드를 리뷰해주세요:

- 주석 부분은 빼고
- 코드는 전체의 일부


class cDBProperty(object):
    #mDB_Type = None

    def __init__(self , db_type ):
        self.mDB_Type = db_type

    def ConnectInfo(self):
        print("cDBProperty::ConnectInfo")
        return None

    def GetDBType(self):
        return self.mDB_Type


    def GetArgs(self):
        return None

    def GetKwargs(self):
        return None


class cMysqlProperty(cDBProperty):
    # mAR=None
    # mKW=None
    def __init__(self , *args , **kwargs ):
        cDBProperty.__init__(self, E_DB.MYSQL)
        self.mArgs = args
        self.mKwargs = kwargs

    # def __init__(self , id, pw, db_name , host_ip, port = 3306 ,  charset='utf8', use_unicode=True ):
    #     cDBProperty.__init__(self,E_DB.MYSQL  )
    #     #print "---------------------------------cMysqlProperty :: init"
    #     self.mHost_ip = host_ip
    #     self.mId = id
    #     self.mPw = pw
    #     self.mDB_NAME = db_name
    #     self.mCharset = charset
    #     self.mUse_unicode = use_unicode
    #     self.mPort = port

    def GetArgs(self):
        return self.mArgs

    def GetKwargs(self):
        return self.mKwargs


    def ConnectInfo(self):
        print("cMysqlProperty::ConnectInfo mDB_Type " , self.GetDBType())

        return self.mArgs, self.mKwargs
        # return self.mAR , self.mKW

        # return { 'host' : self.mHost_ip ,
        #          'user' :  self.mId ,
        #          'passwd' : self.mPw ,
        #          'db' : self.mDB_NAME }
        #
        # return { 'host' : self.mHost_ip ,
        #          'user' :  self.mId ,
        #          'password' : self.mPw ,
        #          'database' : self.mDB_NAME ,
        #         'charset' : self.mCharset ,
        #          'use_unicode' : self.mUse_unicode }

        #

class cPostgresqlProperty( cMysqlProperty ):
    def __init__(self , *args , **kwargs ):
        cMysqlProperty.__init__( *args , **kwargs )
        cDBProperty.__init__(self, E_DB.POSTGRESQL)

class cOracleProperty(cDBProperty):

    # tnsinfo ex) "id\passwd@db"
    def __init__(self , tns_info ):
        cDBProperty.__init__(self,E_DB.ORACLE )
        #print "---------------------------cOracleProperty :: init"
        self.mTnsInfo = tns_info

    def ConnectInfo(self):
        # print "cOracleProperty::ConnectInfo mDB_Type " , cDBProperty.mDB_Type
        return self.mTnsInfo


class cIgniteProperty(cDBProperty):
    def __init__(self, *args, _schema='PUBLIC'):
        cDBProperty.__init__(self, E_DB.IGNITE)
        self.mArgs = args
        self.schema = _schema

    def GetArgs(self):
        return self.mArgs

    def GetKwargs(self):
        return self.schema
""")

print(f"점수: {result.score}/10")
print(f"문제점: {result.issues}")
