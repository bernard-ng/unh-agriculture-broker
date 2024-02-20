import socket
import json
import paho.mqtt.client as mqtt

# Configuration MQTT
broker_address = "192.168.43.208"
mqtt_port = 1883


class Publisher:
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect(('192.168.43.208', 12345))

    def publish(self, message):
        self.socket.send(message)

# # Configuration du socket pour accepter les données entrantes
# socket_host = '0.0.0.0'  # Écoute sur toutes les interfaces réseau
# socket_port = 12345  # Port pour le serveur socket
#
# # Création et configuration du serveur socket
# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server_socket.bind((socket_host, socket_port))
# server_socket.listen(5)
# print(f"Écoute sur toutes les interfaces réseau, port {socket_port} pour les données entrantes...")
#
# while True:
#     # Accepter une nouvelle connexion
#     conn, addr = server_socket.accept()
#     print(f"Connecté à {addr}")
#
#     # Recevoir des données de la connexion
#     data = conn.recv(1024)  # Ajustez la taille du buffer si nécessaire
#
#     if not data:
#         break
#
#     # Décoder les données JSON reçues et extraire le topic et le message
#     json_data = json.loads(data.decode())
#     topic = json_data['topic']  # Assurez-vous que les données JSON contiennent un champ 'topic'
#     message = json_data['message']  # et un champ 'message'
#
#     # Publier le message sur le topic MQTT
#     client.publish(topic, message)
#
#     # Fermer la connexion
#     conn.close()
#
# # Fermer le serveur socket
# server_socket.close()
