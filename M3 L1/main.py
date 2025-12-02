from flask import Flask,render_template
import random as r
app = Flask(__name__)
reals=["2019'da yapılan bir araştırmaya göre, insanların %60'ından fazlası akıllı telefonlarındaki iş mesajlarına işten ayrıldıktan sonraki 15 dakika içinde yanıt veriyor.","Elon Musk, sosyal ağların içeriği görüntülemek için mümkün olduğunca fazla zaman harcamamız için bizi platformun içinde tutmak üzere tasarlandığını iddia ediyor.","Teknolojik bağımlılıkla mücadele etmenin bir yolu, zevk veren ve ruh halini iyileştiren faaliyetler aramaktır.","Sosyal ağların olumlu ve olumsuz yanları vardır ve bu platformları kullanırken her ikisinin de farkında olmalıyız."]
@app.route("/")
def hello_world():
    return render_template("index.html")
@app.route("/goober")
def hiloo():
    return "<h1>HI IM A GOOBER</h1>"
@app.route("/gercekler")
def gercekler():
    return f"<h2>{r.choice(reals)}</h2>"
@app.route("/yazi_tura")
def yazi_tura():
    chos=r.randint(0,1)
    if chos==0:
        choosed="tura"
    else:
        choosed="yazı"
    return f"<h1>{choosed}</h1>"
app.run(debug=True)