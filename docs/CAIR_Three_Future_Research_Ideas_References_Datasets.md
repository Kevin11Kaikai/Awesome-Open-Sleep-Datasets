# CAIR 博士后未来研究：三个 Idea、参考文献与开放数据路线

**整理日期：2026-11-05**  
**核心建议：选择 Idea 1 作为今晚面试的唯一 Future Research Vision；Idea 2 是第一项实验，Idea 3 是重要的后续科学问题。**  
**对应 Slide：** `CAIR_Idea1_Evidence_Verified_Multimodal_Escalation.pptx`

## 0. 30 秒快速记忆

- **My PhD — COVER：** *When should a medical AI model accept a prediction, and when should it defer?* 已建立风险感知 selective prediction；不应将尚未完成的 Stage 2 当成既有成果。
- **My next question：** *When can we trust a proposed correction after deferral?*
- **My idea：** Stage 2 先提出候选修正，再使用**独立核验的 EEG/EOG/EMG 证据**研究是否采用修正、保留 primary prediction 或继续 abstain。
- **The scientific test：** *Does independent evidence verification reduce newly introduced errors at matched decision coverage?*
- **The critical distinction：** 一个 spindle/eye-movement 事件真实存在 **≠** 该事件足以支持修正后的睡眠阶段。

> **Memorable line:** “My PhD taught medical AI when not to trust a prediction. My postdoctoral research will investigate when there is enough physiological evidence to trust a correction.”

---

## 1. 三个 Research Ideas：一眼比较

| | **Idea 1 — Evidence-Verified Multimodal Escalation** ★ | **Idea 2 — Risk-Controlled Specialist Arbitration** | **Idea 3 — Disagreement-Aware Sleep Staging** |
|---|---|---|---|
| **核心问题** | 经独立生理证据核验的修正是否比仅靠置信度更可靠？ | 在 COVER 拒绝的样本上，应信任哪个独立专家？ | 哪些困难样本是模型真正错误，哪些是人工专家也存在合理分歧？ |
| **与 COVER 关系** | 在冻结的 Stage 1 上研究 Stage 2 决策可靠性 | COVER 的直接、最低成本延续 | 扩展 COVER 所依赖的单一 ground-truth label 假设 |
| **主要科学增量** | 评估**证据有效性是否具有决策价值**，不只是生成解释 | 研究针对 deferred case 的受约束专家选择与拒绝 | 区分预测风险与标注/生理歧义，建立 disagreement-aware 评价 |
| **参考论文** | SleepVLM；TRACE-PSG；OpenTSLM；RSSP（参见 §4） | RSSP；COVER；selective prediction 传统基线 | RSSP 的标签噪声动机；多专家分期评估研究 |
| **第一批数据** | Sleep-EDF → HMC → DREAMS / CAP / PSG-IPA | 原有 Sleep-EDF-20 frozen deferred epochs | PSG-IPA staging 子集 → ISRUC-Sleep；DOD 需先检查逐专家标签 |
| **可证伪预测** | 验证策略在匹配 coverage 下减少新错误 | 独立专家相较 Conformer 在 deferred 样本上产生正的净纠错收益 | 多专家分歧对模型失败有可测量的解释或预测价值 |
| **最大研究风险** | **证据存在不等于修正正确**；验证策略可能没有增量价值 | 容易成为简单模型 ensemble / arbitration 的增量工程 | 高质量多专家 staging 数据有限，且可能弱化 Stage 2 叙事 |
| **面试角色** | **唯一核心愿景** | **最先实施的实验** | **未来拓展与评估严谨性的补充** |

**决策：选 Idea 1。** 它最自然地将 COVER 的 accept/defer 拓展到 *adopt a correction / retain / abstain*，并且即使 foundation model 输给传统 specialist，仍能够检验一个独立且有意义的科学假设：**生理证据核验究竟能否帮助系统避免 harmful corrections？**

## 2. Idea 1：主线与可执行研究计划

### 2.1 单一句子研究愿景

**From risk-aware deferral to evidence-verified correction: deciding whether to trust a proposed sleep-stage correction using independently verifiable PSG evidence.**

### 2.2 三个层层递进的 RQs

**RQ1 — Correction.** 在完全相同、预先冻结的 COVER deferred epochs 上，对独立 specialist 和 foundation-model 候选的**救回错误**、**引入新错**、个体异质性与最终 coverage–risk 进行公平对比。不能用测试真值选择模型或设置采纳阈值。

