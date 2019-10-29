from flask import jsonify
from flask import Blueprint
from helper import is_isbn_or_key
from yushu_book import YuShuBook


web = Blueprint('web', __name__)

@web.route('/book/search/<q>/<page>')
def search(q, page):
    """
    :param q: 普通关键字
    :param page:
    :return:
    """
    isbn_or_key = is_isbn_or_key(word=q)
    if isbn_or_key == 'isbn':
        result = YuShuBook.search_by_isbn(q)
    else:
        result = YuShuBook.search_by_keyword(q)

    return jsonify(result)
    # return jsonifyn.dump(result), 200, {'content-type':'application/json'}
