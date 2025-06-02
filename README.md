# 🛍️ Digital Product Shop (Backend)

這是一個以 FastAPI + Firebase 為基礎的數位商品販售後端，支援 Google 登入、訂單建立、Stripe 金流、授權下載等功能。

---

## 🚀 快速開始

### 安裝 Poetry（如果尚未安裝）

```bash
curl -sSL https://install.python-poetry.org | python
```

### 初始化專案

```bash
git clone https://github.com/ayililili/digital-shop-backend.git
cd digital-shop-backend
poetry install
cp .env.example .env  # 編輯環境變數
```

### 執行應用

```bash
poetry run uvicorn app.main:app --reload
```

---

## 📁 專案結構

- `app/main.py` - FastAPI 應用啟動
- `app/api/` - API 路由模組
- `app/core/` - 設定、JWT、CORS 等核心工具
- `app/services/` - 外部服務封裝（Firestore、Firebase、Stripe、GCS）
- `app/schemas/` - Pydantic 資料結構，用於 API 輸入/輸出驗證

---

## 🔐 登入流程

1. 前端使用 Google 登入，取得 `id_token`
2. 傳送 `POST /google-login` 至後端
3. 後端透過 Firebase 驗證 `id_token`
4. 查詢（或建立）Firestore 使用者紀錄
5. 回傳簽發的 JWT 與使用者資料

---

## 🛠️ TODO

- [x] Google 登入驗證流程
- [x] Firebase 驗證與 Firestore 使用者建立
- [x] JWT 簽發與驗證
- [x] Refresh Token 產生與 Access Token 換發機制
- [ ] 使用 Redis 儲存 Refresh Token（含 TTL）
- [ ] 商品管理 API
- [ ] Stripe Checkout 整合
- [ ] Stripe Webhook 處理訂單
- [ ] 建立訂單紀錄
- [ ] 檔案上傳與 GCS 授權下載（signed URL）
- [ ] 管理後台（可選）
- [ ] Logging、錯誤處理優化
- [ ] API 測試與文件產出（Swagger / Redoc）

---

## 📄 License

MIT © Ayi
