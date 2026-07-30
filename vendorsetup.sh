#!/bin/bash

PATCH_DIR="device/oplus/op6893/patches"

# Restore patches
restore_device_patches() {
    if [ -d "$PATCH_DIR" ]; then
        cd hardware/oplus && git restore . && cd -
    fi
}

# Apply patches
apply_device_patches() {
    if [ -d "$PATCH_DIR" ]; then
        for PATCH in "$PATCH_DIR"/*.patch; do
            [ -e "$PATCH" ] || continue
            echo "Applying $PATCH..."
            git apply "$PATCH"
        done
    fi
}

restore_device_patches
apply_device_patches
