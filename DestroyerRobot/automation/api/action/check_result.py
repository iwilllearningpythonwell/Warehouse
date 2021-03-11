from DestroyerRobot.automation.util.JosnUtil import JsonUtils
class CheckResult():
    """
    responseData:判断实际响应结果与预期结果是否一致
    exceptResponse ：
    """
    @classmethod
    def check(self, responseData, exceptResponse):
        if isinstance(responseData ,str):
            responseData = eval(responseData)
        if isinstance(exceptResponse , str):
            exceptResponse = eval(exceptResponse)
        for key, value in exceptResponse.items():
            if key in responseData:
                if responseData[key] == value:
                    responseResult = 1
                else:
                    responseResult = 0
                    return responseResult
            else:
                responseResult = 0
                return responseResult
        return responseResult

if __name__ == "__main__":
    r =  {'code': 200, 'msg': '成功', 'data': {'id': 90, 'code': None, 'userName': '13600000001', 'roleName': None, 'token': '4c3ff365-4f45-4798-98da-ea6ff33a6e01', 'loginName': '13600000001', 'loginSysName': 'bonus', 'menus': None, 'extend': {'id': 90, 'userName': '13600000001', 'jobNumber': '12344321', 'companyName': '优选好生活科技（珠海）有限公司', 'mobile': '13600000001', 'email': '1317@sina.com', 'pswd': '58323dbea8b88b453ff18d4aac3844c5', 'createTime': 1508314932000, 'lastLoginTime': 1599902037000, 'status': 1, 'cityId': 110100, 'roleId': 118, 'roleName': '运营人员', 'clientId': '60c5f16391d0cffe8de3e9f0846cf5ba'}, 'openId': None}}
    c = '{"code":200,"msg":"成功"}'

    print(CheckResult.check(r, c))
