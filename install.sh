#!/data/data/com.termux/files/usr/bin/bash

echo "[*] Updating Termux..."
pkg update -y

echo "[*] Installing Python..."
pkg install python -y

echo "[*] Installing rehanzx tool..."

cp rehanzx.py $PREFIX/bin/rehanzx
chmod +x $PREFIX/bin/rehanzx

echo ""
echo "✅ rehanzx successfully installed!"
echo "✅ Ab sirf likho: rehanzx"
echo ""
