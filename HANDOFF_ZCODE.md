# Pagemi — Zcode 接力入口

更新：2026-10-18

请先读 [当前交接](docs/PAGEMI_HANDOFF.md)、[线上部署与预算](docs/HANDOFF_GOOGLE_CLOUD.md) 和 [实测记录](docs/VALIDATION.md)。本文件取代早期 AI Studio 免费层与旧版部署指令。

- 名称统一使用 **Pagemi**，读作 **PAGE-mee**
- 本地入口：`/Users/joeyzhao/Documents/Pagemi`
- 公开仓库：https://github.com/joeymilano/pagemi
- 正式演示：https://pagemi.joeyzhao.cc
- 视觉 Deck 与素材：`docs/pitch-deck-v2/`
- 视频制作：`docs/video-kit/START_HERE_OPUS.md`
- 官方模板：`docs/submission/Pagemi_Official_Template_2026-10-18.pptx` 与 PDF
- 完整素材包：`output/Pagemi_Creative_Kit_2026-10-18.zip`

## 接下来

完成真实功能演示视频，补入公开链接，再核对并提交比赛表单。Pagemi 简介、公开仓库链接与官方 PDF 已填入当前浏览器表单，但没有提交回执；不要把填表等同提交。

人工语义评分、商家访谈和真人任务测试仍待完成。现有数据只支持已测流程结论，不支持收益、退货率或市场验证结论。

## 运行约束

使用官方 Vertex AI。用户允许的新增模型调用现金预算为 1 美元，已有大部分用量；不得重置费用账本或提高额度。云服务计费保持已批准状态，不能套用旧文件里的解绑指令。密钥不得进入聊天、日志或仓库。

底层云项目与服务 ID 保留原值，避免中断网址和存储。不要对基础设施标识进行全局替换。历史测试原件不可改写；本轮名称变更改变了提示词哈希，不代表重新完成了实测。
