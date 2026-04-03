import requests
import http.server
import socketserver
import webbrowser
import os
# 这个模块用于爬取网页内容并解析HTML标签。
#记忆战队 from honkai star rail
sc1="https://fastcdn.hoyoverse.com/content-v2/hkrpg/155153/a1a9ef0c725b1a0769a5cc8f09c4b5fe_1287956239496454957.png" #主c
sc2="https://fastcdn.hoyoverse.com/content-v2/hkrpg/155819/365635a3493e9523cf3c3769e0169721_4924415025585271982.png" #治疗
sc3="https://fastcdn.hoyoverse.com/content-v2/hkrpg/159043/9afd392f1b8068e06832559fe4163529_3491875745193218742.png" #副c
sc4="https://fastcdn.hoyoverse.com/content-v2/hkrpg/160346/54fb37ea230e2f6b9b7cc8a12e79329b_1607694867232341960.png" #辅助
bg_sc1="https://4kwallpapers.com/images/wallpapers/honkai-star-rail-4320x2160-24493.jpg" #背景图
html_content = f"""<!DOCTYPE html>
<html lang="zh">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>记忆战队</title>
    <rel="stylesheet" href="stylecss">
    <style>
    body{{
    font-size: 20px;
     background-color: #f0f0f0;
     font-family: Arial, sans-serif;
     background-image: url("{bg_sc1}");
     background-size: cover;
        background-position: center;
        background-attachment: fixed;
        background-repeat: no-repeat;
    }}
    h1{{
     color: #333; padding: 20px;
    }}
    img{{
     border-radius: 20px;
        margin: 20px;
    }}
    span{{
        font-size:50px;
        color: pink;
        text-align: center;
    }}
    </style>
</head>
<body>
<div class="container">
<h1>记忆战队</h1>
<div class="team">
<img src="{sc1}" referrerpolicy="no-referrer" alt="主C" width="200">
<span>遐蝶</span>
<br>
<img src="{sc2}" referrerpolicy="no-referrer" alt="治疗" width="200">
<span>风堇</span>
<br>
<img src="{sc3}" referrerpolicy="no-referrer" alt="副C" width="200">
<span>长夜月</span>
<br>
<img src="{sc4}" referrerpolicy="no-referrer" alt="辅助" width="200">
<span>昔涟</span>
</div>
</body>
</html>"""
with open("memory team.html", "w", encoding="utf-8") as f:
    f.write(html_content) # 将生成的HTML内容写入文件，文件名为"memory team.html"，使用UTF-8编码保存
PORT=8000 # 定义服务器监听的端口号，这里设置为8000
Handler=http.server.SimpleHTTPRequestHandler # 创建一个HTTP请求处理器，使用Python内置的SimpleHTTPRequestHandler类
print(f"Serving at port {PORT}") # 打印服务器正在监听的端口号
webbrowser.open(f"http://localhost:{PORT}/memory team.html") 
# 使用webbrowser模块打开默认浏览器，并访问本地服务器上的"memory team.html"页面
with socketserver.TCPServer(("", PORT), Handler) as httpd: # 创建一个TCP服务器，绑定到指定的端口，
    #并使用之前定义的Handler处理请求
    print("Server started at http://localhost:{PORT}") # 打印服务器启动成功的消息
    httpd.serve_forever() # 启动服务器，进入无限循环，等待并处理客户端请求
