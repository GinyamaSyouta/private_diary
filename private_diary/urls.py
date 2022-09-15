from django.contrib import admin
from django.contrib.staticfiles.urls import static
from django.urls import path, include

from . import settings_common, settings_dev

urlpatterns = [
    path('admin/', admin.site.urls),
    # adminはデフォルトの管理者画面用

    path('blog/', include('blog.urls')),

    path('', include('diary.urls')),
    # http://localhost:8000/ (FQDNとポート番号以外何もパスの指定なし)のときは
    # diaryフォルダ内のurlsクラスを呼び出す

    path('accounts/', include('allauth.urls')),
]

# 開発サーバでメディアを配信できるようにする設定
urlpatterns += static(settings_common.MEDIA_URL, document_root=settings_dev.MEDIA_ROOT)
