from typing import Optional
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

import random  # randomライブラリを追加

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/omikuji")
def omikuji():
    omikuji_list = [
        "大吉",
        "中吉",
        "小吉",
        "吉",
        "半吉",
        "末吉",
        "末小吉",
        "凶",
        "小凶",
        "大凶"
    ]

    return omikuji_list[random.randrange(10)]

### コードいろいろ... ###

@app.get("/index")
def index():
    html_content = """
    <html lang="ja">
	    <head>
		    <meta charset="UTF-8">
		    <title>時間割2026-前期</title>
    	</head>
	    <body>
		    <table border="1">
	    		<thead>
	    			<tr>
	    				<th>後期時間割</th>
	    				<th colspan="2">月曜日</th>
	    				<th colspan="2">火曜日</th>
	    				<th colspan="2">水曜日</th>
	    				<th colspan="2">木曜日</th>
	    				<th colspan="2">金曜日</th>
	    			</tr>
	    		</thead>
	    		<tbody>
	    			<tr>
	    				<th rowspan="2">1限</th>
	    				<td colspan="2"></td>
	    				<td colspan="2"></td>
	    				<td colspan="2">情報技術基礎および演習</td>
		    			<td colspan="2"></td>
		    			<td colspan="2">ネットワーククラウド開発</td>
	    			</tr>
            <tr>
              <td colspan="2"></td>
              <td colspan="2"></td>
              <td><a href="https://els.sa.dendai.ac.jp/webclass/course.php/202611069324010101/?acs_=5d08dcd1"
	    					target="_blank" rel="nooperner noreferrer">Webclass</a></td>
	    				<td><a href="https://dendai.zoom.us/j/96349918951?pwd=cXoGaU0xgdy16PbuobnXAJ55g1kTZr.1"
	    		    			target="_blank" rel="nooperner noreferrer">Zoom</a></td> 
            <td colspan="2"></td>
            <td><a href="https://cpslab.notion.site/2026-33bfddc337a18170aef1cd09e2d27ee7"
		    				target="_blank" rel="noopener noreferrer">Page</a></td>
		    			<td><a href="https://tdu.app.box.com/folder/375717412110"
	    					target="_blank" rel="noopener noreferrer">Box</a></td>
           </tr>
    				<tr>
    					<th rowspan="2">2限</th>
    					<td colspan="2">情報メディア基礎ゼミ</td>
	    				<td colspan="2">ヒューマンインタラクション</td>
	    				<td colspan="2">データベースプログラミング演習</td>
	    				<td colspan="2">自然言語処理</td>
	    				<td colspan="2">ネットワーククラウド開発演習</td>
    				</tr>
          <tr>
            <td colspan="2"><a href="https://els.sa.dendai.ac.jp/webclass/course.php/202611069114010101/?acs_=dc94293d"
    						target="_blank" rel="noopener noreferrer">Webclass</a></td>
           <td colspan="2"><a href="https://els.sa.dendai.ac.jp/webclass/course.php/202611069714010101/?acs_=a7d905a0"
    						target="_blank" rel="nooperner noreferrer">Webclass</a></td>
           <td colspan="2"><a href="http://www.cue.im.dendai.ac.jp/%7Emasuda/ji/sql/sql2026.html"
    						target="_blank" rel="noopener noreferrer">Page</a></td>
    					<td><a href="https://els.sa.dendai.ac.jp/webclass/course.php/202611112114010101/?acs_=e227a57f"
	    					target="_blank" rel="nooperner noreferrer">Webclass</a></td>
            <td><a href="https://dendai.zoom.us/j/97286411580?pwd=ZTI00MHvfGJbc1fjjeMoMo9MqayLZB.1"
    						target="_blank" rel="noopener noreferrer">Zoom</a></td>
           <td><a href="https://cpslab.notion.site/2026-33bfddc337a18170aef1cd09e2d27ee7"
	    					target="_blank" rel="noopener noreferrer">Page</a></td>
	    				<td><a href="https://tdu.app.box.com/folder/375717412110"
	    					target="_blank" rel="noopener noreferrer">Box</a></td>
         </tr>
	    			<tr>
    					<th rowspan="2">3限</th>
    					<td colspan="2">知的処理および演習</td>
    					<td colspan="2"></td>
	    				<td colspan="2"></td>
	    				<td colspan="2">人工知能</td>
    					<td colspan="2">インタラクティブメディアとデザイン</td>
    				</tr>
           <tr>

             <td colspan="2"><a href="https://www.mlab.im.dendai.ac.jp/intelligent/"
    						target="_blank" rel="nooperner noreferrer">Page</a></td>
             <td colspan="2"></td>
             <td colspan="2"></td>
    					<td colspan="2"><a href="https://els.sa.dendai.ac.jp/webclass/course.php/202611104914010101/?acs_=f1770a5a"
    						target="_blank" rel="noopener noreferrer">Webclass</td>
            <td><a href="https://els.sa.dendai.ac.jp/webclass/course.php/202611080414010101/?acs_=861e305a"
    						target="_blank" rel="noopener noreferrer">Webclass</td>
	    				<td><a href="https://dendai.zoom.us/j/93597327887?pwd=ckI1b1FaTVR1dWFnRE0vWjM1c1VmZz09">Zoom</a></td>
            </tr>
	    			<tr>
			    		<th rowspan="2">4限</th>
	    				<td colspan="2">情報システム設計論</td>
		    			<td colspan="2"></td>
	        			<td colspan="2"></td>
    					<td colspan="2">暗号セキュリティと暗号技術</td>
	    				<td colspan="2"></td>
		    		</tr>
           <tr>
	    				<td><a href="https://els.sa.dendai.ac.jp/webclass/course.php/202611112714010101/?acs_=9bc78ebb"
	    					target="_blank" rel="noopener noreferrer">Webclass</a></td>
             <td><a href="https://tdu.app.box.com/folder/376321664752"
	    					target="_blank" rel="nooperner noreferrer">Box</a></td>
	    				<td colspan="2"></td>
              <td colspan="2"></td>
           <td colspan="2"><a href="https://els.sa.dendai.ac.jp/webclass/course.php/202611041114010101/?acs_=3ab3d288"
	    					target="_blank" rel="nooperner noreferrer">Webclass</a></td>
		    			<td colspan="2"></td>
           </tr>
				    <tr>
					    <th rowspan="2">5限</th>
				    	<td colspan="2"></td>
				     	<td colspan="2"></td>
			    		<td colspan="2"></td>
		    			<td colspan="2"></td>
		    			<td colspan="2"></td>
	    			</tr>
            <tr></tr>
			    </tbody>
		    </table>
	    </body>
    </html>

    """
    return HTMLResponse(content=html_content, status_code=200)

@app.post("/present")
async def give_present(present):
    code_list = list()
    for c in present:
        code_list.append(ord(c))
    return {"response": f"サーバです。メリークリスマス！ {present}ありがとう。プレゼントの文字コードは{code_list}でした。"}  # f文字列というPythonの機能を使っている