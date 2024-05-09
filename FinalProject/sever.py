import http.client
import http.server
import json
from pathlib import Path
import termcolor
import socketserver
import jinja2 as j

PORT = 8080
socketserver.TCPServer.allow_reuse_address = True
def data(ENDPOINT):
    server = "rest.ensembl.org"
    params = "?content-type=application/json"
    url = server + ENDPOINT + params

    print(f"Server {server}")
    print(f"URL {url}")

    conn = http.client.HTTPConnection(server)

    try:
        conn.request("GET", ENDPOINT + params)
    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()

    response = conn.getresponse()
    print(f"Response received!: {response.status} {response.reason}\n")
    data1 = response.read().decode("utf-8")
    person = json.loads(data1)
    return person

class Seq:
    def __init__(self, gene):
        self.gene = gene

    def get_sequence(self):
        person = data("/lookup/symbol/homo_sapiens/" + self.gene)
        name = person["id"]
        person1 = data("sequence/id/" + name)
        seq = person1["seq"]
        return seq
    def seq_len(self):
        seq = self.get_sequence()
        return len(seq)

    def count(self, base):
        seq = self.get_sequence()
        base_count = seq.count(base)
        percentage = round((base_count/len(seq) * 100), 2)

        return base + ": " + str(base_count) + " (" + str(percentage) + "%)"

class TestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        termcolor.cprint(self.requestline, 'green')
        request = self.requestline.split(" ")
        action = request[1]
        application_type = ""
        content_type = "html"
        if "?" in request[1]:
            separate = request[1].split("?")
            action, instruction = separate[0], separate[1]
            if "json=1" in request[1]:
                application_type = separate[2]

        def read_html_file(filename):
            contents = Path("html/" + filename).read_text()
            contents = j.Template(contents)
            return contents

        def name_spe(specie):
            specie = specie.replace("+", " ").strip().lower()
            specie_all = ""
            person = data("/info/species")
            for i in person["species"]:
                if i["display_name"].lower() == specie.lower():
                    specie_all = i["name"]
            return specie_all

        def json_file(name, filename):
            json_dict = {}
            if type(name) == list:
                for index, content in enumerate(name):
                    json_dict[index] = content
            elif type(name) == str or type(name) == int:
                json_dict["1"] = name
            elif type(name) == dict:
                json_dict = name
            with open(filename, "w") as f:
                json.dump(json_dict, f)
                f.close()

            contents = Path(filename).read_text()
            content_type = 'application/json'
            return contents, content_type

        if action == "/" or action == "/index.html":
            content_type = "html"
            contents = open("index.html").read()
        elif action == "/listSpecies":
            person = data("/info/species")
            total = len(person["species"])
            number = total
            if instruction != "limit=":
                number = instruction[6:]
                number = int(number)
            names = []
            for i in range(number):
                name = person["species"][i]["common_name"].capitalize()
                names.append(name)
            if application_type == "json=1":
               contents, content_type = json_file(names, "listSpecies.json")
            else:
                contents = read_html_file("listSpecies.html").render(context={"total": total, "number": number, "list": names})
        elif action == "/karyotype":
            specie = instruction[8:]
            chromosomes = []
            sci_specie = name_spe(specie)
            if sci_specie:
                person1 = data("/info/assembly/" + sci_specie)
                if person1["karyotype"]:
                    for chrom in person1["karyotype"]:
                        chromosomes.append(chrom)
                else:
                    chromosomes = "We could not find the karyotype"
                if application_type == "json=1":
                    contents, content_type = json_file(chromosomes, "karyotype.json")
                else:
                    contents = read_html_file("karyotype.html").render(context={"chromosomes": chromosomes})
            else:
                contents = open("/html/error.html").read()
        elif action == "/chromosomeLength":
            chromosomerequest = instruction.split("&")
            specie = chromosomerequest[0][8:]
            number = chromosomerequest[1][7:]
            sci_specie = name_spe(specie)
            if sci_specie:
                person1 = data("/info/assembly/" + sci_specie)
                length = person1["top_level_region"][int(number)]["length"]
                if application_type == "json=1":
                    contents, content_type = json_file(length, "chromosomeLength.json")
                else:
                    contents = read_html_file("chromosomeLength.html").render(context={"length": length})
            else:
                contents = open("/html/error.html").read()

        elif action == "/geneSeq":
            gene = instruction[5:]
            s = Seq(gene)
            sequence = s.get_sequence()
            gene_dict = {"gene": gene, "sequence": sequence}
            if application_type == "json=1":
                contents, content_type = json_file(gene_dict, "geneSeq.json")
            else:
                contents = read_html_file("geneSeq.html").render(context=gene_dict)
        elif action == "/geneInfo":
            gene = instruction[5:]
            s = Seq(gene)
            person = data("/lookup/symbol/homo_sapiens/" + gene)
            start, end, name = person["start"], person["end"], person["id"]
            length = s.seq_len()
            chromosomes_dict = {"gene": gene, "start": start, "end": end, "length": length, "id": name}
            if application_type == "json=1":
                contents, content_type = json_file(chromosomes_dict, "geneInfo.json")
            else:
                contents = read_html_file("geneInfo.html").render(context=chromosomes_dict)
        elif action == "/geneCalc":
            gene = instruction[5:]
            s = Seq(gene)
            length = s.seq_len()
            bases = ["A", "G", "T", "C"]
            results = []
            for i in bases:
                base = s.count(i)
                results.append(base)
            calc_dict = {"gene": gene, "length": length, "results": results}
            if application_type == "json=1":
                contents, content_type = json_file(calc_dict, "geneCalc.json")
            else:
                contents = read_html_file("geneCalc.html").render(context=calc_dict)
        elif action == "/geneList":
            information = instruction.split("&")
            chromosome = information[0][7:]
            start = information[1][6:]
            end = information[2][4:]
            person = data("/phenotype/region/homo_sapiens/" + chromosome + ":" + start + "-" + end)
            names = []
            for i in range(len(person)):
                names.append(person[i]["id"])
            list_dict = {"chromosome": chromosome, "start": start, "end": end, "names": names}
            if application_type == "json=1":
                contents, content_type = json_file(list_dict, "geneList.json")
            else:
                contents = read_html_file("geneList.html").render(context=list_dict)
        elif self.requestline.startswith("GET /favicon.ico"):
            contents = ""


        self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', content_type)
        self.send_header('Content-Length', len(contents.encode()))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(contents.encode())

        return

Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()