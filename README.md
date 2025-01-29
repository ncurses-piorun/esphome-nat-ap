# esphome-nat-ap
Repeater component for Esphome and esp-idf framework.
This custom ESPHome component based on https://github.com/mag1024/esphome-nat-ap.git implements WIFI repeater/extender functionality
for ESP32s. Specifically, it runs a SoftAP (in addition to the existing wifi connection), and configures it to perform NAT. Only works with the `esp-idf` framework (not Arduino).

> **_Warning:_** very hacky.

Usage:
```
esphome:
  ...
external_components:
  - source: github://ncurses-piorun/esphome-nat-ap@main

esp32:
  board: esp32dev
  framework:
    type: esp-idf
    sdkconfig_options:
      CONFIG_COMPILER_OPTIMIZATION_SIZE: y
      CONFIG_LWIP_IP_FORWARD: y
      CONFIG_LWIP_IPV4_NAPT: y

wifi:
  ...
  ap:
    ssid: "Fallback Hotspot"
    password: "W5Lqyert5u1r"
    ap_timeout: 0s

nat_ap:
  id: nat1
  ssid: "my_ssid"
  password: !secret wifi_password
```
