# Director script — The mistake is still live.

主片195秒，英语旁白，16:9。片头0–13秒是解释性视觉包装，13秒后尽快进入真实产品。

## 01 · 0:00–0:05 · The mistake is still live.

**画面：**概念开场：占画面三分之一的工单落下 Resolved 印章并抽走，露出背后的 100% waterproof。1.2秒停顿，然后切到仍亮着的错误承诺。右下小字 Illustrative scenario。

**旁白：** The ticket is closed. The mistake is still live.

**声音：**一次干净的盖章声；1.8秒切掉混响，留低频脉冲。

**证据：** `editorial illustration; original fixture in lib/fixtures.ts`

## 02 · 0:05–0:13 · One page. Two misunderstandings.

**画面：**实物感背包大图，细线框住水瓶；切成原页面承诺与商家规格对照。轻微推近，禁止伪造商品浸水试验。

**旁白：** The bottle looks included. The page promises waterproof protection. The specification says otherwise.

**声音：**玻璃质感轻触两次，低频节拍开始。

**证据：** `assets/brand/commuter-one-ai-generated.png; assets/current/03-live-specification.png`

## 03 · 0:13–0:24 · Pagemi

**画面：**3D包装快速压平为真实首页，1秒品牌落版后进入全屏桌面工作台。屏幕角落持续保留 Synthetic demo。

**旁白：** Pagemi turns customer confusion into evidence-linked page repairs. Here is the working prototype, running on Google Cloud.

**声音：**低音打开到宽立体声；品牌出现不额外爆炸。

**证据：** `assets/current/01-live-start.png; live recording required`

## 04 · 0:24–0:42 · Read the evidence.

**画面：**真实点击来源，放大规格关键句4秒，再看图片。Run audit实际点击与返回必须录到；如缩短等待，明确标 Analysis wait shortened。

**旁白：** Gemini reads feedback, merchant specifications, and the product image. Feedback identifies a problem. The specification supports product facts. An image can show a bottle, but cannot prove waterproof performance.

**声音：**微弱扫描音只沿来源连线移动，旁白下音乐降低。

**证据：** `Take A; lib/agent.ts; lib/fixtures.ts`

## 05 · 0:42–1:00 · Repair, ask, or hand off.

**画面：**三项实际问题依次选中，各停3–4秒，红色过度声明、琥珀色缺资料、灰色人工处理。不要给每条反馈都闪绿色勾。

**旁白：** The agent separates page problems from missing information and operational issues. It corrects the unsupported waterproof claim, asks for laptop dimensions, and leaves a broken zipper or late delivery for human action.

**声音：**有节制的三次状态声；没有成功庆祝音。

**证据：** `Take A; assets/evidence/real-response-excerpt.json`

## 06 · 1:00–1:19 · Every change has a source.

**画面：**真实前后差异与来源并排；将不支持的 waterproof 词组与受支持文字进行匹配剪辑。其余界面不扭曲。批准前保留人审复选框。

**旁白：** Each proposed change shows its source. A separate Gemini request checks the replacement text. Program rules restrict edits to three fields. Price, inventory, policies, and certifications stay outside the editing scope.

**声音：**细线连上时轻响；旁白读 source 时停留。

**证据：** `Take A; lib/agent.ts; lib/domain.ts`

## 07 · 1:19–1:38 · New evidence. Old approval expires.

**画面：**第一次真正批准之后补充规格。特写实际 Outdated 状态；外层批准连接线从绿变琥珀并断开。静止2秒让评委理解。

**旁白：** Approval applies to exact wording and exact evidence. When the merchant adds a new specification, that approval becomes outdated. The application requires a fresh assessment before publication.

**声音：**音乐抽空0.4秒；低而短的失效提示音，无刺耳警报。

**证据：** `Take B; domain invalidation tests; no final-prompt live clip yet`

## 08 · 1:38–1:56 · Dimensions, without an invented promise.

**画面：**录入32×23×3厘米的合成商家规格并重审。只有真实返回安全尺寸建议才展示成功；保留尺寸提示和未保证通用兼容的措辞。

**旁白：** We add measured sleeve dimensions. A new assessment can disclose those measurements and ask customers to check their device. Dimensions alone do not guarantee that every sixteen-inch laptop fits.

**声音：**节拍恢复，三段刻度线跟随真实尺寸；不画未测量的电脑适配。

**证据：** `Take B; historical screenshot is reference only`

## 09 · 1:56–2:18 · Approve. Publish. Read it back.

**画面：**至少12秒连续真实操作：勾选、批准、发布、打开页面、刷新、复查。其余6–10秒特写变更文字和实际版本；剪辑不能省略授权顺序。

**旁白：** Now the merchant reviews and approves the new text. Publication creates a persistent page version. We open the storefront, refresh it, and read the published result back. Writing succeeded and content verification are separate checks.

**声音：**鼠标点击轻音；只在真正发布完成后出现低音落点，复查再一个柔和确认。

**证据：** `Take C; final release publicRuns`

## 10 · 2:18–2:34 · A way back.

**画面：**真实点击恢复和刷新，旧措辞重新出现，新版本号递增。严禁用倒放页面切换假装回滚。

**旁白：** If a change needs to be reversed, the merchant restores an earlier page. Restoration creates another recorded version. The history remains visible, and the restored content can be checked again.

**声音：**机械归位感轻响，不反放前一段音频。

**证据：** `Take C; final release publicRuns`

## 11 · 2:34–2:53 · Tested. With limits visible.

**画面：**5条真实耗时线依次出现34.8、69.5、29.2、20.2、30.9秒；下方常驻 Synthetic tests。展示早前504失败且无可批准补丁。禁止标100% accuracy。

**旁白：** The release passed five consecutive public workflows and thirty-five local tests. The five journeys took twenty to sixty-nine seconds. Earlier revisions had timeout failures. Human accuracy grading and merchant testing are still pending.

**声音：**音乐缩减到脉冲，让数字读得清楚。

**证据：** `assets/evidence/vertex-release-2026-10-18.json`

## 12 · 2:53–3:05 · Google AI, controlled execution.

**画面：**简洁四节点架构。商家批准位于模型和发布之间。模型到发布之间不画直连箭头。文字足够大，不展示密钥或云账单。

**旁白：** Gemini runs through Vertex AI. Cloud Run serves the application, Firestore records versions, and private Cloud Storage holds uploaded images. The model has no publishing tool.

**声音：**脉冲逐渐合并，避免音效盖住技术名称。

**证据：** `docs/IMPLEMENTATION.md; docs/HANDOFF_GOOGLE_CLOUD.md`

## 13 · 3:05–3:15 · Fix the page. Not just the ticket.

**画面：**回到开场同一构图，错误承诺已被真实批准后的文字替代；最后6秒定格品牌、Google Cloud服务文字和短仓库链接，按钮感入口只作落版。

**旁白：** Our next test is with merchants: can they make accurate repairs with less effort? Pagemi. Fix the page. Not just the ticket.

**声音：**温暖双音收束；末尾0.5秒自然衰减，不突然截断。

**证据：** `future research hypothesis; measured business impact not claimed`

