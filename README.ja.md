# deno_robot

DenoからWindows/Macのマウスとキーボードの操作を自動化するためのライブラリです。

このプロジェクトはクライアント・サーバーアーキテクチャを採用しています。Denoクライアントから軽量なPythonサーバーへHTTPリクエストを送信し、サーバー側で `PyAutoGUI` を使用してホストマシンのデスクトップを制御します。

## 機能

-   **マウス制御**: カーソルの移動、左クリック・右クリックの実行、現在のマウス位置の取得が可能です。
-   **キーボード制御**: 個別のキーの押下・解放、キーの長押し、文字列の入力が可能です。
-   **画面情報**: 画面の解像度を取得できます。

## 必要条件

-   Deno（クライアント用）
-   Python 3（サーバー用）
-   Pythonライブラリ: `Flask`, `PyAutoGUI`

## 使い方

### 1. サーバーのセットアップ（Python）

制御したいマシンでサーバーを実行します。

1.  **Pythonの依存パッケージをインストール:**
    ```sh
    pip3 install flask pyautogui
    ```

2.  **（オプション）ネットワークアクセスの設定:**
    デフォルトでは、サーバーは `localhost`（`127.0.0.1` および `::1`）からのリクエストのみを受け付けます。他のマシンからの接続を許可するには、`allow_networks.json` を編集し、アクセスを許可したいIPアドレスまたはネットワーク範囲を追加してください。

3.  **サーバーを実行:**
    ```sh
    python3 server.py
    ```
    *注意: サーバーはデフォルトでポート80を使用します。一部のシステムでは管理者権限または `sudo` が必要になる場合があります。*

### 2. クライアントの使用（Deno）

サーバーにアクセスできる任意のマシンでDenoスクリプトを実行します。

1.  **Denoのインストール:**
    https://deno.land/ の指示に従ってください。

2.  **サンプルスクリプトの実行:**
    リポジトリには機能を確認するためのサンプルが含まれています。

    *   **一連の操作の自動化 (`sample.js`):**
        このスクリプトはマウスの移動、クリック、キー入力を行います。macOSでは、この一連の操作により「このMacについて」ウィンドウが開きます。
        ```sh
        deno run -A sample.js
        ```

    *   **マウス位置の監視 (`poswatch.js`):**
        このスクリプトは継続的にポーリングを行い、マウスの座標が変化するたびにその位置を出力します。
        ```sh
        deno run -A poswatch.js
        ```

### 自身のプロジェクトで `Robot` クラスを使用する

`Robot` クラスをインポートして、独自の自動化スクリプトを作成できます。

```javascript
import { Robot } from "https://deno.land/x/deno_robot/Robot.js";
import { sleep } from "https://deno.land/x/sleep/mod.ts";

// サーバーに接続します。エンドポイントが指定されていない場合、デフォルトで "http://localhost/" が使用されます。
const robot = new Robot();

// 画面サイズを取得
const screenSize = await robot.screenSize();
console.log("Screen size:", screenSize); // 例: "1920,1080"

// 画面の中央にマウスを移動
const [width, height] = screenSize.split(",").map(Number);
await robot.mouseMove(width / 2, height / 2);
await sleep(1);

// 右クリックを実行
await robot.mouseClickRight();
await sleep(1);

// メッセージを入力
await robot.keyType("Hello from Deno!");
```

## ライセンス

MIT License — 詳細は [LICENSE](LICENSE) を参照してください。
