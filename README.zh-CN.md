[English](README.md) | **简体中文**

# Telegram 频道 API

读取任意公开 Telegram 频道：订阅数、简介以及最新帖子（含浏览量和表情回应），以 JSON 返回。

由 [Serpent API](https://apiserpent.com) 提供。完整文档：**[Telegram Channel API 文档](https://apiserpent.com/telegram-channel-api)**。

## 快速开始

1. 在 [apiserpent.com](https://apiserpent.com) 注册并获取 API Key，每个账号赠送 10 次免费调用。
2. 在请求头 `X-API-Key` 中带上你的 Key 调用接口：

```bash
curl -G "https://apiserpent.com/api/telegram/channel" \
  --data-urlencode "channel=durov" \
  -H "X-API-Key: $SERPENT_API_KEY"
```

## 接口

`GET https://apiserpent.com/api/telegram/channel`

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| `channel` | 是 | 公开频道用户名，可带或不带 `@`，也可以是 `t.me/` 链接 |
| `before` | 否 | 返回早于该帖子 id 的内容；翻页时传入上一次响应的 `next_before`。 |

## 返回结果

顶层字段：`success`、`channel`、`title`、`description`、`subscribers`、`photo_url`、`preview_enabled`、`posts[]`（最多 20 条，最新在前）、`next_before`。每条帖子包含 `id`、`url`、`date`、`text`、`views`、`photos[]`、`videos[]`、`link_preview`、`reactions[]`。

完整字段列表和响应示例请参阅[文档](https://apiserpent.com/telegram-channel-api)。

## 示例代码

| 文件 | 语言 | 运行方式 |
| --- | --- | --- |
| [`example.py`](example.py) | Python 3（`pip install requests`） | `SERPENT_API_KEY=sk_live_... python example.py` |
| [`example.mjs`](example.mjs) | Node.js 18+（无需依赖） | `SERPENT_API_KEY=sk_live_... node example.mjs` |

## 应用场景

- 频道监控与告警
- 社交媒体舆情与开源情报研究
- 公开频道内容归档

## Serpent API 的更多能力

- [Serpent API 文档](https://apiserpent.com/docs)：Google、Bing、Yahoo、DuckDuckGo 和 Brave 搜索结果，以及 AI 引用排名跟踪
- [GitHub 上的全部 SDK 与工具](https://github.com/apiserpent)

## 许可证

MIT
