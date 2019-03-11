# -*- coding: utf-8 -*-

from openerp.http import EndPoint, request

from ..tools import PerfLogger, profile

native_call = EndPoint.__call__


def __call__(self, *args, **kwargs):
    if not request.uid:
        return native_call(self, *args, **kwargs)
    logger = PerfLogger()
    path = request.httprequest.environ['PATH_INFO']
    model = kwargs.get('model', '')
    method = kwargs.get('method', '')
    m_args = kwargs.get('args') if model and method else args
    m_kwargs = kwargs.get('kwargs') if model and method else kwargs
    if not method and path.split('/')[-1] == 'search_read':
        method = 'search_read'
    logger.on_enter(request.cr, request.uid, path, model, method)
    try:
        res = profile(native_call)(self, *args, **kwargs)
        logger.log_call(m_args, m_kwargs, res)
        return res
    except Exception, e:
        logger.log_call(m_args, m_kwargs, err=e)
        raise
    finally:
        logger.on_leave()

EndPoint.__call__ = __call__
