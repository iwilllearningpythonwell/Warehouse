import requests

class baimap:
    """
    https://blog.csdn.net/weixin_43105618/article/details/90700411?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-5.nonecase&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-5.nonecase
    http://lbsyun.baidu.com/apiconsole/key/create
    """
    def __init__(self,address):
        self.address = address


    def dmaps(self):
        base = url = "http://api.map.baidu.com/geocoder?address=" + self.address + "&output=json&key=f247cdb592eb43ebac6ccd27f796e2d2"
        response = requests.get(base)
        answer = response.json()
        return answer['result']['location']['lng'], answer['result']['location']['lat']


if __name__=='__main__':
    a=baimap("北京市昌平区定泗路99号").dmaps()
    print(a)