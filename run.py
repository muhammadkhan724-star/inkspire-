import uvicorn
from app.config import settings

if __name__ == "__main__":
    print("=" * 64)
    print(f"🚀 INKSPIRE BLOGGING PLATFORM IS STARTING")
    print("=" * 64)
    print(f"🌐 Public Blog URL:    {settings.SITE_URL}")
    print(f"🔐 Admin Studio URL:   {settings.SITE_URL}/admin")
    print(f"👤 Default Admin User: {settings.ADMIN_USERNAME}")
    print(f"🔑 Default Password:   {settings.ADMIN_PASSWORD}")
    print(f"🗺️ Dynamic Sitemap:    {settings.SITE_URL}/sitemap.xml")
    print(f"🤖 Robots.txt:         {settings.SITE_URL}/robots.txt")
    print(f"📡 RSS 2.0 Feed:       {settings.SITE_URL}/feed.xml")
    print("=" * 64)
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=False)
