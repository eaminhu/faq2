<h1>分散型金融 (DeFi) とは何ですか?</h1>
<h2><code>Arya</code> オンライン Markdown エディタへようこそ</h2>
<p><a href="https://markdown.lovejade.cn/?utm_source=markdown.lovejade.cn">Arya</a> は、<code>Vue</code>、<code> に基づくソフトウェアです。 Vditor</code> は、将来のために構築されたオンライン Markdown エディターです。軽量かつ強力です。組み込みの貼り付け HTML は自動的に Markdown に変換され、フローチャート、ガント チャート、シーケンス図、タスク リストをサポートし、スタイル付きの画像や PDF をエクスポートできます。 、WeChat 公開アカウント用に特別に設計された HTML など。 </p>
<hr />
<h3>使用方法</h3>
<p><strong>マイクロ ノート</strong>: 現在のデフォルトのドキュメントをクリアすると、使用できるようになります。 <a href="https://markdown.lovejade.cn/?utm_source=markdown.lovejade.cn">Arya</a> もう 1 つの大きな利点は、編集したコンテンツはローカルにのみ保存され、自分にはアップロードされないことです。データはサーバーに送信されるため、<strong>ユーザーの個人的なプライバシーが覗かれることはなく、 安心して使用できます</strong>; Github ソース コード: <a href="https://github.com/nicejade /markdown-online-editor">markdown-online-editor</a> では、一部の機能はまだ開発中です🚧ので、ご期待ください。 </p>
<p>デフォルトは <a href="https://hacpai.com/article/1577370404903?utm_source=github.com">表示されたものがそのまま得られる</a> モードで、<code> を渡すことができます。 ⌘-⇧-M</code>(<code>Ctrl-⇧-M</code>) で切り替えるか、次の方法で切り替えます。</p>
<ul>
<li>表示されているものがそのまま得られます: <code>⌘-⌥-7</code> (<code>Ctrl-alt-7</code>);</li>
<li>インスタント レンダリング: <code>⌘-⌥-8</code> (<code>Ctrl-alt-8</code>);</li>
<li>分割画面レンダリング: <code>⌘-⌥-9</code> (<code>Ctrl-alt-9</code>);</li>
</ul>
<h4>PPT プレビュー</h4>
<p>これを <code>PPT</code> プレビューとして使用する場合 (入口は <code>Settings</code> にあります)、さまざまなグラフのレンダリングはまだサポートされていないことに注意してください。< を使用できます。 code> ---</code> は水平スライドを定義し、<code>--</code> は垂直スライドを定義します。詳細な設定については、<a href="https://github.com/hakimel" を参照してください。 /reveal.js#table-of-contents">RevealJs ドキュメント</a>。 </p>
<hr />
<hr />
<h4>1. ToDo <code>Todo</code> リストを作成する</h4>
<ul>
<li>[x] 🎉 通常、<code>Markdown</code> はパーサーに付属する基本関数です。</li>
<li>[x] 🍀 <strong>フローチャート</strong>、<strong>ガント チャート</strong>、<strong>シーケンス図</strong>、<strong>タスク リスト</strong>をサポートします;< /li >
<li>[x] 🏁 HTML の貼り付けと Markdown への自動変換をサポートします。</li>
<li>[x] 💃🏻 ネイティブ絵文字の挿入と、よく使用される絵文字のリストの設定をサポートします。</li>
<li>[x] 🚑 偶発的な損失を防ぐために、編集したコンテンツを<strong>ローカル ストレージ</strong>に保存することをサポートします。</li>
<li>[x] 📝<strong>リアルタイム プレビュー</strong>、メイン ウィンドウ サイズのドラッグ、文字カウントをサポートします。</li>
<li>[x] 🛠 よく使用されるショートカット キー (<strong>Tab</strong>) とコード ブロックの追加とコピーをサポートします</li>
<li>[x] ✨ PDF、PNG、JPEG などのスタイル付きの<strong>エクスポート</strong>をサポートします。</li>
<li>[x] ✨ Vditor をアップグレードし、<code>echarts</code> チャートのサポートを追加します。</li>
<li>[x] 👏 プロフェッショナルなものにするための Markdown 構文のチェックと書式設定をサポートします。</li>
<li>[x] 🦑 スタッフ、および<a href="https://github.com/b3log/vditor/issues/117?utm_source=hacpai.com#issuecomment-526986052">一部のサイト、ビデオ、オーディオをサポートします分析</a>;</li>
<li>[x] 🌟 <strong>WYSIWYG</strong> 編集モード (<code>⌘-⇧-M</code>) のサポートを追加します。</li>
</ul>
<hr />
<h4>2. 質量エネルギー保存式を書く ​​[^LaTeX]</h4>
<p>$$
E=mc^2
$$</p>
<hr />
<h4>3. コード [^code] をハイライト表示します</h4>
<pre><code class=" language-js">// ページ内のすべての DOM 要素に 1 ピクセルのストローク (アウトライン) を追加します。
[].forEach.call($$("*"),function(a){
  a.style.outline=&quot;1px ソリッド #&quot;+(~~(Math.random()*(1&lt;&lt;24))).toString(16);
})
</code></pre>
<h4>4. <a href="https://github.com/knsv/mermaid#flowchart">フローチャート</a>を効率的に作成する</h4>
<pre><code class=" language-mermaid">グラフ TD;
  A-->B;
  A-->C;
  B-->D;
  C--->D;
