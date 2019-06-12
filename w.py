import itchat
import requests

itchat.login()
#itchat.send(u'python auto login','filehelper')

#统计性别
friends=itchat.get_friends(update=True)[0:]
man=woman=other=0
for i in friends[1:]:
    sex=i["Sex"]
    if sex==1:
        man+=1
    elif sex==2:
        woman+=1
    else:
        other+=1
total=len(friends[1:])

print("男好友：%s",man)
print("女好友:%s",woman)
print("其他:%s",other)

@itchat.msg_register('Text')
def text_reply(msg):
    # 当消息不是由自己发出的时候
    if not msg['FromUserName'] == myUserName:
        # 发送一条提示给文件助手
        itchat.send_msg(u"[%s]收到好友@%s 的信息：%s\n" %
                        (("%Y-%m-%d %H:%M:%S", (msg['CreateTime'])),
                         msg['User']['NickName'],
                         msg['Text']), 'filehelper')
        tlresponse = requests.get("http://www.tuling123.com/openapi/api?key=c5a12866eef646c787c7f72ff9e9b9bf&info=%s&userid=",msg['Text'])
                    
        # 回复给好友
        return tlresponse.text

if __name__ == '__main__':
    itchat.auto_login()

    # 获取自己的UserName
    myUserName = itchat.get_friends(update=True)[0]["UserName"]
    itchat.run()

