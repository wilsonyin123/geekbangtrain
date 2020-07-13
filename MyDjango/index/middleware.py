from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin
class Middle1(MiddlewareMixin):
    def process_request(self,request):
         print('中间件请求')
 
    def process_view(self, request, callback, callback_args, callback_kwargs):
         print('中间件视图')
 
    def process_exception(self, request, exception):
         print('中间件异常')
 
    def process_response(self, request, response):
         print('中间件响应')
         return response