# oracle-dba-python-tools

Oracle DB エンジニア（約6年）が、Python を1年で業務レベルにするための学習記録です。最終目標は、外資ビッグテックのソフトウェアエンジニア（SWE）になることです。

A learning log by an Oracle DB engineer (about 6 years of experience) who aims to reach a professional level in Python within one year, on the way to a software engineer (SWE) role at a big tech company.

## 現在のフェーズ / Current phase

**フェーズ0（〜2027年の帰国まで） / Phase 0 (until returning to Japan in 2027)**

| 目標 / Goal | 指標 / Metric | 状況 / Status |
|---|---|---|
| 検証環境向けの Python ツールを作る / Build Python tools for test environments | 公開したツール数 / Tools published | 0 |
| LeetCode Easy を50問解く / Solve 50 LeetCode Easy problems | 解いた問題数 / Problems solved | 0 / 50 |
| 実績を数字で記録する / Record results in numbers | 数字つきの成果 / Quantified results | 0 |

ツールの候補 / Tool ideas:

- AWR レポートの解析 / AWR report analyzer
- alert.log の要約 / alert.log summarizer
- パッチ適用前チェック / Pre-patch checklist runner

## ディレクトリ構成 / Layout

```
logs/        日次の学習ログ / Daily learning logs (YYYY-MM-DD.md)
exercises/   基礎の練習と LeetCode / Basic exercises and LeetCode
tools/       検証環境向けツール / Tools for test environments
tests/       pytest のテスト / pytest tests
```

## 使い方 / Usage

```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements-dev.txt
pytest
```

日次ログは `logs/TEMPLATE.md` をコピーして `logs/YYYY-MM-DD.md` として作ります。

To write a daily log, copy `logs/TEMPLATE.md` to `logs/YYYY-MM-DD.md`.

## データの取り扱い / Data handling

このリポジトリには、顧客情報・社内情報・実環境のログを一切含めません。ツールのサンプルデータは、すべて自作のダミーデータです。

This repository contains no customer data, no internal company information, and no logs from real environments. All sample data for the tools is synthetic.

コミット前の確認 / Before each commit:

- [ ] ホスト名・IP・SID・ユーザー名・顧客名が入っていない / No hostnames, IPs, SIDs, user names, or customer names
- [ ] 実環境の AWR・alert.log・トレースファイルが入っていない / No real AWR reports, alert.logs, or trace files
- [ ] 社内の手順書や資料の内容をコピーしていない / Nothing copied from internal runbooks or documents
