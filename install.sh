#!/data/data/com.termux/files/usr/bin/bash

clear
echo "[+] Updating Termux..."
pkg update -y

echo "[+] Installing Python & Git..."
pkg install python git -y

echo "[+] Installing Python Requirements..."
pip install requests
pip install pyfiglet
pip install rich

echo "[+] Setting permissions..."
chmod +x rehanzx.py
chmod +x rehanzx_old.py

echo "[+] Installing launcher & old tool..."

# ✅ Launcher install
cp rehanzx.py $PREFIX/bin/rehanzx

# ✅ Old tool bhi install hoga
cp rehanzx_old.py $PREFIX/bin/rehanzx_old.py

chmod +x $PREFIX/bin/rehanzx
chmod +x $PREFIX/bin/rehanzx_old.py

echo ""
echo "[✓] RehanzX Installed Successfully!"
echo "[✓] Run Tool using: rehanzx"
echo ""
