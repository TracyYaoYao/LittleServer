from flask import Flask, render_template, request, redirect
from service import tinyurlSvc

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tinyurl')
def tinyurl():
    return render_template('tinyurl.html')

@app.route('/api/tinyurl/encode', methods=['POST', 'GET'])
def tinyurlEncode():
    url = request.form['text']
    if not url.startswith('http') or not url.startswith('https'):
        return "ERROR: url must start with http / https"
    return tinyurlSvc.tinyurlSvcImpl().EncodeURL(url)

@app.route('/api/tinyurl/decode', methods=['POST', 'GET'])
def tinyurlDecode():
    turl = request.form['text']
    return tinyurlSvc.tinyurlSvcImpl().DecodeURL(turl)

@app.route('/r/<string:turl>')
def tinyurlRedirect(turl):
    return redirect(tinyurlSvc.tinyurlSvcImpl().SearchURL(turl), 302)

# if __name__=='__main__':
#     app.config['SERVER_NAME'] = 'kiki.binacs.cn'
#     app.run('0.0.0.0', debug=True, port=5000)
#     app.run('0.0.0.0', debug=True, port=8100, ssl_context=('your_path/XXXX.pem', 'your_path/XXXX.key'))

# import http.server
# import socketserver
# import ipaddress
# import argparse
# import sys
# import os
#
# VERSION=1.0
# PORT=8888
# IP='0.0.0.0'
#
# def start_web_server(ip,port,root):
#     Handler=http.server.SimpleHTTPRequestHandler
#     print("pyWebServer v{}".format(VERSION),'by HanselSoft')
#     print('start web server at {} : {}, root dir={}'.format(ip,port,root))
#
#     try:
#         os.chdir(root)
#         with socketserver.TCPServer((ip,port),Handler) as httpd:
#             httpd.serve_forever()
#     except Exception as e:
#         print("Error: ",e)
#         sys.exit(-2)
#
# def main():
#     parse=argparse.ArgumentParser()
#     parse.add_argument('--port','--p',type=int,help='server port number, defaulr is {}'.format(PORT),default=PORT)
#     parse.add_argument('-ip','-i',help='bind to address,defalut is {}'.format(IP),default=IP)
#     parse.add_argument('--dir','--d',help='web server root directory, default is current \directory', default=os.getcwd() + '/templates')
#     args=parse.parse_args()
#
#     try:
#         ipaddress.ip_address(args.ip)
#     except ValueError:
#         print('error : incorrect IP:',args.ip)
#         sys.exit(-1)
#
#     if not os.path.isdir(args.dir):
#         print("error:diretory '{}' is not existed.".format(args.dir))
#         sys.exit(-1)
#     start_web_server(args.ip,args.port,args.dir)
#
# if __name__=='__main__':
#     try:
#         main()
#     except(KeyboardInterrupt,SystemExit):
#         sys.exit(0)