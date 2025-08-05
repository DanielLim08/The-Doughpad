# The-Doughpad
This is a 8 key macropad with a rotary encoder. I wanted to have a lot of macros, hence the increased key number, along with the rotary encoder for additional versatility when assigning macros.
# Features
EC11 Rotary encoder 
2 WS2812B RGB LEDs
8 Keys
1 Case

I have just recently started with Fusion360, and have never interacted with KiCAD or firmware before, so most of this design process was pretty new to me! However, I found it a great first project (both in terms of KiCAD and Fusion), and a great way for me to familiarize myself with both KiCAD and Fusion360.

# CAD Model:
<img width="445" height="533" alt="Doughpad_Case_CAD_Design" src="https://github.com/user-attachments/assets/7ff9ab6d-ad45-442a-b48c-6267886bab97" />

I made my CAD model in Fusion360, and it has a basic top and bottom for the macropad. Everything fits inside the top and bottom case parts.

# PCB Design:
Schematic:
<img width="850" height="442" alt="PCD_Schematic" src="https://github.com/user-attachments/assets/2bd3ff07-510a-4803-a1ca-04e2cb11da70" />

PCB:
<img width="333" height="397" alt="PCB" src="https://github.com/user-attachments/assets/676fad18-7533-4916-9919-1f0534a8412b" />

I designed my PCB on KiCAD. 

# Firmware:
I used KMK for my firmware.
The rotary encoder changes volume, and each of the 8 keys has a specific function, some were just there from the original code, while others I added because I thought that they would be useful. (COPY & PASTE).

BOM:
Amount| Item                      |
-----------------------------------
  8   |Cherry MX Switches         |
-----------------------------------
  2   |SK6812 MINI Leds           |
-----------------------------------
  1   |XIAO RP2040                |
-----------------------------------
  1   |EC11 Rotary Encoder        |
-----------------------------------
  8   |DSA Keycaps                |
-----------------------------------
  4   |M3x16mm screws             |
-----------------------------------
  4   |M3 hex nuts                |
-----------------------------------
  9   |Through-hole 1N4148 Diodes |
-----------------------------------
  1   |Case (2 printed parts)     |
-----------------------------------


