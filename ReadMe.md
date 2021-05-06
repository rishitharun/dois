# Denial of Internet Service Attack

### Script to virtually disconnect a victim network device from the gateway in a LAN

**Developer** - [Rishi Tharun](https://linkedin.com/in/rishitharun03) - <<vrishitharunj@gmail.com>><br>

>NOTE:
> * Target system is **Linux** only - Not portable
> * Root access is required to run
> * Requires **Python 3.x**


#### About the script
This script is used to perform an attack on a fellow network device in a LAN, by means of ARP Spoofing. When the attack is successfully executed, the victim device will be cut off from the gateway of the LAN, thus cut off from the internet.



#### Pre-requisites
We must be connected to the LAN, in which the victim is connected

#### How this works
Our Script will initially poison the victim's ARP table. It will replace the gateway's MAC with a spoof MAC provided by us. When the victim tries to make a network connection, it will send out an ARP request, to identify the gateway. Since the gateway MAC is modified in the ARP table, it will not respond to the ARP request. If we simply drop the packet, after three attempts, the victim will send a broadcast to identify the gateway, for which the gateway will respond to the request, and connection will be established between the gateway and the victim. So, we will respond to each ARP request sent by the victim, and thus disconnecting the victim from the gateway until the script stops
