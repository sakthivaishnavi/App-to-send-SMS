import streamlit as st
import socket

def send_sms_via_udp(ip, port, message):
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        udp_socket.sendto(message.encode(), (ip, int(port)))
        return f"Message sent to {ip}:{port}"
    except Exception as e:
        return f"Failed to send message: {str(e)}"
    finally:
        udp_socket.close()

st.title("SMS Sending App")
st.write("This app sends SMS over UDP. Just enter the IP address, port, and your message to send.")

ip = st.text_input("Recipient IP Address", placeholder="e.g., 192.168.1.1")
port = st.text_input("Recipient Port", placeholder="e.g., 5000")
message = st.text_area("Message", placeholder="Type your SMS here...")

if st.button("Send SMS"):
    if ip and port and message:
        result = send_sms_via_udp(ip, port, message)
        st.success(result)
    else:
        st.warning("Please fill out all fields before sending.")
