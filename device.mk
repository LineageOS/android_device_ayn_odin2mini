#
# SPDX-FileCopyrightText: The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

# Lights
PRODUCT_PACKAGES += \
    android.hardware.light-service.lineage

# Overlay
PRODUCT_PACKAGES += \
    Frameworks-Odin2Mini-Overlay \
    LineageSDK-Odin2Mini-Overlay \
    SettingsProvider-Odin2Mini-Overlay

# Soong namespaces
PRODUCT_SOONG_NAMESPACES += \
    $(LOCAL_PATH)

# Inherit from the common OEM chipset makefile.
$(call inherit-product, device/ayn/qcs8550-common/common.mk)

# Inherit from the proprietary files makefile.
$(call inherit-product, vendor/ayn/odin2mini/odin2mini-vendor.mk)
