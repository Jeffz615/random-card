# 随机歌曲洗牌抽卡工具

## 环境

- 操作系统：Windows
- 编程语言：python3.9

```bash
pip install -r requirement.txt
```

## 编译

```bash
build.bat
```

## 修改卡池

修改`song.json`即可

格式如下：
```json
{
  "port": 8000, // 本地监听端口
  "langs_group": [
    {
      "title": "中文普通话曲目", // 标题 
      "label": "C", // 前缀
      "langs": [
        [
          "zh_cn", // 对应的items项
          "中文（普通话）" // 语种
        ]
      ]
    },
    {
      "title": "其他曲目",
      "label": "F",
      "langs": [
        [
          "zh_yue",
          "中文（粤语）"
        ]
      ]
    }
  ],
  "items": {
    "zh_cn": [
      [
        "天亮了", // 歌名
        "韩红" // 歌手
      ],
      [
        "爱我吧",
        "方大同"
      ]
    ],
    "zh_yue": [
      [
        "静夜的单簧管",
        "张敬轩/王菲/林忆莲"
      ],
      [
        "李香兰",
        "张学友(2000年版)"
      ]
    ]
  }
}
```

## 运行

-> **双击main.exe**