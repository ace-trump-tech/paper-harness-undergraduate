# paper-harness-undergraduate

**Languages:** [简体中文](README.md) · [English](README.en.md) · [日本語](README.ja.md)

> 面向本科毕业论文与科研初学者的研究工作台。先建立综述和证据，再设计可完成的小实验，最后在导师确认下写作。

<p align="center"><img src="demo/stem_pipeline.svg" alt="undergraduate thesis workflow" width="900"></p>

<p align="center"><a href="docs/getting-started-zh.md">从零开始教程</a> · <a href="docs/undergraduate-edition-zh.md">工作流说明</a> · <a href="demo/index.html">离线 Demo</a></p>

## 这个仓库解决什么问题

老师给了一个题目，但你不知道如何开始读文献、怎么设计一组能做完的实验、哪些结论不能乱写、怎样保存过程记录。这个仓库将任务拆成：

```text
课题范围 -> 本地资料/文献 -> 综述矩阵 -> 可检验方案
          -> 导师批准的 baseline 实验 -> 证据检查 -> 草稿与完整性检查
```

它不是自动交论文的黑盒。所有文献、实验、claim、相似度筛查和人工确认都保存为 JSON artifact 与事件流；最终结论由学生和导师确认。

## 快速开始

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m paper_harness.cli init examples/stem_project/project.json --output ./runs/my-thesis
python -m paper_harness.cli run ./runs/my-thesis/project.json
```

高风险阶段会返回 `approval-required`。先阅读 `artifacts/`，再继续：

```bash
python -m paper_harness.cli approve ./runs/my-thesis/project.json --stage experiment
python -m paper_harness.cli run ./runs/my-thesis/project.json
```

完整的逐步讲解、常见错误和结果阅读方式见 [从零开始教程](docs/getting-started-zh.md)。

## 为初学者保留的能力

- `undergraduate-guide`：把老师给出的课题转换为综述优先、基线明确、变量有限的实验计划。
- `knowledge-base`：本地持久化长文本分块，不重复把整篇资料塞进上下文，降低 token 消耗和 OOM 风险。
- `similarity-checker`：本地重合筛查，帮助你回看引用与改写，不替代学校正式查重。
- `authorship-editor`：提示贡献表达和 AI 使用披露，**不提供规避 AI 检测的功能**。
- `claim-auditor`：每条草稿 claim 指向文献或实验 artifact；“可追溯”不等于“已经证明”。
- 可恢复运行：中断后再次执行 `run`，已完成 Agent 不会重复产出结果。

## 适用边界

- 默认 Demo 的实验是合成数据，只验证流程，不能作为毕业论文结果。
- 不绕过登录、付费墙、验证码或数据库规则；需要的资料请由你合规导入。
- 不自动投稿、伪造引用或自动断言创新成立。
- 真实实验默认 dry-run，必须经导师/研究者批准后配置并执行。

## 仓库结构

```text
paper_harness/       编排器、Agent、证据链和本地知识库
docs/                 面向新手的教程与工作流说明
examples/             可直接修改的项目配置
demo/                 无 API Key 的离线演示
tests/                无网络单元测试
```

需要多 GPU 的 CV 创新组合探索，请使用独立仓库 `paper-harness-cv`。两者保持独立发布与依赖边界。
