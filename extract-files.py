#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)
from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.fixups_lib import (
    lib_fixups,
    lib_fixups_user_type,
)

namespace_imports = [
    'device/oplus/op6893',
    'hardware/google/interfaces',
    'hardware/google/pixel',
    'hardware/mediatek',
    'hardware/mediatek/libmtkperf_client',
    'hardware/oplus',
]

def lib_fixup_odm_suffix(lib: str, partition: str, *args, **kwargs):
    return f'{lib}_{partition}' if partition == 'odm' else None

def lib_fixup_vendor_suffix(lib: str, partition: str, *args, **kwargs):
    return f'{lib}_{partition}' if partition == 'vendor' else None

lib_fixups: lib_fixups_user_type = {
    **lib_fixups,
    (
        'libadsprpc',
        'vendor.oplus.hardware.performance@1.0',
        'libstdc++',
        'android.hardware.graphics.allocator@2.0',
        'android.hardware.graphics.allocator@3.0',
        'android.hardware.graphics.allocator@4.0',
        'libcamera_core_hwi',
        'libocam_common',
        'liboplus_platform_hwi',
        'vendor.oplus.hardware.cammidasservice@1.0',
        'vendor.oplus.hardware.biometrics.fingerprint@2.1',
        'vendor.oplus.hardware.commondcs@1.0',
        'android.hardware.keymaster-V3-ndk_platform',
        'libneuron_runtime',
    ): lib_fixup_odm_suffix,
    (
        'vendor.mediatek.hardware.videotelephony@1.0',
        'vendor.oplus.hardware.radio-V1-ndk_platform',
    ): lib_fixup_vendor_suffix,
}

blob_fixups: blob_fixups_user_type = {
    'system_ext/lib64/libimsma.so': blob_fixup()
        .replace_needed('libsink.so', 'libsink-mtk.so'),
    'vendor/bin/hw/vendor.mediatek.hardware.pq@2.2-service': blob_fixup()
        .replace_needed('libutils.so', 'libutils-v32.so')
        .replace_needed('libhidlbase.so', 'libhidlbase-v32.so'),
    'vendor/lib64/hw/vendor.mediatek.hardware.pq@2.15-impl.so': blob_fixup()
        .replace_needed('libutils.so', 'libutils-v32.so')
        .replace_needed('libtinyxml2.so', 'libtinyxml2-v34.so'),
    'vendor/lib*/hw/audio.primary.mt6893.so': blob_fixup()
        .replace_needed('libalsautils.so', 'libalsautils-v31.so')
        .replace_needed('libtinyalsa.so', 'libtinyalsa-v32.so'),
    ('vendor/bin/hw/android.hardware.media.c2@1.2-mediatek',
    'vendor/bin/hw/android.hardware.media.c2@1.2-mediatek-64b'): blob_fixup()
        .replace_needed('libavservices_minijail_vendor.so', 'libavservices_minijail.so')
        .add_needed('libcodec2_hidl@1.0.so')
        .add_needed('libshim.so')
        .add_needed('libstagefright_foundation-v33.so'),
    'vendor/bin/hw/mtkfusionrild' : blob_fixup()
        .add_needed('libutils-v32.so'),
    'vendor/bin/mtk_agpsd': blob_fixup()
        .replace_needed('libcrypto.so', 'libcrypto-v32.so')
        .replace_needed('libssl.so', 'libssl-v32.so'),
    'vendor/lib64/libmtkcam_featurepolicy.so': blob_fixup()
        .sig_replace('34 E8 87 40 B9', '34 28 02 80 52'),
    'vendor/bin/hw/android.hardware.wifi@1.0-service-lazy': blob_fixup()
        .replace_needed('libwifi-hal.so', 'libwifi-hal-mtk.so'),
    'system/lib*/libem_support_jni.so': blob_fixup()
        .add_needed('libjni_shim.so'),
    'vendor/lib64/hw/sensors.mt6893.so': blob_fixup()
        .add_needed('libsensors_shim.so'),
    ('vendor/lib*/libaalservice.so',
    'vendor/lib64/libcam.utils.sensorprovider.so',
    'vendor/lib64/liboplus_mtkcam_lightsensorprovider.so'): blob_fixup()
        .replace_needed('libsensorndkbridge.so', 'libsensorndkbridge-v30.so'),
    ('vendor/bin/hw/android.hardware.neuralnetworks@1.3-service-mtk-neuron',
    'vendor/lib*/libnvram.so',
    'odm/bin/hw/vendor.oplus.hardware.charger@1.0-service',
    'vendor/lib*/libsysenv.so'): blob_fixup()
        .add_needed('libbase_shim.so'),
    'odm/bin/hw/vendor.oplus.hardware.cammidasservice@1.0-service': blob_fixup()
        .replace_needed('libhidlbase.so', 'libhidlbase-v32.so'),
    'vendor/lib64/hw/hwcomposer.mt6893.so': blob_fixup()
        .add_needed('libprocessgroup_shim.so')
        .binary_regex_replace(
            b'OnScreenFingerprintPressedIcon',
            b'SurfaceView[UdfpsControllerOve'
    ),
    'vendor/lib64/libmtkcam_stdutils.so': blob_fixup()
        .replace_needed('libutils.so', 'libutils-v32.so'),
    'vendor/bin/hw/camerahalserver': blob_fixup()
        .replace_needed('libutils.so', 'libutils-v32.so')
        .replace_needed('libbinder.so', 'libbinder-v32.so')
        .replace_needed('libhidlbase.so', 'libhidlbase-v32.so'),
    'vendor/lib64/hw/android.hardware.camera.provider@2.6-impl-mediatek.so': blob_fixup()
        .replace_needed('libutils.so', 'libutils-v32.so')
        .replace_needed('libhidlbase.so', 'libhidlbase-v32.so')
        .add_needed('libcamera_metadata_shim.so'),
    'odm/lib*/libui_oplus.so': blob_fixup()
        .replace_needed('android.hardware.graphics.common-V2-ndk_platform.so', 'android.hardware.graphics.common-V2-ndk.so'),
    'vendor/lib*/libmtkisp_metadata.so': blob_fixup()
        .replace_needed('libui.so', 'libui_oplus.so'),
    'vendor/lib64/libsensor_custom.so': blob_fixup()
        .binary_regex_replace(b'android.sensor.wise_light', b'android.sensor.light\x00\x00\x00\x00\x00')
        .sig_replace('5B 00 01 00', '05 00 00 00'),
    ('vendor/lib64/lib3a.sensors.color.so',
    'vendor/lib64/lib3a.sensors.flicker.so',
    'vendor/lib*/libaaa_ltm.so',
    'vendor/lib64/lib3a.ae.stat.so',
    'vendor/lib64/lib3a.flash.so',
    'vendor/lib64/libSQLiteModule_VER_ALL.so'): blob_fixup()
        .add_needed('liblog.so'),
}  # fmt: skip

module = ExtractUtilsModule(
    'op6893',
    'oplus',
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
)

if __name__ == '__main__':
    utils = ExtractUtils.device(module)
    utils.run()
