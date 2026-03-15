# deno_robot

Denoを使ってWindows/Macのマウスとキーボードを操作するライブラリです。

## 機能
- マウスカーソルの移動
- マウスクリック(左クリック、右クリック)
- キーボード入力(キーの押下、リリース、入力)

## 必要環境
- Python 3
- Flask
- PyAutoGUI

## 使い方
### サーバーの設定
1. 必要なライブラリをインストールします:
   ```sh
   pip3 install flask
   pip3 install pyautogui
   ```
2. サーバーを起動します:
   ```sh
   python3 server.py
   ```

### クライアントの使用
1. Denoをインストールします: https://deno.land/
2. サンプルスクリプトを実行します:
   ```sh
   deno run -A sample.js
   ```

サンプルスクリプトでは以下の操作が行われます:
- マウスカーソルを座標(10, 10)に移動
- マウスをクリック
- "down"キーを押下
- "enter"キーを押下

## ライセンス
MIT License