</code></pre>
<h4>5. <a href="https://github.com/knsv/mermaid#sequence-diagram">シーケンス図</a>を効率的に描画する</h4>
<pre><code class=" language-mermaid">シーケンス図
  参加者アリス
  参加者のボブ
  アリス→ジョン: こんにちは、ジョン、調子はどうですか？
  ループヘルスチェック
      ジョン->ジョン: 心気症との戦い
  終わり
  ジョンの右の注: 合理的な考えが優先されます...
  ジョン-->アリス: 素晴らしいですね!
  ジョン→ボブ: あなたはどうですか?
  ボブ-->ジョン: いいですね!
</code></pre>
<h4>6. <a href="https://github.com/knsv/mermaid#gantt-diagram">ガント チャート</a>を効率的に作成する</h4>
<ブロック引用>
<p><strong>ガント チャート</strong> 基本的な考え方はシンプルです。これは基本的に折れ線グラフであり、横軸は時間を表し、縦軸は活動 (プロジェクト) を表し、線は全期間における活動の計画と実際の完了を表します。タスクがいつ計画されるか、および計画された要件と実際の進捗状況がどのように比較されるかを視覚的に示します。 </p>
</blockquote>
<pre><code class=" language-mermaid">ガント
  タイトルプロジェクトの開発プロセス
  セクションプロジェクトが確認されました
    需要分析:a1、2019-06-22、3D
    実現可能性レポート:a1、5d以降
    概念実証: 5d
  セクションプロジェクトの実施
    概要デザイン:2019-07-05、5d
    詳細設計:2019-07-08、10d
    コーディング:2019-07-15、10d
    テスト:2019-07-22、5d
  セクションリリース受付
    公開: 2D
    受け入れ: 3D
</code></pre>
<h4>7. サポートチャート</h4>
<pre><code class=" language-echarts">{
  "背景色": "#212121",
  「タイトル」: {
    "text": ""Wanqing Youcaoxuan" アクセス ソース",
    「サブテキスト」: 「2019 年 6 月」、
    "x": "中心"、
    "テキストスタイル": {
      「カラー」: 「#f2f2f2」
    }
  }、
  }
</code></pre>
<ブロック引用>
<p><strong>備考</strong>: 上記の echarts チャートのデータ 📈 は、厳密な <strong>JSON</strong> 形式を使用する必要があります。JSON.stringify(data) を使用してオブジェクトを転送し、標準データを取得できます。普通に使えます。 </p>
</blockquote>
<h4>8. 描画テーブル</h4>
<p>| 作品名 | オンライン アドレス | オンライン日付 |
| ----- | -------------------------------------- ---------------------------------------------------- ---- | :----------: |
| Lovejade チェーン | <a href="https://nicelinks.site/??utm_source=markdown.lovejade.cn">https://nicelinks.site</a> | 2017-09-20 |
| 万清友草軒 | <a href="https://jeffjade.com/??utm_source=markdown.lovejade.cn">https://jeffjade.com</a> | 2014-09-20 |
| Jingxuan Villa| <a href="http://quickapp.lovejade.cn/??utm_source=markdown.lovejade.cn">http://quickapp.lovejade.cn</a> | 2019-01-12 | </p>
<h4></h4>
<p>最新更新日: 2019.08.21</p>