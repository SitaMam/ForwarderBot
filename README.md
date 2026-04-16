# ExitBazar — Complete Setup Guide
## (No coding knowledge needed — follow step by step)

---

## STEP 1: Install Required Software on Your Computer

1. Go to https://nodejs.org → Download "LTS" version → Install it
2. Go to https://code.visualstudio.com → Download → Install it (this is your code editor)
3. Go to https://git-scm.com → Download → Install it

---

## STEP 2: Create Accounts (All Free)

1. **Supabase** (your database): https://supabase.com → Sign up with GitHub
2. **Vercel** (your hosting): https://vercel.com → Sign up with GitHub (you may already have this)
3. **Google Cloud Console** (YouTube API): https://console.cloud.google.com → Sign in with Google
4. **Razorpay** (payments): https://razorpay.com → Sign up as business

---

## STEP 3: Set Up Supabase Database

1. Go to https://supabase.com/dashboard
2. Click "New Project" → Name it "exitbazar" → Set a strong password → Create
3. Wait 2 minutes for it to start
4. Click "SQL Editor" in left sidebar
5. Click "New Query"
6. Copy ALL the code from the file `schema.sql` and paste it there
7. Click "Run" (green button)
8. You should see "Success" — your database is ready!

### Get your Supabase keys:
1. Go to Settings → API
2. Copy "Project URL" — save it
3. Copy "anon public" key — save it
4. Copy "service_role" key — save it (keep this SECRET, never share)

---

## STEP 4: Set Up YouTube API

1. Go to https://console.cloud.google.com
2. Create a new project called "exitbazar"
3. Click "Enable APIs and Services"
4. Search "YouTube Data API v3" → Enable it
5. Go to "Credentials" → "Create Credentials" → "API Key"
6. Copy the API key — save it

### Set up OAuth (for sellers to connect their channel):
1. Still in Google Console → Credentials → "Create Credentials" → "OAuth Client ID"
2. Application type: "Web application"
3. Name: "ExitBazar"
4. Authorized redirect URIs: Add `https://exitbazar.vercel.app/api/auth/callback/google`
5. Also add `http://localhost:3000/api/auth/callback/google` (for testing)
6. Click Create → Copy Client ID and Client Secret — save them

---

## STEP 5: Set Up Razorpay

1. Go to https://dashboard.razorpay.com
2. Sign in → Go to Settings → API Keys
3. Generate Test Key (for testing first)
4. Copy Key ID and Key Secret — save them

---

## STEP 6: Download and Set Up the Project

Open "Terminal" (Mac) or "Command Prompt" (Windows) and type these commands one by one:

```bash
# 1. Download the project template
npx create-next-app@14 exitbazar --tailwind --app --no-typescript --no-eslint

# 2. Go into the folder
cd exitbazar

# 3. Install all required packages
npm install @supabase/supabase-js @supabase/auth-helpers-nextjs recharts lucide-react razorpay googleapis next-auth

# 4. Open in VS Code
code .
```

---

## STEP 7: Create Environment Variables File

In VS Code, create a new file called `.env.local` in the root of your project.
Paste this and fill in YOUR values:

```env
# Supabase
NEXT_PUBLIC_SUPABASE_URL=your_supabase_project_url_here
NEXT_PUBLIC_SUPABASE_ANON_KEY=your_supabase_anon_key_here
SUPABASE_SERVICE_ROLE_KEY=your_supabase_service_role_key_here

# YouTube / Google
YOUTUBE_API_KEY=your_youtube_api_key_here
GOOGLE_CLIENT_ID=your_google_client_id_here
GOOGLE_CLIENT_SECRET=your_google_client_secret_here

# Razorpay
RAZORPAY_KEY_ID=your_razorpay_key_id_here
RAZORPAY_KEY_SECRET=your_razorpay_key_secret_here
NEXT_PUBLIC_RAZORPAY_KEY_ID=your_razorpay_key_id_here

# NextAuth
NEXTAUTH_URL=http://localhost:3000
NEXTAUTH_SECRET=any_random_long_string_at_least_32_characters

# App
NEXT_PUBLIC_APP_URL=http://localhost:3000
```

---

## STEP 8: Copy All Code Files

Copy each file from this package into the correct location in your project.
The folder structure should look like this:

```
exitbazar/
├── .env.local                    ← you just created this
├── schema.sql                    ← paste in Supabase SQL editor
├── package.json
├── next.config.js
├── tailwind.config.js
├── app/
│   ├── layout.js
│   ├── page.js                   ← Home page
│   ├── globals.css
│   ├── listings/
│   │   ├── page.js               ← Browse listings
│   │   └── [id]/
│   │       └── page.js           ← Single listing
│   ├── post/
│   │   └── page.js               ← Post a listing (seller)
│   ├── login/
│   │   └── page.js               ← Login page
│   ├── seller/
│   │   └── dashboard/
│   │       └── page.js           ← Seller dashboard
│   ├── buyer/
│   │   └── dashboard/
│   │       └── page.js           ← Buyer dashboard
│   ├── deal-room/
│   │   └── [id]/
│   │       └── page.js           ← Deal room
│   └── api/
│       ├── auth/
│       │   └── [...nextauth]/
│       │       └── route.js      ← Auth handler
│       ├── youtube/
│       │   └── route.js          ← YouTube API
│       ├── listings/
│       │   └── route.js          ← Listings CRUD
│       ├── razorpay/
│       │   └── route.js          ← Payment handler
│       └── requests/
│           └── route.js          ← Buyer requests
├── components/
│   ├── Navbar.js
│   ├── ListingCard.js
│   ├── ChannelStats.js
│   ├── ValuationBadge.js
│   └── TrustBadge.js
└── lib/
    ├── supabase.js
    └── youtube.js
```

---

## STEP 9: Run Locally to Test

```bash
npm run dev
```

Open browser → go to http://localhost:3000
You should see ExitBazar running!

---

## STEP 10: Deploy to Vercel

1. Push your code to GitHub:
```bash
git init
git add .
git commit -m "Initial ExitBazar build"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/exitbazar.git
git push -u origin main
```

2. Go to https://vercel.com/dashboard
3. Click "New Project" → Import from GitHub → Select exitbazar
4. Add all your environment variables (same as .env.local)
5. Click Deploy!

---

## You're Live! 🚀

Your site will be at https://exitbazar.vercel.app

---

## Need Help?
If anything doesn't work, the most common issues are:
- Wrong environment variable values
- Not running the schema.sql in Supabase
- Forgot to enable YouTube API

