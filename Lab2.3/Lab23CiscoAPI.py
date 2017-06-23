import requests, json, pprint
from flask import Flask,jsonify, render_template
import sys

controller = "devnetapi.cisco.com/sandbox/apic_em"

def new_ticket():
    url = 'https://sandboxapic.cisco.com/api/v1/ticket'
    payload = {"username": "devnetuser", "password": "Cisco123!"}
    header = {"content-type": "application/json"}
    response = requests.post(url, data=json.dumps(payload),headers=header, verify=False)
    return response.json()['response']['serviceTicket']

def get_host(ticket):
    url = "https://" + controller + "/api/v1/host?limit=1&offset=1"
    header = {"content-type": "application/json", "X-Auth-Token": ticket}
    response = requests.get(url, headers=header, verify=False)
    return response.json()


def get_dev(ticket):
    url = "https://" + controller + "/api/v1/network-device?limit=1&offset=1"
    header = {"content-type": "application/json", "X-Auth-Token": ticket}
    response = requests.get(url, headers=header, verify=False)
    return response.json()


def get_topology(ticket):
    url = "https://" + controller + "/api/v1/topology/physical-topology?limit=1&offset=1"
    header = {"content-type": "application/json", "X-Auth-Token": ticket}
    response = requests.get(url, headers=header, verify=False)
    return response.json()

app = Flask(__name__)

@app.route('/api/topology')
def web_topology():
        return jsonify(get_topology(ticket)['response'])


@app.route('/')
def index():
    return render_template("topology.html")


if __name__ == '__main__':

    ticket = new_ticket()
    print ("Ticket = ")
    pprint.pprint(ticket)

    print("Hosts = ")
    pprint.pprint(get_host(ticket))

    print("Network device = ")
    pprint.pprint(get_dev(ticket))

    print("Network topology = ")
    pprint.pprint(get_topology(ticket))

    app.run(debug=True)


