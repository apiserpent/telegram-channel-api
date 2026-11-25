# Telegram Channel API

Read any public Telegram channel: subscriber count, description and recent posts with views and reactions as JSON.

Powered by [Serpent API](https://apiserpent.com). Full reference: **[Telegram Channel API docs](https://apiserpent.com/telegram-channel-api)**.

## Quick start

1. Get an API key at [apiserpent.com](https://apiserpent.com). Every account starts with 10 free API calls.
2. Call the endpoint with your key in the `X-API-Key` header:

```bash
curl -G "https://apiserpent.com/api/telegram/channel" \
  --data-urlencode "channel=durov" \
  -H "X-API-Key: $SERPENT_API_KEY"
```

## Endpoint

`GET https://apiserpent.com/api/telegram/channel`

| Parameter | Required | Description |
| --- | --- | --- |
| `channel` | Yes | Public channel username, with or without `@`, or a `t.me/` link |
| `before` | No | Return posts older than this post id. Use `next_before` from the previous response. |

## Response

`success`, `channel`, `title`, `description`, `subscribers`, `photo_url`, `preview_enabled`, `posts[]` (up to 20, newest first), `next_before`. Each post has `id`, `url`, `date`, `text`, `views`, `photos[]`, `videos[]`, `link_preview`, `reactions[]`.

See the [docs](https://apiserpent.com/telegram-channel-api) for the complete field list and sample responses.

## Examples

| File | Language | Run |
| --- | --- | --- |
| [`example.py`](example.py) | Python 3 (`pip install requests`) | `SERPENT_API_KEY=sk_live_... python example.py` |
| [`example.mjs`](example.mjs) | Node.js 18+ (no dependencies) | `SERPENT_API_KEY=sk_live_... node example.mjs` |

## Use cases

- Channel monitoring and alerting
- Social listening and OSINT research
- Archiving public channel posts

## More from Serpent API

- [Serpent API docs](https://apiserpent.com/docs) - Google, Bing, Yahoo, DuckDuckGo and Brave search, plus AI rank tracking
- [All SDKs and tools on GitHub](https://github.com/apiserpent)

## License

MIT
