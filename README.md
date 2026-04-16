# ExitBazar PHP Website — Complete Setup Guide
# Hindi + English mein samjhaya gaya hai

---

## 📦 Aapko kya chahiye (Requirements)

1. **XAMPP** — Free software jo PHP + MySQL aapke computer pe run karta hai
2. **Internet connection** — YouTube API ke liye
3. **Text editor** — Notepad++ ya VS Code (free)

---

## STEP 1 — XAMPP Install Karo

1. Go to → **apachefriends.org**
2. "XAMPP for Windows" download karo (free)
3. Install karo — sab default settings rakho
4. Open XAMPP Control Panel
5. **Apache** ke saamne "Start" button dabao ✅
6. **MySQL** ke saamne "Start" button dabao ✅
7. Dono green ho jayenge — iska matlab server chal raha hai

---

## STEP 2 — Files Paste Karo

1. XAMPP install folder dhundho: **C:\xampp\htdocs\**
2. Wahan ek naya folder banao: **exitbazar**
3. Is package ke SAARE files us folder mein paste karo
4. Final path aisa dikhna chahiye:

```
C:\xampp\htdocs\exitbazar\
├── index.php
├── listings.php
├── listing.php
├── login.php
├── post.php
├── seller-dashboard.php
├── buyer-dashboard.php
├── deal-room.php
├── trust.php
├── pricing.php
├── logout.php
├── schema.sql
├── config/
│   └── db.php
├── includes/
│   ├── header.php
│   └── footer.php
├── assets/
│   ├── css/style.css
│   └── js/main.js
└── api/
    └── youtube.php
```

---

## STEP 3 — Database Banao (MySQL)

1. Browser mein type karo: **http://localhost/phpmyadmin**
2. Left sidebar mein "New" click karo
3. Database name mein type karo: **exitbazar**
4. Collation select karo: **utf8mb4_unicode_ci**
5. "Create" button dabao
6. Ab top mein "SQL" tab click karo
7. **schema.sql** file kholo (Notepad se)
8. Saara code copy karo (Ctrl+A then Ctrl+C)
9. phpMyAdmin ke SQL box mein paste karo
10. "Go" button dabao
11. Green message dikhega: "ExitBazar database created successfully!" ✅

---

## STEP 4 — Config File Update Karo

**config/db.php** file kholo aur ye lines update karo:

```php
define('DB_HOST', 'localhost');       // yahi rehne do
define('DB_USER', 'root');            // XAMPP ka default user
define('DB_PASS', '');                // XAMPP mein password nahi hota by default
define('DB_NAME', 'exitbazar');       // yahi rehne do

define('SITE_URL', 'http://localhost/exitbazar');  // yahi rehne do

define('RAZORPAY_KEY_ID', 'rzp_test_XXXXXXXXXX');      // apna Razorpay key
define('RAZORPAY_KEY_SECRET', 'XXXXXXXXXXXXXXXXXX');   // apna Razorpay secret
define('YOUTUBE_API_KEY', 'YOUR_YOUTUBE_API_KEY');      // apna YouTube API key
```

---

## STEP 5 — YouTube API Key Kaise Milega

1. Go to → **console.cloud.google.com**
2. Naya project banao: "exitbazar"
3. "APIs & Services" → "Enable APIs"
4. Search karo "YouTube Data API v3" → Enable
5. "Credentials" → "Create Credentials" → "API Key"
6. Key copy karo → config/db.php mein paste karo

---

## STEP 6 — Razorpay Account

1. Go to → **razorpay.com** → Sign Up
2. Dashboard → Settings → API Keys
3. "Generate Test Key" click karo
4. Key ID aur Key Secret copy karo → config/db.php mein paste karo

---

## STEP 7 — Website Chalao

Browser mein type karo:
```
http://localhost/exitbazar
```

Aapki website khul jayegi! 🎉

---

## STEP 8 — Live Server pe Deploy Karna (Later)

Jab aap ready ho jao live karne ke liye:

1. **Hosting buy karo** (Hostinger ya SiteGround India)
   - PHP 8.0+ support hona chahiye
   - MySQL support
   - Cost: ~₹100-200/month

2. **cPanel** mein jaao → **File Manager**
3. **public_html** folder mein saare files upload karo

4. **Database banao:**
   - cPanel → MySQL Databases
   - Naya database + user banao
   - phpMyAdmin mein schema.sql import karo

5. **config/db.php update karo:**
   ```php
   define('DB_HOST', 'localhost');
   define('DB_USER', 'your_cpanel_db_user');
   define('DB_PASS', 'your_db_password');
   define('DB_NAME', 'your_db_name');
   define('SITE_URL', 'https://yourdomain.com');
   ```

6. Apna domain point karo hosting server pe

---

## ✅ Website Pages — Kahan Kya Hai

| File | URL | Description |
|---|---|---|
| index.php | / | Home page |
| listings.php | /listings.php | Browse channels |
| listing.php?id=1 | /listing.php?id=1 | Channel detail |
| login.php | /login.php | Login & Register |
| post.php | /post.php | List your channel |
| seller-dashboard.php | /seller-dashboard.php | Seller ka control panel |
| buyer-dashboard.php | /buyer-dashboard.php | Buyer ka control panel |
| deal-room.php?id=1 | /deal-room.php?id=1 | Secure chat + escrow |
| trust.php | /trust.php | How It Works |
| pricing.php | /pricing.php | Pricing |
| logout.php | /logout.php | Logout |

---

## 🔧 Common Problems aur Solutions

**Problem: Blank white page**
Solution: config/db.php mein DB_USER aur DB_PASS check karo

**Problem: "Connection failed" error**
Solution: XAMPP mein MySQL start hai ya nahi check karo

**Problem: YouTube API kaam nahi kar raha**
Solution: YouTube API key sahi hai ya nahi, aur API enable hai ya nahi check karo

**Problem: Images nahi dikh rahe**
Solution: Browser mein Ctrl+Shift+J dabao — console error dekho

---

## 📞 Support

Koi problem aaye to mujhe batao, main help karunga!

Admin login (default):
- Email: admin@exitbazar.com  
- Password: password (change kar dena!)
