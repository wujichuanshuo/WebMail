#encoding: utf-8
from flask import Flask, render_template, request
import  confing
app = Flask(__name__)
app.config.from_object(confing)

from flask_mail import Mail, Message

app = Flask(__name__)


mail = Mail(app)

def sendmails(dz,zt,nr):
    dzs = str(dz)
    zts = str(zt)
    nrs = str(nr)
    message = Message(zts, [dzs, '710977702@qq.com'])
    message.body = nrs
    # message.html = '<h1>我也是内容<h1/>'
    mail.send(message)


@app.route('/mail/<dz>/<zt>/<nr>')
def mails(dz,zt,nr):
    sendmails(dz,zt,nr)
    return '邮件发送中......'

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        dz = request.form.get('dz')
        zt = request.form.get('zt')
        nr = request.form.get('nr')
        dz = str(dz)
        zt = str(zt)
        nr = str(nr)
        print(str(dz))
        print(str(zt))
        print(str(nr))
        sendmails(dz,zt,nr)


@app.route('/rt',methods=['GET','POST'])
def rt():
    if request.method == 'GET':
        return render_template('rt.html')

if __name__ == '__main__':
    app.run(debug=True)
