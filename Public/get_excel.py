# coding=utf-8
import xlrd,os


def datacel(file_name,sheet=1,qbrow=6,endrow=99):
    # print(sheet)
    try:
        directpath = os.path.dirname(os.path.dirname(__file__))
        f = directpath+'/test_data/'+file_name
        file=xlrd.open_workbook(f)
        me=file.sheets()[sheet]
        nrows=me.nrows
        # print nrows
        # 测试用例ID
        listid=[]
        # 用例名称
        listcasename=[]
        # 预置条件
        listpreset=[]
        # 请求头信息
        listheader=[]
        # 依赖关系
        listdepend=[]
        # 请求参数
        listparame=[]
        # 请求url
        listurl=[]
        # 参数类型
        listpatype=[]
        # 请求方式
        listmethod=[]
        # 逾期结果
        listyq=[]
        # print listid
        for i in range(qbrow,nrows):
            if i == endrow:
                break
            listid.append(me.cell(i,0).value)
            listcasename.append(me.cell(i,2).value)
            listpreset.append(me.cell(i, 5).value)
            listheader.append(me.cell(i, 6).value.replace("\n","").replace(" ",""))
            listdepend.append(me.cell(i, 7).value.replace(" ",""))
            listurl.append(me.cell(i,8).value+me.cell(i,9).value)
            listparame.append(me.cell(i,10).value.replace("\n","").replace(" ",""))
            listpatype.append(me.cell(i,11).value)
            listmethod.append(me.cell(i,12).value)
            listyq.append(me.cell(i,13).value)
        # print(listsql)
        return listid,listcasename,listpreset,listheader,listdepend,listurl,listparame,listpatype,listmethod,listyq
    except Exception:
        pass


# for i in datacel('接口测试用例模板V1.0.xls',sheet=1):
#     print(i)
#     continue


def makedata(file_name,sheet):

    listid,listcasename,listpreset,listheader,listdepend,listurl,listparame,listpatype,listmethod,listyq = datacel(file_name,sheet=sheet)
    make_data=[]
    for i in range(len(listid)):
        # print listurl[i]
        make_data.append(
            {"id":listid[i],
             "casename":listcasename[i],
             "preset":listpreset[i],
             'header':listheader[i],
             'depend':listdepend[i],
             'url':listurl[i],
             'parame':listparame[i],
             'patype':listpatype[i],
             'method':listmethod[i],
             'yq':listyq[i],
             }
        )
    return make_data

# for i in makedata('接口测试用例模板V1.0.xls',1):
#     print(i)