**RQ2 — Physiological explanation.** 在存在所需真实模态的记录上，逐步增加第二 EEG、EOG、chin EMG 等通道，评估对难例的**实际边际价值**；不能假设模态越多或 LLM 越大一定更可靠。控制 subject split、采样率、导联、时序上下文与缺失模态。

**RQ3 — Evidence verification.** 让第二阶段输出 `(claim, channel, start_time, end_time, feature_type)`，用**独立的事件标签、检测器或盲法专家审阅**，分别验证：（i）指针位置；（ii）事件是否真实存在；（iii）事件是否按照分期规则支持修正。再检验核验后的 decision policy 是否降低新错误。

### 2.3 单页 Slide 的最简流程

```text
Frozen COVER (ACCEPT / DEFER)
           │
      Deferred epochs
           │
     ┌─────┴──────────────────────┐
     ▼                            ▼
Independent reassessment     Multichannel PSG evidence
Specialist / foundation      EEG + EOG + EMG (when available)
     └──────────────┬─────────────┘
                    ▼
       Independent verification
  Does the localized event exist?
  Does the event support this stage?
                    ▼
     ADOPT correction / RETAIN / ABSTAIN
                    │
   TEST: new errors at matched coverage

Open-data foundation (NOT an algorithm module):
Sleep-EDF → HMC → DREAMS / CAP / PSG-IPA / Challenge 2018
```

**必须保留的风险边界：** *Evidence present* 不能直接推导出 *correction correct*。一个候选修正即使有真实事件作背景，仍可能与其他通道信息相冲突；采用决定必须通过独立 held-out 评估。

### 2.4 Minimum Viable Experiment（应从这里开始，不训练昂贵 FM）

1. **Frozen protocol：** 使用现有 COVER Sleep-EDF-20 subject-held-out split、gate、sample keys 和 primary predictions；先审计此前 30-case pilot（仅用于生成假设，不用于最终选择）。
2. **Candidate baselines：** primary-only；COVER + abstention；一个真正独立训练的 specialist（如 TinySleepNet）；固定版本 FM（资源允许时）；confidence-only acceptance；evidence-conditioned acceptance。
3. **Primary endpoints：** `rescue = # (primary wrong, corrected right)`；`harm = # (primary right, corrected wrong)`；`net = rescue - harm`。还要报告 final cascade coverage、selective risk、macro-F1、N1/transition 结果与 per-subject variability。
4. **Evidence pilot：** 从 frozen deferred cohort 按受试者/阶段/分歧预先抽取核查集；在有事件真值的 DREAMS、CAP、PSG-IPA/Challenge 2018 上验证 detector，再用独立标注或专家审阅评价 claim→signal→stage support。
5. **公平决策对照：** 在**相同返回预测比例（matched decision coverage）**下比较 evidence-based policy、confidence-only、agreement-only、无核验的 explanation policy。所有阈值在 calibration/dev set 上选定，不使用 held-out labels。
6. **失败判据：** 如果 evidence validity 与 correction correctness 缺少稳定关联，或者 evidence-conditioned policy 在匹配 coverage 后未能超越简单基线，就不能宣称验证机制减少了不可靠纠错。阴性结果同样可以形成关于 Stage 2 适用边界的实证结论。

**跨数据集注意：** Sleep-EDF 当前 gate 不保证能直接迁移 HMC/CAP；到新数据域时需重新训练/校准（仅用训练和开发受试者），并以独立外部测试集报告结果。R&K/AASM 标签、采样率和导联不可直接默认为相同。

---

## 3. Idea 2 和 Idea 3：为什么保留，但不作为今晚主线

### Idea 2 — Risk-Controlled Specialist Arbitration

- **假设：** COVER gate 选择的困难样本形成了一个与完整测试集不同的条件分布；在该分布上，独立 specialist 和 primary model 的互补性能预测何时应采用修正。
- **第一实验：** 原样冻结 gate；仅在 held-out deferred samples 比较 primary / specialist / FM。对阈值、修正选择规则使用 subject-disjoint calibration；报告 `rescue − harm` 和匹配 coverage 的 selective risk。
- **最适合数据：** **Sleep-EDF-20**（第一批）；**HMC**（另设 domain-shift 实验，不能直接重复原 gate 的“冻结”承诺）。
- **论文启发：** RSSP 的 Q1/Q2 多视角一致性提示要检验独立再判断，但 RSSP 的**标签噪声训练样本筛选**不是已经验证的推理阶段纠错策略。
- **为什么不是主线：** 高可行性，但如果没有独立的风险约束方法论，容易止步于 expert selection 或模型组合。**它应成为 Idea 1 的 RQ1。**

