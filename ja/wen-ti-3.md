<h1>👩🏫 質問 3</h1>
<p>&amp;#x20;:拍手:fq2</p>
<ol start="2">
<li><strong>GitHub Actions ワークフローをトリガーする</strong>: メイン ブランチにプッシュした後、GitHub Actions ワークフローが自動的にトリガーされ、<code>zh-CN</code> フォルダー内の Markdown ファイルの英語への翻訳が開始されます。対応するターゲット ディレクトリに保存します。 (<code>en-US</code> など)、元のファイル ディレクトリ構造を維持します。</li>
</ol>
<p>GitHub リポジトリに必要なファイルと依存関係が含まれていることを確認してから、上記の手順に従うと、翻訳プロセスを自動化できます。ファイルを他の言語に翻訳する必要がある場合は、ワークフロー ファイル内のターゲット ディレクトリ名を適宜変更してください (例: フランス語の場合は <code>fr-FR</code>)。</p>