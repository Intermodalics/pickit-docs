.. attention::
  When communicating with KUKA robots, the Pickit server IP address cannot belong to the following IP ranges:

  - 169.254.0.0 to 169.254.255.255
  - 192.168.0.0 to 192.168.0.255
  - 172.16.0.0 to 172.16.255.255
  - 172.17.0.0 to 172.17.255.255

  The default Pickit server IP is **169.254.5.180**, which belongs to the first range, so it must be modified.