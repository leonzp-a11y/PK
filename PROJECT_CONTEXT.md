# PK Project Context

## 项目背景

本项目位于 Windows 笔记本的 `E:\PK`，主要包含 PK 项目的设计文档、战斗表现分析材料、脚本工具、截图和 Codex Skill 相关内容。当前目标是让该项目可以在 Windows 笔记本与 Mac 笔记本的 Codex 环境之间稳定同步。

用户希望通过 Git 将项目同步到 Mac，并已创建 GitHub 远程仓库：

```text
https://github.com/leonzp-a11y/PK.git
```

## 关键决策

1. 使用 Git 作为 Windows 与 Mac 间的主要同步方式。
2. 使用 GitHub 远程仓库作为同步中转。
3. 仓库主分支使用 `main`。
4. `.mp4` 视频文件不纳入 Git 同步，避免仓库过大或触发 GitHub 大文件限制。
5. 截图、文档、Markdown、Python 脚本、HTML 图示、配置等项目工作文件纳入 Git。
6. 添加 `.gitattributes`，让 Windows/Mac 间换行和二进制文件处理更稳定。
7. GitHub 认证问题最终通过 Git Credential Manager 解决，已成功推送。

## 已完成工作

1. 在 `E:\PK` 初始化 Git 仓库。
2. 创建并提交 `.gitignore`，排除视频、缓存、临时文件、本地环境和大型源素材。
3. 创建并提交 `.gitattributes`，定义文本换行和二进制文件处理规则。
4. 完成首次本地提交：

```text
d7ea3e8 Initial PK project
```

5. 绑定远程仓库：

```text
origin  https://github.com/leonzp-a11y/PK.git
```

6. 成功推送 `main` 分支到 GitHub：

```text
main -> main
```

7. 本地 `main` 已设置为跟踪远程 `origin/main`。

## 未完成任务

1. 在 Mac 笔记本的 Codex 中克隆仓库。
2. 如果用户需要，可将 GitHub 仓库从 Private 改为 Public。
3. 如果以后需要同步视频，再单独考虑网盘或 Git LFS；当前明确不需要同步 `.mp4`。
4. Mac 克隆后可检查文档、脚本、图片路径是否符合预期。

## 重要文件路径

### 项目根目录

```text
E:\PK
```

### Git 同步相关

```text
E:\PK\.gitignore
E:\PK\.gitattributes
E:\PK\PROJECT_CONTEXT.md
```

### 主要设计文档

```text
E:\PK\设计文档
E:\PK\战斗表现底层框架v0.1.md
E:\PK\设计文档\自动战斗表现底层框架v0.2.md
E:\PK\设计文档\自动战斗表现底层框架v0.2.docx
E:\PK\设计文档\战斗表现规则框架-V0.2.md
E:\PK\设计文档\钓鱼系统设计方案.md
E:\PK\设计文档\世界碎片与逸闻系统.md
```

### 战斗表现分析相关

```text
E:\PK\combat_video_analysis
E:\PK\设计文档\战斗表现分析报告
E:\PK\设计文档\战斗表现分析报告\战斗DEMO表现分析报告-蜘蛛洞穴.docx
```

### 脚本工具

```text
E:\PK\build_auto_combat_framework_doc.py
E:\PK\build_combat_doc_report.py
E:\PK\build_combat_framework_doc.py
E:\PK\extract_docx_images.py
E:\PK\extract_docx_outline.py
E:\PK\sync_auto_combat_framework_from_user_doc.py
E:\PK\tools
```

### Skill 相关

```text
E:\PK\SKILL
E:\PK\SKILL\worldbuilding-designer\SKILL.md
```

## Mac 端同步步骤

在 Mac 的 Codex 终端中执行：

```bash
mkdir -p ~/Projects
cd ~/Projects
git clone https://github.com/leonzp-a11y/PK.git
cd PK
git status
```

如果 `git status` 显示工作区干净，并且分支跟踪 `origin/main`，则同步成功。

## 日常同步流程

### Windows 修改后推送

```powershell
cd E:\PK
git pull
git add .
git commit -m "Update"
git push
```

### Mac 修改后推送

```bash
cd ~/Projects/PK
git pull
git add .
git commit -m "Update"
git push
```

### 另一台机器更新

```bash
git pull
```

Windows PowerShell 中同样执行：

```powershell
git pull
```

## 注意事项

1. `.mp4` 文件已被 `.gitignore` 排除，Mac 克隆后看不到视频是正常现象。
2. 如果 GitHub 仓库改为公开，仓库中的文档、截图、配置、脚本都会被别人看到。
3. 不要在 Git 中提交账号、密码、token、私钥或 `.env` 文件。
4. 以后新增大文件时，先确认是否应该进 Git；超过 100MB 的文件不要直接提交到普通 GitHub 仓库。

## 下一步计划

1. 将本文件提交并推送到 GitHub。
2. 用户在 Mac 端克隆仓库。
3. Mac 克隆完成后运行 `git status` 检查状态。
4. 后续在两台机器之间使用 `pull -> edit -> add -> commit -> push` 的节奏同步。
