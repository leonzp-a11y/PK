---
name: worldbuilding-designer
description: Design and maintain worldbuilding, narrative structure, character voice, anecdote systems, triggered text, lore entries, faction/location history, and narrative configuration needs for the PK mobile game project. Use when Codex is asked to create, revise, organize, or evaluate PK world setting documents, main or side story concepts, in-game anecdotes, event snippets, NPC dialogue, triggered flavor text, lore logs, or narrative content that must remain consistent with project design goals.
---

# Worldbuilding Designer

## Overview

Use this skill to produce narrative design that can become game content, not only prose. Keep outputs consistent with the project's design-document structure: design purpose, player experience, target design, mind map, interaction/prototype needs, concrete design, and configuration structure.

Treat all existing PK documents as source of truth. If no setting source exists yet, clearly mark assumptions as draft and keep them easy to replace.

## Core Principles

- Start from player experience: define what the player should notice, feel, understand, or want to do next.
- Keep the world usable: every setting element should help gameplay, progression, collection, exploration, combat identity, social identity, or content production.
- Separate canon from draft: label unconfirmed ideas as `待定` or `草案`.
- Prefer modular design: split worldbuilding into factions, locations, characters, historical events, rules, mysteries, and text delivery systems.
- Keep text concise for mobile use: short scene text, clear hooks, strong nouns, and controlled information density.
- Design for reuse: important terms, characters, locations, and event types should be reusable across main story, anecdotes, triggered text, UI logs, and configuration tables.

## Workflow

1. Confirm the design purpose.
   - Write a one-sentence concept.
   - Define the intended player-side experience.
   - Define short-, mid-, and long-term goals.

2. Build the narrative module map.
   - Split the design into systems and content modules.
   - Identify dependencies between world rules, characters, locations, triggers, rewards, and records.
   - Keep the mind map suitable for later conversion into design documents.

3. Design the content structure.
   - For worldbuilding: define world premise, core conflict, factions, locations, history, power rules, and player identity.
   - For stories: define premise, conflict, player role, key beats, involved characters, outcome, and unlock conditions.
   - For anecdotes: define trigger, location, involved subject, short event, player-facing effect, record behavior, and optional follow-up.
   - For triggered text: define trigger condition, display method, text variants, cooldown/repeat rule, priority, and log behavior.

4. Prepare implementation-facing details.
   - Call out UI needs, interaction path, state changes, and edge cases.
   - Define configuration fields only after the content behavior is clear.
   - Keep fields tied to actual design use.

5. Review consistency.
   - Check whether tone, terminology, timeline, faction logic, and character behavior conflict with existing project materials.
   - If a conflict appears, list it directly and propose a clean resolution.

## Output Standards

Use Chinese for PK project-facing narrative documents unless the user asks otherwise.

For a worldbuilding design, use this structure:

```markdown
# 世界观设计名称

## 1. 设计目的
### 1.1 概念简述
### 1.2 玩家侧体验
### 1.3 目标设计

## 2. 世界观模块脑图

## 3. 核心设定
### 3.1 世界基础规则
### 3.2 核心冲突
### 3.3 玩家身份
### 3.4 势力与地区
### 3.5 历史与现状

## 4. 内容落地方式
### 4.1 主线剧情
### 4.2 支线剧情
### 4.3 逸闻
### 4.4 触发式文本
### 4.5 图鉴或日志

## 5. 配置结构
```

For an anecdote design, use this structure:

```markdown
## 逸闻名称

| 项目 | 内容 |
| --- | --- |
| 一句话概念 |  |
| 玩家体验目标 |  |
| 触发条件 |  |
| 发生地点 |  |
| 关联角色/对象 |  |
| 展示方式 |  |
| 是否记录 |  |
| 后续影响 |  |

### 事件流程

### 文本内容

### 配置需求
```

For triggered text, use this structure:

```markdown
## 触发式文本组名称

| 字段 | 内容 |
| --- | --- |
| 触发场景 |  |
| 触发条件 |  |
| 优先级 |  |
| 冷却/重复规则 |  |
| 展示方式 |  |
| 文本长度 |  |
| 是否进入日志 |  |

### 文本列表

| id | 条件补充 | 文本 | 备注 |
| --- | --- | --- | --- |
```

## Text Style

- Use precise, readable Chinese.
- Avoid overlong exposition in triggered text.
- Prefer concrete objects, actions, and sensory details over abstract lore explanation.
- Give each faction, location, or character a recognizable narrative function.
- Let mysteries create questions, but do not hide basic player motivation.
- Keep repeated UI text stable and short.

## Configuration Guidance

When configuration is needed, define:

- table name
- table purpose
- primary key
- field name
- field type
- required or optional
- description
- example value
- related table or field

Common narrative configuration tables may include:

- `world_term_config`: world terms, glossary, unlock rules
- `lore_entry_config`: lore logs and archive entries
- `anecdote_config`: anecdote metadata and trigger rules
- `trigger_text_config`: triggered text groups and display rules
- `dialogue_config`: dialogue lines, speakers, branches, and conditions
- `location_lore_config`: location descriptions and exploration text

Only add tables or fields that the current design actually needs.
