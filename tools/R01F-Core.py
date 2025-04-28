import subprocess
import json
import time
from datetime import datetime
import os

gmer01f = "/etc/xray/config.json"
trafficuser = "/etc/qos/limit/quota.json"
serverip = "127.0.0.1:10085"
trafficcache_user = "/etc/qos/limit/traffic_cache.json"

def has_config(last_mtime, gmer01f):
    try:
        current_mtime = os.path.getmtime(gmer01f)
        if current_mtime != last_mtime:
            return current_mtime
        return last_mtime
    except FileNotFoundError:
        print(f"File konfigurasi tidak ada: {gmer01f}")
        return last_mtime

def email_user(file_path):
    try:
        with open(file_path, "r") as file:
            config_data = json.load(file)
            clients_data = {}
            for inbound in config_data.get("inbounds", []):
                if "clients" in inbound["settings"]:
                    for client in inbound["settings"]["clients"]:
                        if "email" in client:
                            email = client["email"]
                            protocol = inbound["tag"]
                            if protocol not in clients_data:
                                clients_data[protocol] = []
                            clients_data[protocol].append({
                                "user": email,
                                "uplink": 0,
                                "downlink": 0,
                                "total": 0,
                                "last_updated": None
                            })
            return clients_data
    except FileNotFoundError:
        print(f"File konfigurasi tidak ada: {file_path}")
        return {}
    except json.JSONDecodeError:
        print(f"Error membaca file konfigurasi: {file_path}")
        return {}
def query_api(pattern):
    try:
        result = subprocess.run(
            ["xray", "api", "statsquery", f"--server={serverip}", f"--pattern={pattern}"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        data = json.loads(result.stdout)
        return data.get("stat", [])
    except Exception as e:
        print(f"Error API : {e}")
        return []
def load_trafficdata(file_path):
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("File trafik tidak ditemukan, inisialisasi file baru.")
        return {}
    except json.JSONDecodeError:
        print("Error membaca file JSON. File akan diinisialisasi ulang.")
        return {}
def load_trafficcache():
    try:
        with open(trafficcache_user, "r") as file:
            data = json.load(file)
            if isinstance(data, dict):
                return data
            else:
                print("Cahche trafik tidak valid, menginisialisasi cache baru.")
                return {}
    except FileNotFoundError:
        print("Cache trafik tidak ada, inisialisasi cache baru.")
        return {}
    except json.JSONDecodeError:
        print("Error membaca cahche trafik. Cache akan diinisialisasi ulang.")
        return {}
def save_trafficdata(trafficuser, traffic_data):
    try:
        with open(trafficuser, "w") as file:
            json.dump(traffic_data, file, indent=4)
    except Exception as e:
        print(f"Error menyimpan data trafik: {e}")

def save_trafficache(traffic_cache):
    try:
        with open(trafficcache_user, "w") as file:
            json.dump(traffic_cache, file, indent=4)
    except Exception as e:
        print(f"Error menyimpan cache trafik ke file JSON: {e}")

def client_in_trafik(traffic_data, clients_data):
    for protocol, clients in clients_data.items():
        if protocol not in traffic_data:
            traffic_data[protocol] = []
        if not isinstance(traffic_data[protocol], list):
            traffic_data[protocol] = []
        for client in clients:
            if isinstance(client, dict) and "user" in client:
                user_email = client["user"]
                if not any(existing_client["user"] == user_email for existing_client in traffic_data[protocol]):
                    traffic_data[protocol].append(client)
    for protocol, clients in traffic_data.items():
        clients = list(clients)
        for client in clients[:]:
            if isinstance(client, dict) and "user" in client:
                user_email = client["user"]
                found_in_config = any(client["user"] == email for protocol_data in clients_data.values() for email in [c["user"] for c in protocol_data])
                if not found_in_config:
                    traffic_data[protocol].remove(client)

def menginisialisasi_traffic():
    traffic_data = load_trafficdata(trafficuser)
    traffic_cache = load_trafficcache()
    clients_data = email_user(gmer01f)
    if not traffic_data:
        traffic_data = clients_data
        save_trafficdata(trafficuser, traffic_data)
        print("Data trafik baru berhasil disalin")
    
    return traffic_data, clients_data, traffic_cache


def record_traffic():
    last_config_mtime = 0
    traffic_data, clients_data, traffic_cache = menginisialisasi_traffic()
    
    while True:
        print("Memulai pencatatan trafik...")
        last_config_mtime = has_config(last_config_mtime, gmer01f)
        if last_config_mtime:
            print("membaca ulang...")
            clients_data = email_user(gmer01f)
        uplink_stats = query_api("uplink")
        downlink_stats = query_api("downlink")
        client_in_trafik(traffic_data, clients_data)
        for stat in uplink_stats:
            if "name" in stat and stat["name"].startswith("user>>>"):
                user_email = stat["name"].split(">>>")[1]
                uplink_value = int(stat.get("value", 0))
                previous_uplink = traffic_cache.get(f"{user_email}_uplink", 0)
                delta_uplink = max(0, uplink_value - previous_uplink)
                traffic_cache[f"{user_email}_uplink"] = uplink_value
                print(f"Uplink Update: {user_email} - Delta: {delta_uplink}")
                for protocol, clients in traffic_data.items():
                    for client in clients:
                        if client["user"] == user_email:
                            client["uplink"] += delta_uplink
                            client["total"] += delta_uplink
                            client["last_updated"] = datetime.now().isoformat()

        for stat in downlink_stats:
            if "name" in stat and stat["name"].startswith("user>>>"):
                user_email = stat["name"].split(">>>")[1]
                downlink_value = int(stat.get("value", 0))
                previous_downlink = traffic_cache.get(f"{user_email}_downlink", 0)
                delta_downlink = max(0, downlink_value - previous_downlink)
                traffic_cache[f"{user_email}_downlink"] = downlink_value
                print(f"Downlink Update: {user_email} - Delta: {delta_downlink}")
                
                for protocol, clients in traffic_data.items():
                    for client in clients:
                        if client["user"] == user_email:
                            client["downlink"] += delta_downlink
                            client["total"] += delta_downlink
                            client["last_updated"] = datetime.now().isoformat()
        save_trafficdata(trafficuser, traffic_data)
        save_trafficache(traffic_cache)
        
        print(f"Data trafik telah disimpan")
        time.sleep(5)

if __name__ == "__main__":
    record_traffic()