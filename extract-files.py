#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#


from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)

from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

namespace_imports = [
    'vendor/ayn/qcs8550-common',
]

blob_fixups: blob_fixups_user_type = {
    'vendor/etc/display/qdcm_calib_data_xm91080_video_mode_dsi_panel_without_DS.json': blob_fixup()
        .regex_replace('nt35532_video_mode_dsi_panel_without_DSC', 'xm91080_video_mode_dsi_panel_without_DSC'),
}  # fmt: skip

module = ExtractUtilsModule(
    'odin2mini',
    'ayn',
    blob_fixups=blob_fixups,
    namespace_imports=namespace_imports,
    add_firmware_proprietary_file=True,
)

if __name__ == '__main__':
    utils = ExtractUtils.device_with_common(
        module, 'qcs8550-common', module.vendor
    )
    utils.run()
