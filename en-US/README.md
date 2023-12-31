# What is decentralized finance (DeFi)?

## 欢迎使用 `Arya` 在线 Markdown 编辑器

[Arya](https://markdown.lovejade.cn/?utm\_source=markdown.lovejade.cn)，是一款基于 `Vue`、`Vditor`，为未来而构建的在线 Markdown 编辑器；轻量且强大：内置粘贴 HTML 自动转换为 Markdown，支持流程图、甘特图、时序图、任务列表，可导出携带样式的图片、PDF、微信公众号特制的 HTML 等等。

***

### 如何使用

**微注**：清空目前这份默认文档，即处于可使用态。[Arya](https://markdown.lovejade.cn/?utm\_source=markdown.lovejade.cn) 另一大优点在于：编辑内容只会在您本地进行保存，不会上传您的数据至服务器，**绝不窥测用户个人隐私，可放心使用**；Github 源码：[markdown-online-editor](https://github.com/nicejade/markdown-online-editor)，部分功能仍在开发🚧，敬请期待。

默认为[所见即所得](https://hacpai.com/article/1577370404903?utm\_source=github.com)模式，可通过 `⌘-⇧-M`（`Ctrl-⇧-M`）进行切换；或通过以下方式：

* 所见即所得：`⌘-⌥-7`（`Ctrl-alt-7`）；
* 即时渲染：`⌘-⌥-8`（`Ctrl-alt-8`）；
* 分屏渲染：`⌘-⌥-9`（`Ctrl-alt-9`）；

#### PPT 预览

如果您用作 `PPT` 预览（入口在`设置`中），需要注意，这里暂还不能支持各种图表的渲染；您可以使用 `---` 来定义水平方向上幻灯片，用 `--` 来定义垂直幻灯片；更多设定可以参见 [RevealJs 文档](https://github.com/hakimel/reveal.js#table-of-contents)。

***

***

#### 1. 制作待办事宜 `Todo` 列表

* [x] 🎉 通常 `Markdown` 解析器自带的基本功能；
* [x] 🍀 支持**流程图**、**甘特图**、**时序图**、**任务列表**；
* [x] 🏁 支持粘贴 HTML 自动转换为 Markdown；
* [x] 💃🏻 支持插入原生 Emoji、设置常用表情列表；
* [x] 🚑 支持编辑内容保存**本地存储**，防止意外丢失；
* [x] 📝 支持**实时预览**，主窗口大小拖拽，字符计数；
* [x] 🛠 支持常用快捷键(**Tab**)，及代码块添加复制
* [x] ✨ 支持**导出**携带样式的 PDF、PNG、JPEG 等；
* [x] ✨ 升级 Vditor，新增对 `echarts` 图表的支持；
* [x] 👏 支持检查并格式化 Markdown 语法，使其专业；
* [x] 🦑 支持五线谱、及[部分站点、视频、音频解析](https://github.com/b3log/vditor/issues/117?utm\_source=hacpai.com#issuecomment-526986052)；
* [x] 🌟 增加对**所见即所得**编辑模式的支持(`⌘-⇧-M`)；

***

#### 2. 书写一个质能守恒公式\[^LaTeX]

$$
E=mc^2
$$

***

#### 3. 高亮一段代码\[^code]

```js
// 给页面里所有的 DOM 元素添加一个 1px 的描边（outline）;
[].forEach.call($$("*"),function(a){
  a.style.outline="1px solid #"+(~~(Math.random()*(1<<24))).toString(16);
})
```

#### 4. 高效绘制[流程图](https://github.com/knsv/mermaid#flowchart)

```mermaid
graph TD;
  A-->B;
  A-->C;
  B-->D;
  C-->D;
```

#### 5. 高效绘制[序列图](https://github.com/knsv/mermaid#sequence-diagram)

```mermaid
sequenceDiagram
  participant Alice
  participant Bob
  Alice->John: Hello John, how are you?
  loop Healthcheck
      John->John: Fight against hypochondria
  end
  Note right of John: Rational thoughts <br/>prevail...
  John-->Alice: Great!
  John->Bob: How about you?
  Bob-->John: Jolly good!
```

#### 6. 高效绘制[甘特图](https://github.com/knsv/mermaid#gantt-diagram)

> **甘特图**内在思想简单。基本是一条线条图，横轴表示时间，纵轴表示活动（项目），线条表示在整个期间上计划和实际的活动完成情况。它直观地表明任务计划在什么时候进行，及实际进展与计划要求的对比。

```mermaid
gantt
  title 项目开发流程
  section 项目确定
    需求分析       :a1, 2019-06-22, 3d
    可行性报告     :after a1, 5d
    概念验证       : 5d
  section 项目实施
    概要设计      :2019-07-05  , 5d
    详细设计      :2019-07-08, 10d
    编码          :2019-07-15, 10d
    测试          :2019-07-22, 5d
  section 发布验收
    发布: 2d
    验收: 3d
```

#### 7. 支持图表

```echarts
{
  "backgroundColor": "#212121",
  "title": {
    "text": "「晚晴幽草轩」访问来源",
    "subtext": "2019 年 6 月份",
    "x": "center",
    "textStyle": {
      "color": "#f2f2f2"
    }
  },
  }
```

> **备注**：上述 echarts 图表📈，其数据，须使用严格的 **JSON** 格式；您可使用 JSON.stringify(data)，将对象传换从而得标准数据，即可正常使用。

#### 8. 绘制表格

| 作品名称  | 在线地址                                                                                          |    上线日期    |
| ----- | --------------------------------------------------------------------------------------------- | :--------: |
| 倾城之链  | [https://nicelinks.site](https://nicelinks.site/??utm\_source=markdown.lovejade.cn)           | 2017-09-20 |
| 晚晴幽草轩 | [https://jeffjade.com](https://jeffjade.com/??utm\_source=markdown.lovejade.cn)               | 2014-09-20 |
| 静轩之别苑 | [http://quickapp.lovejade.cn](http://quickapp.lovejade.cn/??utm\_source=markdown.lovejade.cn) | 2019-01-12 |

####

最新更新于 2019.08.21
