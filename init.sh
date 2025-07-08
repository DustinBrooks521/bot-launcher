#!/bin/bash
echo "[+] Setting up environment directories..."
mkdir -p logs
touch config.json

echo "[+] Creating basic config..."
cat <<EOF > config.json
{
  "enable_scraper_bot": true,
  "enable_clip_bot": true,
  "enable_monitor_bot": true,
  "enable_cronk_bridge": true
}
EOF
