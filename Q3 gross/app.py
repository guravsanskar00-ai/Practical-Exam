from  flask import Flask, render_template
app = Flask(__name__)
empid=101
empname="John Doe"
department="IT"
basic_salary=50000
hra=basic_salary*0.2
da=basic_salary*0.12
ta=basic_salary*0.8
pf=basic_salary*0.1
gross_salary=basic_salary+hra+da+ta
net_salary=gross_salary-pf

@app.route("/")
def home():
    return render_template("salary.html", empid=empid, empname=empname, department=department, basic_salary=basic_salary, hra=hra, da=da, ta=ta, pf=pf, gross_salary=gross_salary, net_salary=net_salary)
if __name__ == "__main__":
    app.run(debug=True)