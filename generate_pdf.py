from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML
import os
import datetime
import re



def generate_pdf(data):
    files = os.listdir("./output")

    version_list =[]
    for x in files:
        matches = re.findall(r"v(\d+)",x)
        for y in matches:
            version_list.append(int(y))

    file_name = "./output/Model_poznawczy_raport_"+datetime.date.today().strftime("%Y_%m_%d") + "_v"
    if version_list ==[]:
        version=1
    else:
        version=max(version_list)+1


    while os.path.exists(file_name + str(version) + ".pdf"):
        version+=1

    output_path = file_name+str(version)+".pdf"
    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template("report_template.html")


    html_out = template.render(data)

    HTML(string=html_out).write_pdf(output_path)
    return output_path