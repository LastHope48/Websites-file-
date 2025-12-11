# İçe Aktarma
from flask import Flask, render_template, request


app = Flask(__name__)

def result_calculate(size, lights, device):
    # Elektrikli cihazların enerji tüketimini hesaplamaya olanak tanıyan değişkenler
    home_coef = 100
    light_coef = 0.04
    devices_coef = 5   
    return size * home_coef + lights * light_coef + device * devices_coef 

# İlk sayfa
@app.route('/')
def index():
    return render_template('index.html')
# İkinci sayfa
@app.route('/<size>')
def lights(size):
    return render_template(
                            'lights.html', 
                            size=size
                           )

# Üçüncü sayfa
@app.route('/<size>/<lights>')
def electronics(size, lights):
    return render_template(
                            'electronics.html',                           
                            size = size, 
                            lights = lights                           
                           )

# Hesaplama
@app.route('/<size>/<lights>/<device>')
def end(size, lights, device):
    return render_template('end.html', 
                            result=result_calculate(int(size),
                                                    int(lights), 
                                                    int(device)
                                                    )
                        )
# Form
@app.route('/form')
def form():
    return render_template('form.html')

#Formun sonuçları
@app.route('/submit_form', methods=['POST'])
def submit_form():
    # Veri toplama için değişkenleri tanımlayın
    name = request.form['name']
    date=request.form["date"]
    address=request.form["address"]
    email=request.form["email"]
    # Verilerinizi kaydedebilir veya e-posta ile gönderebilirsiniz
    with open('form.txt','a',encoding="utf-8") as f:
        f.write(name+"\n")
        f.write(date+"\n")
        f.write(address+"\n")
        f.write(email+"\n")
        f.write("FORM BİTİŞ"+"\n")
    return render_template('form_result.html', 
                           # Değişkenleri buraya yerleştirin
                           name=name,
                           date=date,
                           address=address,
                           email=email,
                           )
@app.route("/submit_form_pro", methods=["POST"])
def submit_form_pro():
    check_box_value=request.form["checkbox"]
    if check_box_value=="on":
        check_box_value_true="Evet"
    else:
        check_box_value_true="Hayır"
    return render_template("submit_pro_result.html",
            check_box_value_true=check_box_value_true)
app.run(debug=True)