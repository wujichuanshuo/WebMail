import poplib, os.path, mimetypes
from email.parser import BytesParser, Parser
from email.policy import default
class ma:
    fo=''
    to=''
    ms=''
    def __init__(self,fo,to,ms):
        self.fo=fo
        self.to=to
        self.ms=ms
# 输入邮件地址, 口令和POP3服务器地址:
def pp3():
    email = '710977702@qq.com'
    password = 'ektbjesoxjimbcec'
    pop3_server = 'pop.qq.com'
    # 连接到POP 3服务器:
    #conn = poplib.POP3(pop3_server, 110)
    conn = poplib.POP3_SSL(pop3_server, 995)
    # 可以打开或关闭调试信息:
    conn.set_debuglevel(1)
    # 可选:打印POP 3服务器的欢迎文字:
    print(conn.getwelcome().decode('utf-8'))
    # 输入用户名、密码信息
    # 相当于发送POP 3的user命令
    conn.user(email)
    # 相当于发送POP 3的pass命令
    conn.pass_(password)
    # 获取邮件统计信息，相当于发送POP 3的stat命令
    message_num, total_size = conn.stat()
    print('邮件数: %s. 总大小: %s' % (message_num, total_size))
    # 获取服务器上的邮件列表，相当于发送POP 3的list命令
    # resp保存服务器的响应码
    # mails列表保存每封邮件的编号、大小
    resp, mails, octets = conn.list()
    print(resp, mails)
    # 获取指定邮件的内容（此处传入总长度，也就是获取最后一封邮件）
    # 相当于发送POP 3的retr命令
    # resp保存服务器的响应码
    # data保存该邮件的内容
    i=0
    a=list()
    for i in range(0,10):
        resp, data, octets  = conn.retr(len(mails)-i)
        # 将data的所有数据（原本是一个字节列表）拼接在一起
        msg_data = b'\r\n'.join(data)
        # 将字符串内容解析成邮件，此处一定要指定policy=default
        msg = BytesParser(policy=default).parsebytes(msg_data)       #①
        print(type(msg))
        print('发件人:' + msg['from'])
        print('收件人:' + msg['to'])
        print('主题:' + msg['subject'])

        #print('第一个收件人名字:' + msg['to'].addresses[0].username)
        #print('第一个发件人名字:' + msg['from'].addresses[0].username)
        for part in msg.walk():
            counter = 1
            # 如果maintype是multipart，说明是容器（用于包含正文、附件等）
            if part.get_content_maintype() == 'multipart' :
                continue
            # 如果maintype是multipart，说明是邮件正文部分
            elif part.get_content_maintype() == 'text':
                print(part.get_content())
                ma1=ma(msg['from'],msg['to'],part.get_content())
                a.append(ma1)
    # 退出服务器，相当于发送POP 3的quit命令
    conn.quit()
    for i in range(0, ):
        print(a[i].to + '     ' + a[i].fo + "        " + a[i].ms)
    return a
a=pp3()