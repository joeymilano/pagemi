# Pagemi 接力说明

更新：2026-10-18，上海时间

## 名称

正式名称 **Pagemi**，读作 **PAGE-mee**。产品界面、源码包名、模型身份、演示材料和 GitHub 仓库全部采用此名称。工作入口为 `/Users/joeyzhao/Documents/Pagemi`（兼容原目录的链接）。云项目展示名已更新；底层项目 ID、服务 ID、公共运行地址与历史测试记录保留原值。

## 当前成果

- 新视觉 Deck：`docs/pitch-deck-v2/`，16 页，黑白/柠檬绿，六张大图、开源图标、图表与流程动效。
- 网页版：`output/pitch-deck-v2/Pagemi_Visual_Pitch_2026-10-18.html`，独立离线文件，含动效。
- 静态版：同目录 `Pagemi_Visual_Pitch_2026-10-18.pdf`，小于 5 MB。
- 官方模板：`docs/submission/Pagemi_Official_Template_2026-10-18.pptx` 及 PDF，保留原模板结构，已更名。此版本与视觉 Deck 分开使用。
- 视频脚本、英文旁白、SRT、分镜及现有截图已统一 Pagemi；入口 `docs/video-kit/START_HERE_OPUS.md`。
- 图像生成原稿、提示词及 Phosphor MIT 图标许可证保存在视觉 Deck 目录。

## 线上状态

- URL：https://pagemi.joeyzhao.cc
- 名称版本：`merchreflex-00023-fow`，100% 流量
- UI、P 图标、健康接口、包名和模型身份均已统一；提示词哈希改变，决策规则、存储和预算未改
- 35 项本地测试、构建及类型检查通过；候选健康、标题和图标检查通过后切流。此前已验证公网示例会话和工作台，本次未重跑付费模型流程
- 本轮未启动 Gemini 审查，不消耗新增模型调用预算
- 原有“五次完整流程”的数据来自 `merchreflex-00018-mib`，不是本轮重新测试结果

## 视频制作

优先打开 `docs/pitch-deck-v2/OPUS_HANDOFF.md`。用网页 Deck 观察图像慢推、扫描线和图表入场。金属回环与雨滴织物是概念图，不能作为商品性能证明。仍需录制真实模型返回、证据更新导致批准失效、发布、读取页面与回滚。

本轮的动效预览只是 Deck 展示，不是参赛演示视频。正式视频链接仍未填写，不得当作已经提交。

## 未完成

1. 真实演示视频、公开视频链接与最终提交回执
2. 人工语义评分、商家任务测试与访谈
3. 比赛表单已填入 Pagemi 简介、新仓库链接、官方 PDF 和 Retail & Commerce 分类；视频待补，未提交，无成功回执
4. 长期品牌域名、商标检索；初步网络搜索不等于名称权利可用

## 文案要求

标题不加句号，优先 2–6 个词。用具体动作和实测数字，避免 trust、empower、transform 等空泛口号。生成图、历史截图和未完成测试只保留必要的短标签，详情放交接文档。

## Public domain update

The public entry is https://pagemi.joeyzhao.cc. Cloudflare forwards to the existing Google Cloud Run application without redirecting the browser. Gemini, Firestore and image storage remain on Google Cloud. Two full synthetic workflows passed through the new domain, including model generation, approval, publication, served-page verification and rollback. Measured post-preflight durations were 52.192 and 23.728 seconds. These are domain-integration checks, not new semantic grading. The earlier no-model-call statements refer only to the prior name-only release.
