from flask import jsonify, request
from helper import is_isbn_or_key
from yushu_book import YuShuBook
from app.forms.bookfrom import SearchForm

from . import web

@web.route('/book/search/<q>/<page>')
def search():
    """
    :param q: 普通关键字
    :param page:
    :return:
    """
    form = SearchForm(request.args)
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data

        isbn_or_key = is_isbn_or_key(word=q)
        if isbn_or_key == 'isbn':
            result = YuShuBook.search_by_isbn(q)
        else:
            result = YuShuBook.search_by_keyword(q, page)

        return jsonify(result)
    else:
        return jsonify({'msg': '校验参数失败'})
    # return jsonifyn.dump(result), 200, {'content-type':'application/json'}

