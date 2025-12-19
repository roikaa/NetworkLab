from netmiko import ConnectHandler, NetmikoTimeoutException,
NetmikoAuthenticationException
import logging
logging.basicConfig(level=logging.INFO)
device = {
"device_type": "cisco_ios",
"host": "192.168.1.2", # IP de SW2
"username": "admin",
"password": "cisco",
"secret": "cisco" # Enable password si nécessaire
}
try:
    with ConnectHandler(**device) as conn:
        output = conn.send_command("show etherchannel summary")

        if "P" in output and "Po1" in output:
            print("✅ EtherChannel est actif et tous les ports sont bundled.")
            logging.info("EtherChannel OK")
        else:
            print("⚠️ EtherChannel non actif ou ports non bundled.")
            logging.warning("Vérifiez les configurations LACP")

except (NetmikoTimeoutException, NetmikoAuthenticationException) as e:
    print(f"❌ Erreur de connexion : {e}")
    logging.error(f"Connexion échouée : {e}")
