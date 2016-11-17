from flask import Flask, render_template
from cim_client import *


app = Flask(__name__)

#url for loading page: usually localhost:PORT/<<app.route(link)>>
#@app.route("/cim_info")
#def hello():
#        return render_template('cim.html')

@app.route("/cim_info")
def get_cim_info():
	os = get_OS_info()
	#test = atest()
	atest = "abdd"
	return render_template('cim.html', atest=atest, os=os)
'''
	return render_template('cim.html', **{
	'test' : test,
        'os_info': os,
	
})'''

if __name__ == "__main__":
            app.run(debug=True)
