# 项目概览

**最后更新：** 2026-03-28

---

## 这个项目是什么

这是 Elias 的**个人 AI 助手（小白）的工作空间**，本质是 AI 助手的"大脑"，不是传统代码项目。

备份在 GitHub：https://github.com/tenbj/workspace.git

---

## 目录结构

```
qclaw/workspace/
├── .git/                    # Git 仓库
├── .openclaw/               # openclaw 状态数据
│
├── *.md                     # 核心配置文件（见下方详解）
│
├── memory/                  # 每日记忆
│   ├── YYYY-MM-DD.md        # 每日原始笔记
│   └── meetings/            # 例会纪要
│       └── 每日例会-YYYY-MM-DD.md
│
├── knowledge/               # 知识库（2026-03-28 新建）
│   ├── index.json           # 全局索引
│   ├── plans/               # 所有计划方案
│   │   └── knowledge-system-v1.md  # 知识系统方案
│   └── about-elias/         # 关于 Elias 的认知档案
│       └── k-elias-001.md   # 初始档案
│
└── skills/                  # 技能模块
    └── free-web-search/     # 网页搜索技能
        ├── SKILL.md
        ├── search.js
        ├── price_checker.js
        └── xianyu_price.js
```

---

## 配置文件说明

| 文件 | 作用 | 优先级 |
|------|------|--------|
| **IDENTITY.md** | 小白是谁：名字、风格、emoji | 高 |
| **SOUL.md** | 小白的行事风格定义 | 高 |
| **USER.md** | Elias 是谁：名字、时区、偏好 | 高 |
| **AGENTS.md** | 工作区规则：记忆系统、知识库、群聊规范等 | 高 |
| **TOOLS.md** | 本地环境笔记：SSH、摄像头、TTS 等 | 中 |
| **BOOTSTRAP.md** | 初始化引导（用过就删） | 低 |
| **HEARTBEAT.md** | 心跳任务配置 | 低 |

---

## 记忆系统

### 三层结构

1. **每日笔记** `memory/YYYY-MM-DD.md`
   - 当天发生的原始记录
   - 简短，几句话概括

2. **长期记忆** `MEMORY.md`（主会话时加载）
   - 从每日笔记提炼的精华
   - 重要决策、教训、背景

3. **知识库** `knowledge/`
   - 关于 Elias 的认知档案
   - 自动积累，无需询问
   - 不定期反馈"学到了什么"

### 启动流程

每次会话开始，自动读取：
1. `SOUL.md` — 小白是谁
2. `USER.md` — Elias 是谁
3. 今天 + 昨天的 `memory/YYYY-MM-DD.md`
4. 主会话时额外读 `MEMORY.md`

---

## 知识库机制

### 记录触发（自动）

- 聊到 Elias 的工作、生活、偏好、观点
- 他做出决定并给出理由
- 任何他认为重要的事
- 外部讨论中有价值的结论

### 检索触发（聊天时自动）

聊到某话题时，自动检查知识库：
1. 精确匹配 terms 字段
2. 模糊匹配 topics 字段
3. 关联扩散 related 字段

### 分类演化

- 新知识无合适分类 → 待归类队列
- 某分类超过20条 → 提出来是否拆分
- 分类重叠 → 提议合并
- 知识过时 → 标注废弃

---

## GitHub 同步

- 仓库：https://github.com/tenbj/workspace.git
- 工作流程：本地变更 → commit → push
- 原则：定期清理无用文件后再同步

---

## 更新日志

| 日期 | 更新内容 |
|------|----------|
| 2026-03-28 | 建立知识库系统，新增 knowledge/ 目录 |
| 2026-03-28 | 根目录所有 .md 文件改为中文 |
| 2026-03-28 | 清理无用 Python/安装脚本 |
