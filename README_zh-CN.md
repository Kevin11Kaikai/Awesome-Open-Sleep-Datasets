# 开放睡眠数据集目录

[![License: CC BY 4.0](https://img.shields.io/badge/license-CC%20BY%204.0-blue.svg)](LICENSE)
[![Catalog verified](https://img.shields.io/badge/catalog%20verified-2026--11--05-2ea44f.svg)](docs/methodology.md)
[![Tier A / B / C](https://img.shields.io/badge/access-A%20%7C%20B%20%7C%20C-lightgrey.svg)](docs/access-and-licensing.md)

[English](README.md)

本目录收录已经对照原始来源核对过访问方式、许可证和队列规模的睡眠数据集。它面向睡眠分期、多导睡眠图（PSG）、呼吸事件、可穿戴验证、评分者分歧，以及信号级证据定位。

这里不收录“论文里用过 EEG”的全部名单。代码仓库和第三方转载不被视为数据发布。需要审批的队列单独成节。

**2026-11-05** 的核对结果：有原始来源的条目 **23** 个；**Tier A 14** 个（其中 13 个含波形，1 个只有标注）；**Tier B 0** 个；**Tier C 9** 个。冲突和未纳入条目见 [访问与许可](docs/access-and-licensing.md)。

## 为什么要做这个目录

公开的 EEG 分期基准很好找，也很容易被读过头。原始 EEG 本身并不等于多专家分歧、带时间位置的微结构事件，或一份能指回具体通道的临床报告。这三件事是不同的标注。

目录的起点是一项更具体的需求：为可解释睡眠分析的下一阶段寻找数据，使判断能够追溯到通道和时间范围。这条追溯写成 `e_k = (claim_k, source_k, pointer_k)`。TRACE-PSG 在 PSG 报告上发展了这一思路。本次检索没有找到其报告语料或原始波形的公开下载。因此下面每个开放数据集都按它实际提供了这条链的哪一段来评价。

## 收录规则

只有打开了项目页、数据存放页或许可证页，并且访问规则写清楚的资源才会进入目录。

- **Tier A。** 直接下载。不需要账号，也不需要审批。许可证仍然有效。
- **Tier B。** 免费注册或接受标准条款即可，没有人工批准。这一轮没有条目达到该标准。
- **Tier C。** 需要申请、伦理材料、资格培训，或受限使用协议。单独列出。
- **未核实。** 不进入机器可读目录，只写在 [核实说明](docs/access-and-licensing.md#not-reviewed-in-this-pass)。

可以直接下载，并不表示新的研究方案免于本单位伦理审查，也不表示本仓库的许可证覆盖第三方数据。同一官方页面前后数字不一致时，目录保留双方，不自行合并。

结构化副本：[`datasets/datasets.csv`](datasets/datasets.csv)、[`datasets/datasets.json`](datasets/datasets.json)。

## 目录

- [睡眠分期与 PSG](#睡眠分期与-psg)
- [评分者分歧与微结构](#评分者分歧与微结构)
- [呼吸暂停与其他事件](#呼吸暂停与其他事件)
- [可穿戴](#可穿戴)
- [没有波形的标注](#没有波形的标注)
- [开放数据怎么选](#开放数据怎么选)
- [COVER Stage 2](#cover-stage-2)
- [受控访问](#受控访问)
- [许可与伦理](#许可与伦理)
- [如何贡献](#如何贡献)
- [参考文献](#参考文献)

## 睡眠分期与 PSG

下列为 Tier A，且下载中包含原始信号和分期。表中的“记录”是夜次或文件，不是 epoch。

| 数据集 | 受试者 / 记录 | 信号与采样率 | 分期 | 许可证 |
| --- | --- | --- | --- | --- |
| [Sleep-EDF Expanded](https://physionet.org/content/sleep-edfx/1.0.0/) | 100 人，197 条 PSG | EEG、EOG、颏肌电 100 Hz；盒式记录的肌电包络和气流为 1 Hz | R&K，每条一个睡眠图 | ODC-By 1.0 |
| [CAP Sleep Database](https://physionet.org/content/capslpdb/1.0.0/) | 108 条记录（16 名对照，92 条病理记录） | 多通道 EEG、EOG、EMG、呼吸、血氧、ECG。`n1.edf` 的 EEG/EOG 为 512 Hz | R&K，另有 CAP A 相 | ODC-By 1.0 |
| [HMC v1.1](https://physionet.org/content/hmc-sleep-staging/1.1/) | 151 条记录（男 85，女 66） | 4 导 EEG、2 导 EOG、颏肌电、ECG，均为 256 Hz | AASM v2.4，单一评分 | CC BY 4.0 |
| [Challenge 2018](https://physionet.org/content/challenge-2018/1.0.0/) | 1,985 人；训练 994 / 测试 989 | 6 导 EEG、EOG、EMG、ECG、呼吸、血氧，200 Hz | 训练说明中含 AASM 30 秒分期 | ODC-By 1.0 |
| [ISRUC-Sleep](https://sleeptight.isr.uc.pt/) | 118 人，126 条记录 | 整夜 PSG。本次阅读的页面没有重述采样率 | 两名专家 | 写明用于研究；未见标准许可证 |
| [Dreem DOD-H / DOD-O](https://zenodo.org/records/15900394) | 论文：健康 25、OSA 55。代码说明：DOD-O 压缩包有 56 个文件 | HDF5 中的 PSG，含 EEG 与 EOG | 五名技师；文件说明中有共识睡眠图 | Zenodo 记录标明 MIT |
| [BOAS](https://openneuro.org/datasets/ds005555) | 100 名成人，128 夜 | 临床 PSG 与额部 EEG 同步。代码按 256 Hz 处理 | 三名专家、共识标签和 AI 标签 | 数据 CC0；代码 CC BY-NC 4.0 |
| [DREAMS](https://zenodo.org/records/2650142) | 健康整夜 20、患者整夜 27，另有更小的片段集 | PSG 或单通道片段 | 整夜子集同时有 R&K 与 AASM | CC BY-NC-ND 3.0 |

2002 年的 Sleep-EDF 是扩展版的早期子集，不是另一个队列。HMC 只收录 1.1；该版本删除了三条无法修复的记录。

## 评分者分歧与微结构

| 数据集 | 独立标注的内容 | 规模 | 下载里是否有波形 |
| --- | --- | --- | --- |
| [PSG-IPA](https://physionet.org/content/psg-ipa/1.0.0/) | 12 名技师，分别做人工和计算机辅助。分期 5 条；觉醒、腿动、呼吸事件各 5 条 | 20 条 PSG | 有 |
| [Dreem](https://zenodo.org/records/15900394) | 论文为五名技师。HDF5 里是否保存每一名的标签，需要打开文件确认 | 25 + 55，代码 README 另指出一个没有共识分的 DOD-O 文件 | 有 |
| [ISRUC-Sleep](https://sleeptight.isr.uc.pt/?page_id=48) | 两名专家 | 126 条，其中 8 人有两夜 | 有 |
| [BOAS](https://openneuro.org/datasets/ds005555) | 描述了三名专家。事件文件尚未打开，因此仍可能只公开了共识 | 128 夜 | 有 |
| [DREAMS 纺锤波 / K 复合波](https://zenodo.org/records/2650142) | 两名专家标注 30 分钟片段。专家 1 的纺锤波在 1000 秒后被截断 | 纺锤波 8 段，K 复合波 5 段 | 有，但是片段 |
| [CAP](https://physionet.org/content/capslpdb/1.0.0/) | 一个评分团队。A 相含持续时间和通道位置 | 108 条 | 有 |
| [MODA](https://osf.io/8bma7/wiki/home/) | 众包和专家的纺锤波标记 | 180 条 MASS 记录 | 无。MASS 的 EEG 属于 Tier C |

PSG-IPA 的事件任务预先填入睡眠图，评分者不能修改。这份睡眠图不是第二次独立分期。

## 呼吸暂停与其他事件

| 数据集 | 事件时间 | 是否有分期 | 限制 |
| --- | --- | --- | --- |
| [Challenge 2018 训练集](https://physionet.org/content/challenge-2018/1.0.0/) | 样本级觉醒和呼吸事件类别 | 有，30 秒 | 1.0.0 页面未确认测试集标签是否公开 |
| [UCD / St Vincent's](https://physionet.org/content/ucddb/1.0.0/) | 呼吸暂停、低通气和周期性呼吸，带发生时间 | 有，并含伪迹和不确定 | 25 夜，一名技师 |
| [MIT-BIH PSG](https://physionet.org/content/slpdb/1.0.0/) | QRS 已经复核；页面描述了呼吸暂停和 CPAP 时间 | R&K | 正文写 16 名受试者，文件索引 18 个，时长 2–7 小时 |
| [Apnea-ECG](https://physionet.org/content/apnea-ecg/1.0.0/) | 35 条学习记录有逐分钟呼吸暂停 | 无 | 是 ECG，不是 PSG。只有 8 条另含呼吸和血氧。`c05` 与 `c06` 来自同一次记录 |
| [CAP](https://physionet.org/content/capslpdb/1.0.0/) | CAP A 相的起点、持续时间和位置 | 有 | 不是呼吸事件库；命名分组里只有 4 条 SDB |

## 可穿戴

| 数据集 | 公开内容 | 有无 PSG 波形 | 访问 |
| --- | --- | --- | --- |
| [BOAS](https://openneuro.org/datasets/ds005555) | 与临床 PSG 同步的头带 EEG | 有 | A，CC0 |
| [Sleep-Accel](https://physionet.org/content/sleep-accel/1.0.0/) | 31 人的 Apple Watch 加速度、心率、步数和 PSG 分期标签 | 无 | A，ODC-By 1.0 |
| [DREAMT v2.2.0](https://physionet.org/content/dreamt/2.2.0/) | 100 名参与者的手表信号、与 PSG 对齐的数据和技术员分期 | 有 | C，受限协议 |

Sleep-Accel 不能把证据指针落到 EEG 上。发布前剔除的对象包括睡眠呼吸暂停和 REM 睡眠行为障碍。

## 没有波形的标注

[MODA](https://osf.io/8bma7/wiki/home/)（Lacourse 等，Scientific Data，2020）提供 180 条 MASS 记录的纺锤波标注。[MODA_GC 说明](https://github.com/klacourse/MODA_GC)要求向 MASS 另行申请 PSG，而 MASS 需要申请者本单位伦理审查已通过的项目。Borealis 上 MASS SS2 的纺锤波和 K 复合波文件可以直接下载，对应 EEG 仍然受限。

## 开放数据怎么选

| 问题 | 目前最合适的开放数据 | 仍然缺少的部分 |
| --- | --- | --- |
| 用临床 PSG 训练 AASM 分期 | Challenge 2018 训练集（994）和 HMC v1.1（151） | 一致的第二评分者 |
| 与经典低采样率基准比较 | Sleep-EDF Expanded | 疾病多样性和 AASM 标签 |
| 测量专家分歧 | 先用 PSG-IPA，再在打开文件后使用 ISRUC 和 DOD | PSG-IPA 只有 5 条独立分期记录 |
| 指向通道和时间 | CAP 的位置字段；Challenge 2018 和 PSG-IPA 的事件区间 | 把“判断”连到该区间的标签 |
| 比较可穿戴 EEG 和 PSG | BOAS | 尚未确认三名专家的原始轨迹都在事件文件中 |
| 把报告和波形配对 | Tier A 和 Tier B 中没有 | 未找到 TRACE-PSG 的开放数据 |

各字段的采样率限制写在 CSV 中。

## COVER Stage 2

简要结论：分歧用 PSG-IPA，带时间的证据用 Challenge 2018 和 CAP，外部分期用 HMC 与 Sleep-EDF，可穿戴 EEG 用 BOAS。实验设计、否定性结果和建议的 90 天顺序见 [COVER Stage 2 建议](docs/cover-stage2-recommendations.md)。

本目录中没有任何开放数据集已经提供可监督训练的指针式证据。事件时间是构造指针的原料，不是“判断—证据”本身。

## 受控访问

这些是真实的 PSG 资源，但不是直接下载。不要把它们写成 Tier A 或 Tier B。

| 数据集 | 页面给出的人群 | 门槛 |
| --- | --- | --- |
| [SHHS](https://sleepdata.org/datasets/shhs) | 页眉 5,804 名成人；正文 6,441 人入组，3,295 人有第二次 PSG | NSRR 申请和协议 |
| [MESA Sleep](https://sleepdata.org/datasets/mesa) | 睡眠检查入组 2,237；母研究 6,814 | NSRR 申请。MESA 其他检查另走流程 |
| [MrOS Sleep](https://sleepdata.org/datasets/mros) | 第一次成功 PSG 2,911；招募 3,135；重复睡眠测量 1,026 | NSRR 申请。此副本不含体动原始数据 |
| [Cleveland Family Study](https://sleepdata.org/datasets/cfs) | 361 个家庭的 2,284 人。先发布第 5 次访视的 PSG | NSRR 申请，且仅限非商业 |
| [STAGES](https://www.sleepdata.org/datasets/stages) | 1,500 名成人和青少年患者。2023 年移除了 Mayo 的 PSG | NSRR 申请 |
| [MASS](https://ceams-carsm.ca/mass/) | 实验室 PSG。公开说明中 SS1 为 53 人、SS2 为 19 人 | 生物信号需要本单位伦理批件 |
| [DREAMT](https://physionet.org/content/dreamt/2.2.0/) | 100 名参与者 | PhysioNet 受限许可证 |
| [NCH Sleep DataBank](https://physionet.org/content/nch-sleep/3.1.0/) | 3,984 次儿科睡眠检查，3,673 名患者，另有电子病历表 | PhysioNet 资格认证和 CITI 培训 |
| [CPS](https://physionet.org/content/cps-dataset-sleep/1.0.0/) | 113 条诊断 PSG，81 类事件 | 资格认证，且用途须符合原研究目标 |

SHHS 和 MESA 页面在核对当日显示，仓库可能因行政要求而调整。NCH 是儿科数据，STAGES 含青少年；即使签了数据协议，也需要额外的治理。

## 许可与伦理

本仓库采用 [CC BY 4.0](LICENSE)，只覆盖目录、文档和脚本，不覆盖你下载的任何数据集。

每一行写的是 2026-11-05 当天页面上可见的数据集许可证。ODC-By 和 CC BY 需要署名。DREAMS 禁止商业使用和演绎。ISRUC 写的是研究用途，没有标准许可证文本。NSRR 和 PhysioNet 受限协议另有条件；CFS 和 CPS 的限制严于“任何研究都可以”。

可以下载一份去标识文件，并不等于你的方案已经免于伦理审查。

## 如何贡献

更正需要原始链接和打开该链接的日期。链接检查只报告失效，不删除条目。提交前请阅读 [CONTRIBUTING.md](CONTRIBUTING.md)。

```bash
python scripts/export_csv.py
python scripts/validate_catalog.py
```

## 参考文献

比较方法和分级规则见 [方法](docs/methodology.md)。访问条件上的冲突见 [访问与许可](docs/access-and-licensing.md)。

条目中引用的论文和存放包括：Kemp 等，IEEE TBME，2000；Mourtazaev 等，Sleep，1995；Terzano 等，Sleep Medicine，2001；Alvarez-Estevez 与 Rijsman，PLoS ONE，2021 与 2022；Ichimaru 与 Moody，Psychiatry and Clinical Neurosciences，1999；Penzel 等，Computers in Cardiology，2000；Ghassemi 等，Computing in Cardiology，2018；Walch 等，Sleep，2019；Guillot 等，IEEE TNSRE，2020；O'Reilly 等，Journal of Sleep Research，2014；Lacourse 等，Scientific Data，2020；Quan 等，Sleep，1997；Zhang 等，JAMIA，2018；Khalighi 等，Computer Methods and Programs in Biomedicine，2016。

数据来自 PhysioNet、NSRR、Zenodo、OpenNeuro、Borealis、OSF 和 ISRUC 项目网站。本目录不转分发这些记录。
