echo  'KERNEL=="ttyUSB*", ATTRS{idVendor}=="067b", ATTRS{idProduct}=="2303", MODE:="0777", GROUP:="dialout",  SYMLINK+="keysi_base"' >/etc/udev/rules.d/keysi_base.rules

service udev reload
sleep 2
service udev restart
