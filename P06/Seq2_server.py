from Seq1 import Seq
import os
import http.server
import socketserver
import termcolor
from pathlib import Path

# Define the Server's port
PORT = 8080

# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inherits all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        termcolor.cprint(self.requestline, 'green')

        # IN this simple server version:
        # We are NOT processing the client's request
        # It is a happy server: It always returns a message saying
        # that everything is ok

        # Message to send back to the client
        if self.requestline.startswith("PING"):
            contents = "Access to the Server. Is the server alive ?"
        else:
            contents = Path("../S14/error.html").read_text()

        # Generating the response message
        self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'html')
        self.send_header('Content-Length', len(contents.encode()))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(contents.encode())

        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
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

    def what_appears_on_clients(self, msg):
        if msg == "PING":
            print("Ping command!\nOK!")
            return "OK"

        elif msg.startswith("GET"):
            GENES = ["U5", "RNU6_269P", "FXN", "FRAT1", "ADA"]
            for gene in GENES:
                index = GENES.index(gene)
                if 0 <= index <= 4:
                    if msg == f"GET {index}":
                        s = Seq()
                        s.seq_read_fasta(os.path.join("..", "sequences", gene))
                        termcolor.cprint("GET", 'green')
                        print(str(s))
                        return str(s)

        elif msg.startswith("INFO"):
            gene = msg.split(" ")
            gene = gene[1]
            seq = Seq(gene)
            total_len = seq.seq_len()
            len = total_len
            c_a = f"A: {seq.seq_count_base('A')} ({((seq.seq_count_base('A') / total_len) * 100)}%)"
            c_g = f"G: {seq.seq_count_base('G')} ({((seq.seq_count_base('G') / total_len) * 100)}%)"
            c_c = f"C: {seq.seq_count_base('C')} ({((seq.seq_count_base('C') / total_len) * 100)}%)"
            c_t = f"T: {seq.seq_count_base('T')} ({((seq.seq_count_base('T') / total_len) * 100)}%)"
            print(f"Sequence: {seq}\nTotal length: {len}\n{c_a}\n{c_g}\n{c_c}\n{c_t}")
            return f"Sequence: {seq}\nTotal length: {len}\n{c_a}\n{c_g}\n{c_c}\n{c_t}"

        elif msg.startswith("COMP"):
            gene = msg.split(" ")
            gene = gene[1]
            seq = Seq(gene)
            termcolor.cprint("COMP", 'green')
            print(seq.seq_complement())
            return seq.seq_complement()

        elif msg.startswith("REV"):
            gene = msg.split(" ")
            gene = gene[1]
            seq = Seq(gene)
            termcolor.cprint("REV", 'green')
            print(seq.reverse())
            return seq.reverse()

        elif msg.startswith("GENE"):
            gene = msg.split(" ")
            gene = gene[1]
            genes = ["U5", "FRAT1", "FXN", "RNU6_269P", "ADA"]
            if gene in genes:
                termcolor.cprint("GENE  ", 'green')
                s = Seq()
                s.seq_read_fasta(os.path.join("..", "sequences", gene))
                print(str(s))
                return str(s)
