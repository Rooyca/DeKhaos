from flask import Flask, url_for, render_template
import  requests

app = Flask(__name__)

regions = { "BC":"https://cdnruneterra.ar/assets/img/region/BandleCity.png",
			"BW":"https://cdnruneterra.ar/assets/img/region/Bilgewater.png",
			"DE":"https://cdnruneterra.ar/assets/img/region/Demacia.png",
			"FR":"https://cdnruneterra.ar/assets/img/region/Freljord.png",
			"IO":"https://cdnruneterra.ar/assets/img/region/Ionia.png",
			"NX":"https://cdnruneterra.ar/assets/img/region/Noxus.png",
			"PZ":"https://cdnruneterra.ar/assets/img/region/PiltoverZaun.png",
			"SI":"https://cdnruneterra.ar/assets/img/region/ShadowIsles.png",
			"SH":"https://cdnruneterra.ar/assets/img/region/Shurima.png",
			"MT":"https://cdnruneterra.ar/assets/img/region/Targon.png"}

@app.route('/', methods=['GET'])
def home():
	api_re = requests.get('https://api.rooyca.xyz/v1/random/lordeck').json()
	deck_regions = api_re["description"]["regions"]
	data = {"regions":deck_regions,
			"url_1":regions[deck_regions.split('/')[0]],
			"url_2":regions[deck_regions.split('/')[1]],
			"deck_code":api_re["description"]["deckCode"]
	}
	return render_template('home.html', data=data)

if __name__ == "__main__":
	app.run(debug=True)
