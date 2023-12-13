from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import ArticlePost
# 引入定義的ArticlePostForm表單類
from .forms import ArticlePostForm
# 引入User模型
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import markdown
from django.core.paginator import Paginator
from django.db.models import Q
from comment.models import Comment
from .models import ArticleColumn

# 文章列表
def article_list(request):
    search = request.GET.get('search')
    order = request.GET.get('order')
    column = request.GET.get('column')
   
    # 初始化查詢集
    article_list = ArticlePost.objects.all()

    # 搜詢查詢集
    if search:
        article_list = article_list.filter(
            Q(title__icontains=search) |
            Q(body__icontains=search)
        )
    else:
        # 將 search 參數重置為空
        search = ''

    # 分類查詢集
    if column is not None and column.isdigit():
        article_list = article_list.filter(column=column)

   
    # 查詢集排序
    if order == 'total_views':
        # 按熱度排序文章
        article_list = article_list.order_by('-total_views')

    paginator = Paginator(article_list, 3)
    page = request.GET.get('page')
    articles = paginator.get_page(page)

    context = {'articles': articles, 'order': order, 'search': search, 'column': column,
               }

    return render(request, 'article/list.html', context)

# 文章詳情
def article_detail(request, id):
    # 取出相應的文章
    article = ArticlePost.objects.get(id=id)
    # 取出文章評論
    comments = Comment.objects.filter(article=id)
    # 瀏覽量 +1
    article.total_views += 1
    article.save(update_fields=['total_views'])

    md = markdown.Markdown(
        extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
        ]
    )
    article.body = md.convert(article.body)

    context = {'article': article, 'toc': md.toc, 'comments': comments}
    return render(request, 'article/detail.html', context)

# 寫文章的view


@login_required(login_url='/userprofile/login/')
def article_create(request):
    # 判斷用戶是否提交數據
    if request.method == "POST":
        article_post_form = ArticlePostForm(request.POST, request.FILES)
       
        # 判斷提交的數據是否滿足模型的要求
        if article_post_form.is_valid():
            # 保存數據，但暫時不提交到數據庫中
            new_article = article_post_form.save(commit=False)
            # 指定目前登入的用戶為作者
            new_article.author = User.objects.get(id=request.user.id)

            if request.POST['column'] != 'none':
                new_article.column = ArticleColumn.objects.get(
                    id=request.POST['column'])
            # 將新文章保存到數據庫中
            new_article.save()

            article_post_form.save_m2m()

            # 完成後返回到文章列表
            return redirect("article:article_list")
        # 如果數據不合法，返回錯誤信息
        else:
            return HttpResponse("表單內容有誤，請重新填寫。")
    # 如果用戶請求獲取數據
    else:
        # 創建表單類實例
        article_post_form = ArticlePostForm()
        columns = ArticleColumn.objects.all()

        # 賦值上下文
        context = {'article_post_form': article_post_form, 'columns': columns}
        # 返回模板
        return render(request, 'article/create.html', context)

# 安全刪除文章


@login_required(login_url='/userprofile/login/')
def article_safe_delete(request, id):
    if request.method == 'POST':
        article = ArticlePost.objects.get(id=id)
        article.delete()
        return redirect("article:article_list")
    else:
        return HttpResponse("僅允許post請求")

# 更新文章


@login_required(login_url='/userprofile/login/')
def article_update(request, id):
    """
    更新文章的視圖函數
    通過POST方法提交表單,更新titile、body字段
    GET方法進入初始表單頁面
    id: 文章的 id
    """

    # 獲取需要修改的具體文章對象
    article = ArticlePost.objects.get(id=id)
    # 過濾非作者的用户
    if request.user != article.author:
        return HttpResponse("抱歉，你無權修改这篇文章。")

    # 判斷用戶是否為 POST 提交表單數據
    if request.method == "POST":
        # 將提交的數據賦值到表單實例中
        article_post_form = ArticlePostForm(data=request.POST)
        # 判斷提交的數據是否滿足模型的要求
        if article_post_form.is_valid():
            # 保存新寫入的 title、body 數據並保存
            article.title = request.POST['title']
            article.body = request.POST['body']
            if request.POST['column'] != 'none':
                article.column = ArticleColumn.objects.get(
                    id=request.POST['column'])
            else:
                article.column = None
                
            if request.FILES.get('avatar'):
                article.avatar = request.FILES.get('avatar')
            article.save()
            
            # 完成後返回到修改後的文章中。需傳入文章的 id 值
            return redirect("article:article_detail", id=id)
        # 如果數據不合法，返回錯誤信息
        else:
            return HttpResponse("表單內容有誤，請重新填寫。")

    # 如果用戶 GET 請求獲取數據
    else:
        # 創建表單類實例
        article_post_form = ArticlePostForm()
        columns = ArticleColumn.objects.all()
        # 賦值上下文，將 article 文章對象也傳遞進去，以便提取舊的內容
        context = {'article': article, 'article_post_form': article_post_form,
                   'columns': columns, }
        # 將響應返回到模板中
        return render(request, 'article/update.html', context)