### Idea 3 — Disagreement-Aware Sleep Staging

- **假设：** 某些 COVER deferred cases 具有不可忽视的专家间歧义；将所有与单一专家标签不符的预测一律视作错误，会高估某些模型的失败并误导选择策略。
- **第一实验：** 在 PSG-IPA 的 **5 个 sleep-staging recordings** 上使用 **12 位专家的 manual labels** 计算 epoch-wise majority fraction / disagreement；检查模型不确定度、defer score 与人工分歧的关联。将其当作**小规模测量研究**，不要把另外 15 个 event-task recordings 当作多专家 sleep-stage labels。
- **第二数据：** ISRUC-Sleep 的 two-expert labels；Dreem DOD 仅在实际读取 HDF5、确认 per-scorer labels 后加入。多专家不等于多种独立仪器/实验室，应注意 scorer 来源和评价目标。
- **为什么不是主线：** 数据与监督的独特性使它适合阶段性论文或重要 robustness analysis，但在今晚 8–9 分钟的面试里不如 Idea 1 与 COVER Stage 2 直接。

---

## 4. 四篇核心论文：准确贡献与可借鉴之处

| Ref | Paper / official source | 实际重点 | 对本研究的启发 | **不能声称** |
|---|---|---|---|---|
| **[P1]** | **Qiu et al., RSSP**, *Robust Sleep Stage Prediction from Electroencephalogram with Label Noise Using Multimodal Large Language Models*, **MICCAI 2025** — [paper](https://papers.miccai.org/miccai-2025/0793-Paper1959.html) · [code](https://github.com/Leonard-zc/MICCAI2025-RSSP) | Q1 yes/no label verification + Q2 five-class classification → multi-perspective agreement filtering → self-training，以应对**训练标签噪声** | 受启发设计独立 Q2 reassessment，并严格统计 correction/harm | “已证明 Q1/Q2 可直接解决 COVER 的 test-time deferred correction” |
| **[P2]** | **Langer et al., OpenTSLM**, *Time-Series Language Models for Reasoning over Multivariate Medical Text- and Time-Series Data*, **ICML 2026** — [paper](https://proceedings.mlr.press/v306/langer26a.html) · [code](https://github.com/OpenTSLM/OpenTSLM) | 将时间序列作为 LLM 输入模态；soft prompts / cross attention；包括 Sleep-CoT | 不必仅把波形渲染为图片；检验原始时序与自然语言的联合建模能否帮助 difficult epoch | “生成 CoT 就是生理证据正确” |
| **[P3]** | **Deng et al., SleepVLM**, *Explainable and Rule-Grounded Sleep Staging via a Vision-Language Model*, **arXiv 2026** — [paper](https://arxiv.org/abs/2603.26738) | 多通道 PSG waveform-image perception + AASM-informed rationale；释出 MASS-EX 解释标注资源 | 生理事件识别、规则引用与 staging decision 结合；启发 RQ2 | “已有的 AASM 文字解释自动等于独立波形证据核验”或“相关 MASS 波形无需审批” |
| **[P4]** | **Wu et al., TRACE-PSG**, *Traceable Sleep Diagnosis Support with Pointer-Grounded Evidence*, **MICCAI 2026** — [paper](https://papers.miccai.org/miccai-2026/1080-Paper5410.html) | PSG **报告/临床文本层**指标读取、结构化诊断和 restricted Pointer Bank provenance checking | 将可审计的 pointer 思想推进到 `channel + time + physiological event`，并测试对修正选择的价值 | “TRACE-PSG 已解决原始 PSG 波形的事件级定位”或“其报告数据已经公开可下” |

**共同启发不是四模型串联**：独立判断（P1/P2）→ 生理解释（P3）→ 证据溯源（P4）→ **你新增要研究的：证据核验是否改善 correction decision**。

## 5. 官方数据源与研究问题的映射

下面的数据描述来自官方数据发布页，并与 [Awesome-Open-Sleep-Datasets](https://github.com/Kevin11Kaikai/Awesome-Open-Sleep-Datasets) 的 [COVER Stage 2 recommendations](https://github.com/Kevin11Kaikai/Awesome-Open-Sleep-Datasets/blob/main/docs/cover-stage2-recommendations.md) 交叉核对。**直接下载（Tier A）并不代表免除许可证、伦理和机构规定。**

| Dataset / official link | 真实模态与标签 | 已核查访问方式 | 优先研究用途 | 主要局限 |
|---|---|---|---|---|
| **[D1 Sleep-EDF Expanded](https://physionet.org/content/sleep-edfx/1.0.0/)** | Fpz-Cz、Pz-Oz EEG；horizontal EOG；chin EMG；R&K stages（部分记录另有呼吸/温度） | Tier A；ODC-By 1.0 | **RQ1** frozen baseline；**RQ2** 同 cohort 增加通道 | 现有 COVER 只使用一个 EEG channel **≠** 原始数据只有一个通道；cassette chin EMG 为 1 Hz envelope；无常规独立 spindle/K-complex 事件真值 |
| **[D2 HMC v1.1](https://physionet.org/content/hmc-sleep-staging/1.1/)** | 4 EEG + 2 EOG + chin EMG + ECG，256 Hz；AASM v2.4 stages | Tier A；CC BY 4.0 | **RQ2** 多通道与 subject-level 泛化，外部临床 PSG | 151 recordings；没有公开多专家 staging truth；与 Sleep-EDF 导联不直接相同 |
| **[D3 CAP Sleep](https://physionet.org/content/capslpdb/1.0.0/)** | 多 EEG/EOG/EMG/respiration/SpO₂；R&K stages；**CAP phase-A onset/duration/location** | Tier A；ODC-By 1.0 | **RQ3** 带通道信息的事件时间指针 | CAP A phase 是 CAP 事件，**不是**通用 spindle/K-complex 真值；采样率因记录/信号变化 |
| **[D4 PSG-IPA](https://physionet.org/content/psg-ipa/1.0.0/)** | EEG/EOG/EMG/ECG/resp；12 专家；staging、arousal、respiration、limb 等任务 | Tier A；CC BY 4.0 | **Idea 3** 专家分歧；**RQ3** onset/offset boundary uncertainty | 20 个 PSG 分为 4 个任务，每任务 **5** 个 recordings；多专家 staging 只覆盖其中 5 个 |
| **[D5 Challenge 2018](https://physionet.org/content/challenge-2018/1.0.0/)** | 多通道 PSG；AASM stages；可定位的 arousals/respiratory events | Tier A；ODC-By 1.0 | **RQ3** 大规模 timed-event grounding | 994 个有标注训练记录；挑战测试集标签不是公开评测真值；不是多专家重复分期 |
| **[D6 DREAMS](https://zenodo.org/records/2650142)** | PSG 与专门微事件子集；8 段 spindle、5 段 K-complex EEG excerpts 含双专家标注 | 直接下载；仓库记录许可证 CC BY-NC-ND 3.0，使用前复核条款 | **RQ3** 局部 spindle / K-complex event detector validation | 片段短；spindle expert 1 的标注在 1000s 后截断；商业用途等受限 |
| **[D7 ISRUC-Sleep](https://sleeptight.isr.uc.pt/)** | 多通道 PSG；两名专家 staging | 官网有公开下载；标准化授权范围未明 | **Idea 3** 从 PSG-IPA 向更多 nights 扩展 disagreement analysis | 未见清楚的标准开源许可证；不能自动认定可用于商业训练 |
| **[D8 Dreem DOD-H/DOD-O](https://zenodo.org/records/15900394)** | PSG/HDF5；研究描述多位睡眠技术员评分 | 仓库列 Tier A，Zenodo 项目与文件需实际核对 | **Idea 3** 多专家分歧的潜在扩展 | **必须先打开 HDF5 确认是否有可用的逐专家 staging arrays**；不能只凭论文中的专家人数定实验 |

**数据使用顺序：**

1. **今天/第一步：D1 Sleep-EDF** — 不换数据、不改 gate，严格测 Stage 2 是否净纠错。
2. **第一阶段扩展：D1 原始 EOG/第二 EEG → D2 HMC** — 控制新增模态带来的边际价值。
3. **证据标注研究：D6 DREAMS + D3 CAP + D4 PSG-IPA + D5 Challenge 2018** — 分开做 *event exists* 与 *stage supported* 两层真值。
4. **分歧研究：D4 PSG-IPA → D7 ISRUC / D8 DOD（核实后）** — 研究如何定义不可消除的标签歧义。

---

## 6. 研究边界：避免在面试中说错的五件事

1. **COVER 的既有贡献是 Stage 1 风险感知决策**；Stage 2 evidence-based policy 是未来假设。
2. **单通道输入 ≠ Sleep-EDF 原始记录只有单通道**；Sleep-EDF 有两个 EEG 导联与 EOG/EMG（但 EMG 表示因子数据集不同）。
3. **RSSP 的 multi-perspective agreement 主要是训练数据筛选**，不是已经证实的 independent correction decision policy。
4. **事件真实存在 ≠ 支持修正阶段 ≠ 最终决策一定正确**。这是 Idea 1 的首要科学风险，也恰是可测试性所在。
5. **数据目录是可复现研究基础设施**，不应包装为已完成的算法创新；开放发布、可商用和具备公开原始波形是不同命题。

## 7. 面试建议（可直接照读）

**Slide title:** *After DEFER: Can We Trust the Correction?*

**One scientific question:** *Can independently verified physiological evidence identify corrections that are safe to adopt?*

**20-second close:**

> “COVER tells us when not to trust the original prediction. My next research question is when to trust a correction. I will compare independent experts on the same deferred cases, then test whether EEG, EOG, and EMG evidence can be independently verified and used to prevent harmful corrections. The key outcome is not a more persuasive explanation, but fewer new errors at matched coverage.”

**If an interviewer challenges the premise:**

> “I agree that evidence can be real without proving a label. That is exactly why I want a three-level evaluation: localization accuracy, physiological support for the stage, and whether the verification-based policy improves held-out decision risk. If it doesn't, the hypothesis is not supported.”

---

## 8. Source index & verification status

### Papers (official publication records)

- [P1] MICCAI 2025 — [RSSP paper](https://papers.miccai.org/miccai-2025/0793-Paper1959.html); [open-source code](https://github.com/Leonard-zc/MICCAI2025-RSSP).
- [P2] ICML 2026 / PMLR — [OpenTSLM paper](https://proceedings.mlr.press/v306/langer26a.html); [repository](https://github.com/OpenTSLM/OpenTSLM).
- [P3] arXiv — [SleepVLM 2603.26738](https://arxiv.org/abs/2603.26738).
- [P4] MICCAI 2026 — [TRACE-PSG paper](https://papers.miccai.org/miccai-2026/1080-Paper5410.html).

### Datasets (official releases)

- [D1] PhysioNet — [Sleep-EDF Expanded v1.0.0](https://physionet.org/content/sleep-edfx/1.0.0/).
- [D2] PhysioNet — [HMC v1.1](https://physionet.org/content/hmc-sleep-staging/1.1/).
- [D3] PhysioNet — [CAP Sleep v1.0.0](https://physionet.org/content/capslpdb/1.0.0/).
- [D4] PhysioNet — [PSG-IPA v1.0.0](https://physionet.org/content/psg-ipa/1.0.0/).
- [D5] PhysioNet — [Challenge 2018](https://physionet.org/content/challenge-2018/1.0.0/).
- [D6] Zenodo — [DREAMS 2650142](https://zenodo.org/records/2650142).
- [D7] Official project site — [ISRUC-Sleep](https://sleeptight.isr.uc.pt/).
- [D8] Zenodo — [Dreem Open Datasets 15900394](https://zenodo.org/records/15900394).

### User's catalog (actual file read; 2026-11-05 revision)

- [Awesome-Open-Sleep-Datasets — README](https://github.com/Kevin11Kaikai/Awesome-Open-Sleep-Datasets)
- [COVER Stage 2 recommendations](https://github.com/Kevin11Kaikai/Awesome-Open-Sleep-Datasets/blob/main/docs/cover-stage2-recommendations.md)
- [Access and licensing](https://github.com/Kevin11Kaikai/Awesome-Open-Sleep-Datasets/blob/main/docs/access-and-licensing.md)

**Verification interpretation:** [P1]–[P4] 和 [D1]、[D2]、[D4]–[D6] 的核心描述已与出版方/官方发布页比对。[D3] 的细节与开放状态来自仓库中列明的 PhysioNet 原始核查记录，本轮网页工具未能重新打开其页面。[D7]、[D8] 的下载/许可证或逐专家数据结构仍有需要进一步确认的条件，以上没有将其当作已具备的完整实验真值。数据集未实际下载，研究结果均为未来实验设计，不是完成的性能发现。
