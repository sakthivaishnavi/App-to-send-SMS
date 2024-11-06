import streamlit as st
import socket
import threading
import time

def receive_messages(port):
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind(('0.0.0.0', port))  
    messages = []

    while True:
        try:
            data, addr = udp_socket.recvfrom(1024)  
            messages.append(f"Received message from {addr}: {data.decode()}")
            yield messages 
        except Exception as e:
            st.error(f"Error receiving message: {e}")
            break

st.title("Message Receiver")

port = st.number_input("Enter Port", value=5000, min_value=1, max_value=65535)

if st.button("Start Receiving"):
    messages = [] 
    message_generator = receive_messages(port)

  
    for msg in message_generator:
        messages = msg 
        st.write(messages)  
        time.sleep(1)  

