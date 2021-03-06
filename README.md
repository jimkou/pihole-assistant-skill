# <img src="https://raw.githack.com/FortAwesome/Font-Awesome/master/svgs/solid/ad.svg" card_color="#D81159" width="50" height="50" style="vertical-align:bottom"/> Pihole Assistant
Control your pihole with your voice

## About
With pihole assistant you can control many pihole commands. 
Just use the word "Advertisements" or "Advertisement" and then the desired command as listed below:

## Examples
* advertisements enable (pihole enable)
* advertisements disable (pihole disable)
* advertisements restart dns (pihole restart dns)
* advertisements status (pihole status)
* advertisements flush   (pihole flush)     
* advertisements stats or statistics (returns some pihole stats)
* advertisements update gravity (pihole -g)
## Requirements
* Mycroft-core and Pihole.
* Python3.
#### Standard python3 libraries
* json.
* requests.
* num2word.

## Manual Installation
```sh
$ git clone https://github.com/jimkou/pihole-assistant-skill.git /opt/mycroft/skills/pihole-assistant-skill
```
### Important Note
If Pihole is installed in another machine then:
```sh
$ nano /opt/mycroft/skills/pihole-assistant-skill/__init__.py
```
And edit the following fields:
* remote_mode (Set to "YES")
* pihole_ip (Set the IP of the machine that pihole is running on)
* api_token (Set the api token that is located in "/etc/pihole/setupVars.conf")

## Category
**Daily**
Configuration
Productivity

## Tags
#Raspberry
#Pihole
#Ads

