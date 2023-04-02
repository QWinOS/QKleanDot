#!/usr/bin/env bash
set -euo pipefail

muted=$(pulsemixer --id source-1 --get-mute)
if [[ "$muted" == "0" ]]; then
  echo "" > /tmp/micvol-icon
else
  echo "" > /tmp/micvol-icon
fi
