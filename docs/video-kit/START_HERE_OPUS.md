# Pagemi — Opus 5.5 production handoff

更新：2026-10-18，上海时间。交付的是导演方案和素材，不是已完成的视频。用户已指定由 Opus 5.5 接力制作，不需要重新讨论选题。

## 直接执行的任务

制作 **3:15、16:9、1920×1080、30 fps、全英文旁白与字幕** 的 AI Builder Cup 演示片。名字暂定 **“The mistake is still live.”** 前 5 秒抓人，15 秒内看见产品，主体必须看清真实操作。保留 2:55 短版剪辑能力。

- 产品：https://merchreflex-927668522599.asia-southeast1.run.app
- 源码：https://github.com/joeymilano/pagemi
- 仓库根目录：`/Users/joeyzhao/Documents/Pagemi`
- 本素材包：`docs/video-kit/`
- 首先打开 `STORYBOARD.html`，再读 `DIRECTOR_SCRIPT.md`、`CAPTURE_PLAN.md`。
- `timeline.json` 是 195 秒主版的统一时间轴，包含旁白、画面、声效及证据。英文台词在 `VOICEOVER_EN.md`。
- `assets/manifest.json` 给出素材出处、是否历史版本及 SHA-256。不能把 historical 目录的白色旧界面当作当前深色版本。

## 决定观众是否记得的三个瞬间

1. **0:00–0:05：工单关闭，错误仍在。** “Resolved” 快速盖章，画面后面的 “100% waterproof” 留在原位。声音突然收窄。字幕：The ticket is closed. / The mistake is still live. 这是开场叙事包装，不是产品拥有工单系统的证据。
2. **1:19–1:38：批准也会过期。** 用真实 UI 演示新增规格后原批准失效。镜头停在实际的 Outdated 状态，绿色连接线断开。不要臆造界面中不存在的 409 弹窗。
3. **1:56–2:34：修改真正落地，还能恢复。** 先批准，再发布，打开实际店铺、刷新、复查，然后恢复旧版本。页面变化是高潮。版本递增，绝不做倒放伪装回滚。

## 风格与取舍

保留产品的深绿近黑背景、奶白文字、薄荷绿强调色、Manrope 标题和 DM Sans 正文。片头是冷静的商业悬疑感，主体像精密仪器的操作录像。镜头、焦点和声音负责酷炫，不用机器人、地球网络、代码雨、无意义三维旋转或满屏粒子。

画面阅读优先。功能段至少 100 秒主要显示真实产品界面。每个关键结果停留 3–5 秒。放大可以，改写截图文字不可以。UI 放大采用 1.0×→1.12×平移；2.5D 只用于片头平面构图。禁止快速高亮频闪。

## 关键约束

- 2026-10-18 约20:28上海时间核对：提交表单正文和视频字段都写 **3–4 minutes**。旧文档“字段不超过3分钟”已过时。公开 FAQ 仍写 under 3 minutes，冲突未获主办方澄清。**主版 3:15 是按当前专用表单作出的制作选择，不是主办方给了豁免。** 短版2:55保留作备用。
- 当时 Roadmap 显示截止 **10/19 02:29 CST**，约剩6小时；提交页同一钟点却标 IST。内部按较早的上海02:29处理，优先今晚完成。
- 用户批准的本轮新增模型现金上限是 **USD 1**。18:08上海时间快照已保守记账约0.6966美元，工作流额度剩0.2034美元，外加少量诊断。此后可能已有访客消耗。**没有新增预算授权，不能重置账本、提高限额、反复跑付费评估或购置视频服务。** 拍摄前只读核对当前额度。网页 Run audit 和 Reassess 都会产生真实调用。
- 该预算不足以保证整个评审期持续可用。记录并请用户另行决定维护预算；不能把“已部署”写成“已保障到11/7”。
- 保留失败记录。最终发布版连续5次完整流程通过；之前修订有2次504失败。35项本地测试不是35次真人测试。没有商家采访、没有已测业务增长、没有已完成人工准确率评分。
- 产品图片、规格、客户反馈是合成示例，画面保留可读的说明。Merchant-confirmed 不等于第三方认证。
- 只有 `assets/current` 的三张图是本轮现场截取的当前界面，且都在**未运行审查**状态。它们不能证明 AI 成功运行。真实模型响应摘录和测试报告另附。
- 不可把 `output/` 整目录公开：可能含 session、CSRF、密钥设置截图。不要读取或显示 `.env.local` 的值。

## 交付验收

1. `Pagemi_AI_Builder_Cup_3m15.mp4`：H.264/AAC，1080p，30fps，195秒目标，英语字幕烧录，同时交付英文SRT。
2. 可编辑项目，旁白/音乐/声效分轨，所有素材有来源。
3. 完整真实操作原始录像（内部保存），剪辑点清单，等待时间加速标识。
4. 6张成片关键帧，逐镜对照真实功能和证据。
5. 三项关键证明均能看清：来源支撑、批准失效、发布后读取与恢复。
6. 发布公开视频后用无登录窗口确认可播放，再将链接补入官方模板Deck第14页与提交清单。当前没有公开视频，也未提交。

优先顺序：录制两段真实审查与完整发布链 → 旁白和剪辑 → 字幕与混音 → 公共播放验证 → 更新Deck视频链接。制作包装不能挤占真实演示时间。

## Pagemi visual update · 18 October 2026

Use **Pagemi** (PAGE-mee) throughout. The latest art direction and deck are in `../pitch-deck-v2/`. Reuse its original PNG artwork, short slide labels and lime/black palette. New brand visuals are conceptual; record the actual Pagemi interface for product behavior. Old branded exports remain archives.
