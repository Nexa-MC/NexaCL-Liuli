# Liuli / 琉璃

NexaCL 的独立 NTP/1 主题。主题源文件位于 [theme/](theme/)，沿用 `nexa.liuli` 作为安装 ID。

从 [GitHub Releases](https://github.com/Nexa-MC/NexaCL-Liuli/releases/latest) 下载 `.ntp` 文件，然后在 NexaCL 的「设置 → 外观与主题 → 导入主题包」中选择它。已有同 ID 主题可原位升级，现有选项由启动器保留。

在仓库根目录执行 `python eng/build.py`。需要 Python 3.12 或更新版本。构建在 `dist/` 生成主题包和 `SHA256SUMS`。发布时先提交 `theme/theme.json` 中的版本，再推送同版本的 `v<version>` 标签。GitHub Actions 校验版本、打包并发布附件。

通用主题运行时、格式和外部主题预览入口由 [NexaCL 主仓](https://github.com/Nexa-MC/NexaCL/blob/main/docs/themes.md) 维护。主题效果、兼容性及参考来源见 [主题说明](theme/README.md)。本仓采用 Apache-2.0 许可证。
